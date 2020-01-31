
import java.util.Arrays;

public class IntCodeMachine
{

    public IntCodeMachine( int phase, int[] in )
    {
        this.phase = phase;
        this.code = in;
        phaseSet = true;
    }

    public void setInput( int input )
    {
        this.input = input;
        inputUsed = false;
    }

    public int fetchOutput()
    {
        outputFetched = true;
        return this.output;
    }

    public void pause()
    {
        pause = true;
    }

    public void unpause()
    {
        pause = false;
    }

    public boolean isPaused()
    {
        return pause;
    }

    private int[] initialCode;
    private int[] code;// = new int[initialCode.length];
    private int machineState = 0;
    private boolean halt = false;
    private int phase;
    private int input;
    private boolean inputUsed;
    private int output;
    private boolean outputFetched;
    private boolean pause = false;
    private boolean phaseSet;
    private int relativeBase;

    public void run()
    {
        while ( !( halt || pause ) )
        {
            System.out.println( machineState );
            int currentNumber = code[ machineState ];
            int sizeOfInstruction = String.valueOf( currentNumber ).length();
            String currentNumberAsString = Integer.toString( currentNumber );
//            System.out.println( "**" + machineState + "**" );
//            System.out.println( Arrays.toString(code));

            if ( sizeOfInstruction == 1 )
            {
                processSize1Instruction( currentNumber );
                continue;
            }

            if ( sizeOfInstruction == 3 )
            {
                processSize3Instruction( currentNumberAsString );
                continue;
            }

            if ( sizeOfInstruction == 4 )
            {
                processSize4Instruction( currentNumberAsString );
                continue;
            }


            if ( currentNumber == 99 )
            {
                System.out.println("machine halted");
                halt = true;
            }
        }
    }

    public void requestInput()
    {
        if ( phaseSet )
        {
            code[ code[ machineState + 1 ] ] = phase;
            phaseSet = false;
            machineState += 2;
        }
        else if ( inputUsed )
        {
            pause();
        }
        else
        {
            code[ code[ machineState + 1 ] ] = input;
            inputUsed = true;
            machineState += 2;
        }
    }


    public void normalOpCode( int i )
    {
        if ( code[ i ] != 1 && code[ i ] != 2 )
        {
            System.out.println( "error" );
        }
        if ( code[ i ] == 1 )
        {
            code[ code[ i + 3 ] ] = code[ code[ i + 1 ] ] + code[ code[ i + 2 ] ];
        }
        else if ( code[ i ] == 2 )
        {
            code[ code[ i + 3 ] ] = code[ code[ i + 1 ] ] * code[ code[ i + 2 ] ];
        }
    }

    public void processSize1Instruction( int currentNumber )
    {
        switch ( currentNumber )
        {
            case 3:
                requestInput();
                break;


            case 4:

                output = code[ code[ machineState + 1 ] ];
                machineState += 2;
                System.out.println("output  " + output);
                break;


            case 5:
                if ( code[ code[ machineState + 1 ] ] == 0 )
                {
                    machineState += 3;
                }
                else
                {
                    machineState = code[ code[ machineState + 2 ] ];
                }
                break;

            case 6:
                if ( code[ code[ machineState + 1 ] ] != 0 )
                {
                    machineState += 3;
                }
                else
                {
                    machineState = code[ code[ machineState + 2 ] ];
                }
                break;

            case 7:
                if ( code[ code[ machineState + 1 ] ] < code[ code[ machineState + 2 ] ] )
                {
                    code[ code[ machineState + 3 ] ] = 1;
                }
                else
                {
                    code[ code[ machineState + 3 ] ] = 0;
                }
                machineState += 4;
                break;


            case 8:
                if ( code[ code[ machineState + 1 ] ] == code[ code[ machineState + 2 ] ] )
                {
                    code[ code[ machineState + 3 ] ] = 1;
                }
                else
                {
                    code[ code[ machineState + 3 ] ] = 0;
                }
                machineState += 4;
                break;

            case 9:
                relativeBase = code[ code[ machineState + 1 ] ];
                machineState +=2;
                break;

            default:
                normalOpCode( machineState );
                machineState += 4;

        }
    }

    public void processSize3Instruction( String currentNumberAsString )
    {
        if ( !currentNumberAsString.substring( 0, 1 ).equals( "1" ) && !currentNumberAsString.substring( 0, 1 ).equals( "2" ) )
        {
            System.out.println( "error" );
        }
        else if( currentNumberAsString.substring( 0, 1 ).equals( "1" ) ) // 1st param in immediate mode
        {
            if ( currentNumberAsString.substring( 2 ).equals( "1" ) )
            {
                code[ code[ machineState + 3 ] ] = code[ machineState + 1 ] + code[ code[ machineState + 2 ] ];
                machineState += 4;
            }
            else if ( currentNumberAsString.substring( 2 ).equals( "4" ) )
            {
                output = code[ machineState + 1 ];
                machineState += 2;
            }
            else if ( currentNumberAsString.substring( 2 ).equals( "5" ) )
            {
                if ( code[ machineState + 1 ] == 0 )
                {
                    machineState += 3;
                }
                else
                {
                    machineState = code[ code[ machineState + 2 ] ];
                }
            }
            else if ( currentNumberAsString.substring( 2 ).equals( "6" ) )
            {
                if ( code[ machineState + 1 ] != 0 )
                {
                    machineState += 3;
                }
                else
                {
                    machineState = code[ code[ machineState + 2 ] ];
                }
            }
            else if ( currentNumberAsString.substring( 2 ).equals( "7" ) )
            {
                if ( code[ machineState + 1 ] < code[ code[ machineState + 2 ] ] )
                {
                    code[ code[ machineState + 3 ] ] = 1;
                }
                else
                {
                    code[ code[ machineState + 3 ] ] = 0;
                }
                machineState += 4;
            }
            else if ( currentNumberAsString.substring( 2 ).equals( "8" ) )
            {
                if ( code[ machineState + 1 ] == code[ code[ machineState + 2 ] ] )
                {
                    code[ code[ machineState + 3 ] ] = 1;
                }
                else
                {
                    code[ code[ machineState + 3 ] ] = 0;
                }
                machineState += 4;
            }
            else if ( currentNumberAsString.substring( 2 ).equals( "9" ))
            {
                relativeBase = code[ machineState + 1 ];
            }
            else // should just be a 2
            {
                code[ code[ machineState + 3 ] ] = code[ machineState + 1 ] * code[ code[ machineState + 2 ] ];
                machineState += 4;
            }
        }
        else
        {
            if ( currentNumberAsString.substring( 2 ).equals( "1" ) )
            {
                code[ code[ machineState + 3 ] ] = code[ code[ machineState + 1 ] + relativeBase ] + code[ code[ machineState + 2 ] ];
                machineState += 4;
            }
            else if ( currentNumberAsString.substring( 2 ).equals( "4" ) )
            {
                output = code[ code[ machineState + 1 ] + relativeBase ];
                machineState += 2;
            }
            else if ( currentNumberAsString.substring( 2 ).equals( "5" ) )
            {
                if ( code[ code[ machineState + 1 ] + relativeBase ] == 0 )
                {
                    machineState += 3;
                }
                else
                {
                    machineState = code[ code[ machineState + 2 ] ];
                }
            }
            else if ( currentNumberAsString.substring( 2 ).equals( "6" ) )
            {
                if ( code[ code[ machineState + 1 ] + relativeBase ] != 0 )
                {
                    machineState += 3;
                }
                else
                {
                    machineState = code[ code[ machineState + 2 ] ];
                }
            }
            else if ( currentNumberAsString.substring( 2 ).equals( "7" ) )
            {
                if ( code[ code[ machineState + 1 ] + relativeBase ] < code[ code[ machineState + 2 ] ] )
                {
                    code[ code[ machineState + 3 ] ] = 1;
                }
                else
                {
                    code[ code[ machineState + 3 ] ] = 0;
                }
                machineState += 4;
            }
            else if ( currentNumberAsString.substring( 2 ).equals( "8" ) )
            {
                if ( code[ code[ machineState + 1 ] + relativeBase ] == code[ code[ machineState + 2 ] ] )
                {
                    code[ code[ machineState + 3 ] ] = 1;
                }
                else
                {
                    code[ code[ machineState + 3 ] ] = 0;
                }
                machineState += 4;
            }
            else if ( currentNumberAsString.substring( 2 ).equals( "9" ))
            {
                relativeBase = code[ code[ machineState + 1 ] + relativeBase ];
            }
            else // should just be a 2
            {
                code[ code[ machineState + 3 ] ] = code[ machineState + 1 ] * code[ code[ machineState + 2 ] ];
                machineState += 4;
            }
        }

    }

    public void processSize4Instruction( String currentNumberAsString ) // TODO WRITE IN PARAM MODE 2 INTO THIS BIT!!
    {
        if ( !currentNumberAsString.substring( 0, 1 ).equals( "1" ) )
        {
            System.out.println( "error" );
        }
        else // 2nd param in immediate mode
        {
            if ( currentNumberAsString.substring( 1, 2 ).equals( "1" ) ) // both params in immediate mode
            {
                if ( currentNumberAsString.substring( 3 ).equals( "1" ) )
                {
                    code[ code[ machineState + 3 ] ] = code[ machineState + 1 ] + code[ machineState + 2 ];
                    machineState += 4;
                }
                else if ( currentNumberAsString.substring( 3 ).equals( "5" ) )
                {
                    if ( code[ machineState + 1 ] == 0 )
                    {
                        machineState += 3;
                    }
                    else
                    {
                        machineState = code[ machineState + 2 ];
                    }
                }
                else if ( currentNumberAsString.substring( 3 ).equals( "6" ) )
                {
                    if ( code[ machineState + 1 ] != 0 )
                    {
                        machineState += 3;
                    }
                    else
                    {
                        machineState = code[ machineState + 2 ];
                    }
                }
                else if ( currentNumberAsString.substring( 3 ).equals( "7" ) )
                {
                    if ( code[ machineState + 1 ] < code[ machineState + 2 ] )
                    {
                        code[ code[ machineState + 3 ] ] = 1;
                    }
                    else
                    {
                        code[ code[ machineState + 3 ] ] = 0;
                    }
                    machineState += 4;
                }
                else if ( currentNumberAsString.substring( 3 ).equals( "8" ) )
                {
                    if ( code[ machineState + 1 ] == code[ machineState + 2 ] )
                    {
                        code[ code[ machineState + 3 ] ] = 1;
                    }
                    else
                    {
                        code[ code[ machineState + 3 ] ] = 0;
                    }
                    machineState += 4;
                }
                else // should just be a 2
                {
                    code[ code[ machineState + 3 ] ] = code[ machineState + 1 ] * code[ machineState + 2 ];
                    machineState += 4;
                }
            }
            else
            {
                if ( currentNumberAsString.substring( 3 ).equals( "1" ) )
                {
                    code[ code[ machineState + 3 ] ] =
                            code[ code[ machineState + 1 ] ] + code[ machineState + 2 ];
                    machineState += 4;
                }
                else if ( currentNumberAsString.substring( 3 ).equals( "5" ) )
                {
                    if ( code[ code[ machineState + 1 ] ] == 0 )
                    {
                        machineState += 3;
                    }
                    else
                    {
                        machineState = code[ machineState + 2 ];
                    }
                }
                else if ( currentNumberAsString.substring( 3 ).equals( "6" ) )
                {
                    if ( code[ code[ machineState + 1 ] ] != 0 )
                    {
                        machineState += 3;
                    }
                    else
                    {
                        machineState = code[ machineState + 2 ];
                    }
                }
                else if ( currentNumberAsString.substring( 3 ).equals( "7" ) )
                {
                    if ( code[ code[ machineState + 1 ] ] < code[ machineState + 2 ] )
                    {
                        code[ code[ machineState + 3 ] ] = 1;
                    }
                    else
                    {
                        code[ code[ machineState + 3 ] ] = 0;
                    }
                    machineState += 4;
                }
                else if ( currentNumberAsString.substring( 3 ).equals( "8" ) )
                {
                    if ( code[ code[ machineState + 1 ] ] == code[ machineState + 2 ] )
                    {
                        code[ code[ machineState + 3 ] ] = 1;
                    }
                    else
                    {
                        code[ code[ machineState + 3 ] ] = 0;
                    }
                    machineState += 4;
                }
                else // should just be a 2
                {
                    code[ code[ machineState + 3 ] ] =
                            code[ code[ machineState + 1 ] ] * code[ machineState + 2 ];
                    machineState += 4;
                }
            }
        }
    }


}
