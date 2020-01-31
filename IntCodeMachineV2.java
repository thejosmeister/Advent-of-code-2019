

import java.util.HashMap;
import java.util.Map;
import java.util.stream.Collectors;

public class IntCodeMachineV2
{

    public IntCodeMachineV2( long phase, int[] in )
    {
        this.phase = phase;
        phaseSet = true;

        codeMap = new HashMap<Long, Long>()
        {
        };

        for ( int i = 0; i < in.length; i++ )
        {
            codeMap.put( ( long ) i, ( long ) in[ i ] );
        }
    }

    public IntCodeMachineV2( long[] in )
    {
        codeMap = new HashMap<Long, Long>();

        for ( int i = 0; i < in.length; i++ )
        {
            codeMap.put( ( long ) i, in[ i ] );
        }
    }

    public void setInput( long input )
    {
        this.input = input;
        inputUsed = false;
    }

    public long fetchOutput()
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

    private Map<Long, Long> codeMap;
    private long machineState = 0;
    private boolean halt = false;
    private long phase;
    private long input;
    private boolean inputUsed;
    private long output;
    private boolean outputFetched;
    private boolean pause = false;
    private boolean phaseSet;
    private long relativeBase = 0;

    public void run()
    {
        while ( !( halt || pause ) )
        {
            System.out.println( machineState );
            String currentNumber = Long.toString( codeMap.getOrDefault( machineState, ( long ) 0 ) );
            System.out.println( "current number " + currentNumber);
            System.out.println( "relative base " + relativeBase );
            System.out.println(" ");
            System.out.println("state of 63: " + codeMap.get( (long) 63 ));
            System.out.println(" ");
            System.out.println(" ");
            System.out.println(" ");
            System.out.println(" ");
            int sizeOfInstruction = currentNumber.length();
//            System.out.println( "**" + machineState + "**" );
//            System.out.println( Arrays.toString(codeMap));

            if ( sizeOfInstruction == 1 )
            {
                processSize1Instruction( currentNumber );
                continue;
            }

            if ( sizeOfInstruction == 3 )
            {
                processSize3Instruction( currentNumber );
                continue;
            }

            if ( sizeOfInstruction == 4 )
            {
                processSize4Instruction( currentNumber );
                continue;
            }

            if ( sizeOfInstruction == 5 )
            {
                processSize5Instruction( currentNumber );
                continue;
            }

            if ( currentNumber.equals( "99" ) )
            {
                System.out.println( "machine halted" );
                halt = true;
            }

            if( sizeOfInstruction > 5 )
            {
                System.out.println("large instruction");
                halt = true;
            }
        }
    }

    public void requestInput()
    {
        if ( phaseSet )
        {
            codeMap.put( ( long ) 1, phase );
            phaseSet = false;
            machineState += 2;
        }
        else if ( inputUsed )
        {
            pause();
        }
        else
        {
            codeMap.put( codeMap.getOrDefault( machineState + 1, ( long ) 0 ), input );
            inputUsed = true;
            machineState += 2;
        }
    }


    public void normalOpcodeMap( long i )
    {
        if ( codeMap.getOrDefault( i, ( long ) 0 ) != 1 && codeMap.getOrDefault( i, ( long ) 0 ) != 2 )
        {
            System.out.println( "error" );
        }
        if ( codeMap.getOrDefault( i, ( long ) 0 ) == 1 )
        {
            codeMap.put( codeMap.getOrDefault( i + 3, ( long ) 0 ),
                    codeMap.getOrDefault( codeMap.getOrDefault( i + 1, ( long ) 0 ), ( long ) 0 ) + codeMap
                            .getOrDefault( codeMap.getOrDefault( i + 2, ( long ) 0 ), ( long ) 0 ) );
        }
        else if ( codeMap.getOrDefault( i, ( long ) 0 ) == 2 )
        {
            codeMap.put( codeMap.getOrDefault( i + 3, ( long ) 0 ),
                    codeMap.getOrDefault( codeMap.getOrDefault( i + 1, ( long ) 0 ), ( long ) 0 ) * codeMap
                            .getOrDefault( codeMap.getOrDefault( i + 2, ( long ) 0 ), ( long ) 0 ) );
        }
    }

    public void processSize1Instruction( String currentNumber )
    {
        char current = currentNumber.charAt( 0 );
        switch ( current )
        {
            case '3':
                requestInput();
                break;


            case '4':

                output = codeMap.getOrDefault( codeMap.getOrDefault( machineState + 1, ( long ) 0 ), ( long ) 0 );
                machineState += 2;
                System.out.println( "output  " + output + "---------------------------------------------------------");
                System.out.println( codeMap.keySet().stream()
                        .map(key -> key + "=" + codeMap.get(key))
                        .collect( Collectors.joining(", ", "{", "}") ) );
                break;


            case '5':
                if ( codeMap.getOrDefault( codeMap.getOrDefault( machineState + 1, ( long ) 0 ), ( long ) 0 ) == 0 )
                {
                    machineState += 3;
                }
                else
                {
                    machineState =
                            codeMap.getOrDefault( codeMap.getOrDefault( machineState + 2, ( long ) 0 ), ( long ) 0 );
                }
                break;

            case '6':
                if ( codeMap.getOrDefault( codeMap.getOrDefault( machineState + 1, ( long ) 0 ), ( long ) 0 ) != 0 )
                {
                    machineState += 3;
                }
                else
                {
                    machineState =
                            codeMap.getOrDefault( codeMap.getOrDefault( machineState + 2, ( long ) 0 ), ( long ) 0 );
                }
                break;

            case '7':
                if ( codeMap.getOrDefault( codeMap.getOrDefault( machineState + 1, ( long ) 0 ), ( long ) 0 ) < codeMap
                        .getOrDefault( codeMap.getOrDefault( machineState + 2, ( long ) 0 ), ( long ) 0 ) )
                {
                    codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ), ( long ) 1 );
                }
                else
                {
                    codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ), ( long ) 0 );
                }
                machineState += 4;
                break;


            case '8':
                if ( codeMap.getOrDefault( codeMap.getOrDefault( machineState + 1, ( long ) 0 ), ( long ) 0 )
                        .equals( codeMap
                                .getOrDefault( codeMap.getOrDefault( machineState + 2, ( long ) 0 ), ( long ) 0 ) ) )
                {
                    codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ), ( long ) 1 );
                }
                else
                {
                    codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ), ( long ) 0 );
                }
                machineState += 4;
                break;

            case '9':
                relativeBase += codeMap.getOrDefault( codeMap.getOrDefault( machineState + 1, ( long ) 0 ), ( long ) 0 );
                machineState += 2;
                break;

            default:
                normalOpcodeMap( machineState );
                machineState += 4;

        }
    }

    public void processSize3Instruction( String currentNumberAsString )
    {
        if ( !currentNumberAsString.substring( 0, 1 ).equals( "1" ) && !currentNumberAsString.substring( 0, 1 )
                .equals( "2" ) )
        {
            System.out.println( "error" );
        }
        else if ( currentNumberAsString.substring( 0, 1 ).equals( "1" ) ) // 1st param in immediate mode
        {
            if ( currentNumberAsString.substring( 2 ).equals( "1" ) )
            {
                codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ),
                        codeMap.getOrDefault( machineState + 1, ( long ) 0 )
                                + codeMap
                                .getOrDefault( codeMap.getOrDefault( machineState + 2, ( long ) 0 ), ( long ) 0 ) );
                machineState += 4;
            }
            else if ( currentNumberAsString.substring( 2 ).equals( "4" ) )
            {
                output = codeMap.getOrDefault( machineState + 1, ( long ) 0 );
                machineState += 2;
                System.out.println( "output  " + output + "---------------------------------------------------------" );
                System.out.println( codeMap.keySet().stream()
                        .map(key -> key + "=" + codeMap.get(key))
                        .collect( Collectors.joining(", ", "{", "}") ) );
            }
            else if ( currentNumberAsString.substring( 2 ).equals( "5" ) )
            {
                if ( codeMap.getOrDefault( machineState + 1, ( long ) 0 ) == 0 )
                {
                    machineState += 3;
                }
                else
                {
                    machineState =
                            codeMap.getOrDefault( codeMap.getOrDefault( machineState + 2, ( long ) 0 ), ( long ) 0 );
                }
            }
            else if ( currentNumberAsString.substring( 2 ).equals( "6" ) )
            {
                if ( codeMap.getOrDefault( machineState + 1, ( long ) 0 ) != 0 )
                {
                    machineState += 3;
                }
                else
                {
                    machineState =
                            codeMap.getOrDefault( codeMap.getOrDefault( machineState + 2, ( long ) 0 ), ( long ) 0 );
                }
            }
            else if ( currentNumberAsString.substring( 2 ).equals( "7" ) )
            {
                if ( codeMap.getOrDefault( machineState + 1, ( long ) 0 ) < codeMap
                        .getOrDefault( codeMap.getOrDefault( machineState + 2, ( long ) 0 ), ( long ) 0 ) )
                {
                    codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ), ( long ) 1 );
                }
                else
                {
                    codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ), ( long ) 0 );
                }
                machineState += 4;
            }
            else if ( currentNumberAsString.substring( 2 ).equals( "8" ) )
            {
                if ( codeMap.getOrDefault( machineState + 1, ( long ) 0 ).equals( codeMap
                        .getOrDefault( codeMap.getOrDefault( machineState + 2, ( long ) 0 ), ( long ) 0 ) ) )
                {
                    codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ), ( long ) 1 );
                }
                else
                {
                    codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ), ( long ) 0 );
                }
                machineState += 4;
            }
            else if ( currentNumberAsString.substring( 2 ).equals( "9" ) )
            {
                relativeBase += codeMap.getOrDefault( machineState + 1, ( long ) 0 );
                machineState += 2;
            }
            else // should just be a 2
            {
                codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ),
                        codeMap.getOrDefault( machineState + 1, ( long ) 0 )
                                * codeMap
                                .getOrDefault( codeMap.getOrDefault( machineState + 2, ( long ) 0 ), ( long ) 0 ) );
                machineState += 4;
            }
        }
        else
        {
            if ( currentNumberAsString.substring( 2 ).equals( "1" ) )
            {
                codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ),
                        codeMap.getOrDefault( codeMap.getOrDefault( machineState + 1, ( long ) 0 ) + relativeBase,
                                ( long ) 0 )
                                + codeMap
                                .getOrDefault( codeMap.getOrDefault( machineState + 2, ( long ) 0 ), ( long ) 0 ) );
                machineState += 4;
            }
            else if ( currentNumberAsString.substring( 2 ).equals( "3" ) )
            {
                codeMap.put( codeMap.getOrDefault( machineState + 1, (long) 0 ) + relativeBase, input );
                inputUsed = true;
                machineState += 2;
            }
            else if ( currentNumberAsString.substring( 2 ).equals( "4" ) )
            {
                output = codeMap.getOrDefault( codeMap.getOrDefault( machineState + 1, ( long ) 0 ) + relativeBase,
                        ( long ) 0 );
                machineState += 2;
                System.out.println( "output  " + output + "---------------------------------------------------------" );
                System.out.println( codeMap.keySet().stream()
                        .map(key -> key + "=" + codeMap.get(key))
                        .collect( Collectors.joining(", ", "{", "}") ) );
            }
            else if ( currentNumberAsString.substring( 2 ).equals( "5" ) )
            {
                if ( codeMap
                        .getOrDefault( codeMap.getOrDefault( machineState + 1, ( long ) 0 ) + relativeBase, ( long ) 0 )
                        == 0 )
                {
                    machineState += 3;
                }
                else
                {
                    machineState =
                            codeMap.getOrDefault( codeMap.getOrDefault( machineState + 2, ( long ) 0 ), ( long ) 0 );
                }
            }
            else if ( currentNumberAsString.substring( 2 ).equals( "6" ) )
            {
                if ( codeMap
                        .getOrDefault( codeMap.getOrDefault( machineState + 1, ( long ) 0 ) + relativeBase, ( long ) 0 )
                        != 0 )
                {
                    machineState += 3;
                }
                else
                {
                    machineState =
                            codeMap.getOrDefault( codeMap.getOrDefault( machineState + 2, ( long ) 0 ), ( long ) 0 );
                }
            }
            else if ( currentNumberAsString.substring( 2 ).equals( "7" ) )
            {
                if ( codeMap
                        .getOrDefault( codeMap.getOrDefault( machineState + 1, ( long ) 0 ) + relativeBase, ( long ) 0 )
                        <
                        codeMap.getOrDefault( codeMap.getOrDefault( machineState + 2, ( long ) 0 ), ( long ) 0 ) )
                {
                    codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ), ( long ) 1 );
                }
                else
                {
                    codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ), ( long ) 0 );
                }
                machineState += 4;
            }
            else if ( currentNumberAsString.substring( 2 ).equals( "8" ) )
            {
                if ( codeMap
                        .getOrDefault( codeMap.getOrDefault( machineState + 1, ( long ) 0 ) + relativeBase, ( long ) 0 )
                        .equals( codeMap.getOrDefault( codeMap.getOrDefault( machineState + 2, ( long ) 0 ),
                                ( long ) 0 ) ) )
                {
                    codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ), ( long ) 1 );
                }
                else
                {
                    codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ), ( long ) 0 );
                }
                machineState += 4;
            }
            else if ( currentNumberAsString.substring( 2 ).equals( "9" ) )
            {
                relativeBase +=
                        codeMap.getOrDefault( codeMap.getOrDefault( machineState + 1, ( long ) 0 ) + relativeBase,
                                ( long ) 0 );
                machineState += 2;
            }
            else // should just be a 2
            {
                codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ),
                        codeMap.getOrDefault( codeMap.getOrDefault( machineState + 1, ( long ) 0 ) + relativeBase,
                                ( long ) 0 )
                                * codeMap
                                .getOrDefault( codeMap.getOrDefault( machineState + 2, ( long ) 0 ), ( long ) 0 ) );
                machineState += 4;
            }
        }

    }

    public void processSize4Instruction( String currentNumberAsString )
    {
        if ( !currentNumberAsString.substring( 0, 1 ).equals( "1" ) && !currentNumberAsString.substring( 0, 1 )
                .equals( "2" ) )
        {
            System.out.println( "error" );
        }
        else // 2nd param in immediate mode
        {
            int firstParamMode = Integer.parseInt( currentNumberAsString.substring( 1, 2 ) );
            int secondParamMode = Integer.parseInt( currentNumberAsString.substring( 0, 1 ) );

            if ( currentNumberAsString.substring( 3 ).equals( "1" ) )
            {
                if ( firstParamMode == 1 )
                {
                    switch ( secondParamMode )
                    {
                        case 1:
                            codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ),
                                    codeMap.getOrDefault( machineState + 1, ( long ) 0 ) + codeMap
                                            .getOrDefault( machineState + 2, ( long ) 0 ) );
                            break;

                        case 2:
                            codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ),
                                    codeMap.getOrDefault( machineState + 1, ( long ) 0 ) + codeMap
                                            .getOrDefault(
                                                    codeMap.getOrDefault( machineState + 2, ( long ) 0 ) + relativeBase,
                                                    ( long ) 0 ) );
                            break;

                        default:
                            codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ),
                                    codeMap.getOrDefault( machineState + 1, ( long ) 0 ) + codeMap
                                            .getOrDefault( codeMap.getOrDefault( machineState + 2, ( long ) 0 ),
                                                    ( long ) 0 ) );
                    }
                }
                else if ( firstParamMode == 2 )
                {
                    switch ( secondParamMode )
                    {
                        case 1:
                            codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ),
                                    codeMap.getOrDefault(
                                            codeMap.getOrDefault( machineState + 1, ( long ) 0 ) + relativeBase,
                                            ( long ) 0 ) + codeMap
                                            .getOrDefault( machineState + 2, ( long ) 0 ) );
                            System.out.println("got to correct place for 1201*********************************************");
                            break;

                        case 2:
                            codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ),
                                    codeMap.getOrDefault(
                                            codeMap.getOrDefault( machineState + 1, ( long ) 0 ) + relativeBase,
                                            ( long ) 0 ) + codeMap
                                            .getOrDefault(
                                                    codeMap.getOrDefault( machineState + 2, ( long ) 0 ) + relativeBase,
                                                    ( long ) 0 ) );
                            break;

                        default:
                            codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ),
                                    codeMap.getOrDefault(
                                            codeMap.getOrDefault( machineState + 1, ( long ) 0 ) + relativeBase,
                                            ( long ) 0 ) + codeMap
                                            .getOrDefault( codeMap.getOrDefault( machineState + 2, ( long ) 0 ),
                                                    ( long ) 0 ) );
                    }
                }
                else
                {
                    switch ( secondParamMode )
                    {
                        case 1:
                            codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ),
                                    codeMap.getOrDefault( codeMap.getOrDefault( machineState + 1, ( long ) 0 ),
                                            ( long ) 0 ) + codeMap
                                            .getOrDefault( machineState + 2, ( long ) 0 ) );
                            break;

                        case 2:
                            codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ),
                                    codeMap.getOrDefault( codeMap.getOrDefault( machineState + 1, ( long ) 0 ),
                                            ( long ) 0 ) + codeMap
                                            .getOrDefault(
                                                    codeMap.getOrDefault( machineState + 2, ( long ) 0 ) + relativeBase,
                                                    ( long ) 0 ) );
                            break;

                        default:
                            codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ),
                                    codeMap.getOrDefault( codeMap.getOrDefault( machineState + 1, ( long ) 0 ),
                                            ( long ) 0 ) + codeMap
                                            .getOrDefault( codeMap.getOrDefault( machineState + 2, ( long ) 0 ),
                                                    ( long ) 0 ) );
                    }
                }
                machineState += 4;
            }
            else if ( currentNumberAsString.substring( 3 ).equals( "5" ) || currentNumberAsString.substring( 3 )
                    .equals( "6" ) )
            {
                long paramValue;
                long resultantValue;
                if ( firstParamMode == 1 )
                {
                    paramValue = codeMap.getOrDefault( machineState + 1, ( long ) 0 );

                    switch ( secondParamMode )
                    {
                        case 1:
                            resultantValue = codeMap.getOrDefault( machineState + 2, ( long ) 0 );
                            break;

                        case 2:
                            resultantValue = codeMap.getOrDefault(
                                    codeMap.getOrDefault( machineState + 2, ( long ) 0 ) + relativeBase, ( long ) 0 );
                            break;

                        default:
                            resultantValue = codeMap.getOrDefault( codeMap.getOrDefault( machineState + 2, ( long ) 0 ),
                                    ( long ) 0 );
                    }
                }
                else if ( firstParamMode == 2 )
                {
                    paramValue =
                            codeMap.getOrDefault( codeMap.getOrDefault( machineState + 1, ( long ) 0 ) + relativeBase,
                                    ( long ) 0 );

                    switch ( secondParamMode )
                    {
                        case 1:
                            resultantValue = codeMap.getOrDefault( machineState + 2, ( long ) 0 );
                            break;

                        case 2:
                            resultantValue = codeMap.getOrDefault(
                                    codeMap.getOrDefault( machineState + 2, ( long ) 0 ) + relativeBase, ( long ) 0 );
                            break;

                        default:
                            resultantValue = codeMap.getOrDefault( codeMap.getOrDefault( machineState + 2, ( long ) 0 ),
                                    ( long ) 0 );
                    }
                }
                else
                {
                    paramValue =
                            codeMap.getOrDefault( codeMap.getOrDefault( machineState + 1, ( long ) 0 ), ( long ) 0 );

                    switch ( secondParamMode )
                    {
                        case 1:
                            resultantValue = codeMap.getOrDefault( machineState + 2, ( long ) 0 );
                            break;

                        case 2:
                            resultantValue = codeMap.getOrDefault(
                                    codeMap.getOrDefault( machineState + 2, ( long ) 0 ) + relativeBase, ( long ) 0 );
                            break;

                        default:
                            resultantValue = codeMap.getOrDefault( codeMap.getOrDefault( machineState + 2, ( long ) 0 ),
                                    ( long ) 0 );
                    }
                }

                if ( currentNumberAsString.substring( 3 ).equals( "5" ) )
                {
                    if ( paramValue == 0 )
                    {
                        machineState += 3;
                    }
                    else
                    {
                        machineState = resultantValue;
                    }
                }
                else
                {
                    if ( paramValue != 0 )
                    {
                        machineState += 3;
                    }
                    else
                    {
                        machineState = resultantValue;
                    }
                }
            }
            else if ( currentNumberAsString.substring( 3 ).equals( "7" ) || currentNumberAsString.substring( 3 )
                    .equals( "8" ) )
            {
                long firstParamValue;
                long secondParamValue;
                if ( firstParamMode == 1 )
                {
                    firstParamValue = codeMap.getOrDefault( machineState + 1, ( long ) 0 );

                    switch ( secondParamMode )
                    {
                        case 1:
                            secondParamValue = codeMap.getOrDefault( machineState + 2, ( long ) 0 );
                            break;

                        case 2:
                            secondParamValue = codeMap.getOrDefault(
                                    codeMap.getOrDefault( machineState + 2, ( long ) 0 ) + relativeBase, ( long ) 0 );
                            break;

                        default:
                            secondParamValue =
                                    codeMap.getOrDefault( codeMap.getOrDefault( machineState + 2, ( long ) 0 ),
                                            ( long ) 0 );
                    }
                }
                else if ( firstParamMode == 2 )
                {
                    firstParamValue =
                            codeMap.getOrDefault( codeMap.getOrDefault( machineState + 1, ( long ) 0 ) + relativeBase,
                                    ( long ) 0 );

                    switch ( secondParamMode )
                    {
                        case 1:
                            secondParamValue = codeMap.getOrDefault( machineState + 2, ( long ) 0 );
                            break;

                        case 2:
                            secondParamValue = codeMap.getOrDefault(
                                    codeMap.getOrDefault( machineState + 2, ( long ) 0 ) + relativeBase, ( long ) 0 );
                            break;

                        default:
                            secondParamValue =
                                    codeMap.getOrDefault( codeMap.getOrDefault( machineState + 2, ( long ) 0 ),
                                            ( long ) 0 );
                    }
                }
                else
                {
                    firstParamValue =
                            codeMap.getOrDefault( codeMap.getOrDefault( machineState + 1, ( long ) 0 ), ( long ) 0 );

                    switch ( secondParamMode )
                    {
                        case 1:
                            secondParamValue = codeMap.getOrDefault( machineState + 2, ( long ) 0 );
                            break;

                        case 2:
                            secondParamValue = codeMap.getOrDefault(
                                    codeMap.getOrDefault( machineState + 2, ( long ) 0 ) + relativeBase, ( long ) 0 );
                            break;

                        default:
                            secondParamValue =
                                    codeMap.getOrDefault( codeMap.getOrDefault( machineState + 2, ( long ) 0 ),
                                            ( long ) 0 );
                    }
                }

                if ( currentNumberAsString.substring( 3 ).equals( "7" ) )
                {
                    if ( firstParamValue < secondParamValue )
                    {
                        codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ), ( long ) 1 );
                    }
                    else
                    {
                        codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ), ( long ) 0 );
                    }
                }
                else
                {
                    if ( firstParamValue == secondParamValue )
                    {
                        codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ), ( long ) 1 );
                    }
                    else
                    {
                        codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ), ( long ) 0 );
                    }
                }
                machineState += 4;
            }
            else // opcode is 2
            {
                if ( firstParamMode == 1 )
                {
                    switch ( secondParamMode )
                    {
                        case 1:
                            codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ),
                                    codeMap.getOrDefault( machineState + 1, ( long ) 0 ) * codeMap
                                            .getOrDefault( machineState + 2, ( long ) 0 ) );
                            break;

                        case 2:
                            codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ),
                                    codeMap.getOrDefault( machineState + 1, ( long ) 0 ) * codeMap
                                            .getOrDefault(
                                                    codeMap.getOrDefault( machineState + 2, ( long ) 0 ) + relativeBase,
                                                    ( long ) 0 ) );
                            break;

                        default:
                            codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ),
                                    codeMap.getOrDefault( machineState + 1, ( long ) 0 ) * codeMap
                                            .getOrDefault( codeMap.getOrDefault( machineState + 2, ( long ) 0 ),
                                                    ( long ) 0 ) );
                    }
                }
                else if ( firstParamMode == 2 )
                {
                    switch ( secondParamMode )
                    {
                        case 1:
                            codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ),
                                    codeMap.getOrDefault(
                                            codeMap.getOrDefault( machineState + 1, ( long ) 0 ) + relativeBase,
                                            ( long ) 0 ) * codeMap
                                            .getOrDefault( machineState + 2, ( long ) 0 ) );
                            break;

                        case 2:
                            codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ),
                                    codeMap.getOrDefault(
                                            codeMap.getOrDefault( machineState + 1, ( long ) 0 ) + relativeBase,
                                            ( long ) 0 ) * codeMap
                                            .getOrDefault(
                                                    codeMap.getOrDefault( machineState + 2, ( long ) 0 ) + relativeBase,
                                                    ( long ) 0 ) );
                            break;

                        default:
                            codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ),
                                    codeMap.getOrDefault(
                                            codeMap.getOrDefault( machineState + 1, ( long ) 0 ) + relativeBase,
                                            ( long ) 0 ) * codeMap
                                            .getOrDefault( codeMap.getOrDefault( machineState + 2, ( long ) 0 ),
                                                    ( long ) 0 ) );
                    }
                }
                else
                {
                    switch ( secondParamMode )
                    {
                        case 1:
                            codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ),
                                    codeMap.getOrDefault( codeMap.getOrDefault( machineState + 1, ( long ) 0 ),
                                            ( long ) 0 ) * codeMap
                                            .getOrDefault( machineState + 2, ( long ) 0 ) );
                            break;

                        case 2:
                            codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ),
                                    codeMap.getOrDefault( codeMap.getOrDefault( machineState + 1, ( long ) 0 ),
                                            ( long ) 0 ) * codeMap
                                            .getOrDefault(
                                                    codeMap.getOrDefault( machineState + 2, ( long ) 0 ) + relativeBase,
                                                    ( long ) 0 ) );
                            break;

                        default:
                            codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ),
                                    codeMap.getOrDefault( codeMap.getOrDefault( machineState + 1, ( long ) 0 ),
                                            ( long ) 0 ) * codeMap
                                            .getOrDefault( codeMap.getOrDefault( machineState + 2, ( long ) 0 ),
                                                    ( long ) 0 ) );
                    }
                }
                machineState += 4;
            }
        }
    }

    public void processSize5Instruction( String currentNumberAsString )
    {
        if( !currentNumberAsString.substring( 0, 1 ).equals( "2" ))
        {
            System.out.println("error");
        }
        else // 3rd param will be in relative mode
        {
            int firstParamMode = Integer.parseInt( currentNumberAsString.substring( 2, 3 ) );
            int secondParamMode = Integer.parseInt( currentNumberAsString.substring( 1, 2 ) );

            if ( currentNumberAsString.substring( 4 ).equals( "1" ) )
            {
                if ( firstParamMode == 1 )
                {
                    switch ( secondParamMode )
                    {
                        case 1:
                            codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ) + relativeBase,
                                    codeMap.getOrDefault( machineState + 1, ( long ) 0 ) + codeMap
                                            .getOrDefault( machineState + 2, ( long ) 0 ) );
                            break;

                        case 2:
                            codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ) + relativeBase,
                                    codeMap.getOrDefault( machineState + 1, ( long ) 0 ) + codeMap
                                            .getOrDefault(
                                                    codeMap.getOrDefault( machineState + 2, ( long ) 0 ) + relativeBase,
                                                    ( long ) 0 ) );
                            break;

                        default:
                            codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ) + relativeBase,
                                    codeMap.getOrDefault( machineState + 1, ( long ) 0 ) + codeMap
                                            .getOrDefault( codeMap.getOrDefault( machineState + 2, ( long ) 0 ),
                                                    ( long ) 0 ) );
                    }
                }
                else if ( firstParamMode == 2 )
                {
                    switch ( secondParamMode )
                    {
                        case 1:
                            codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ) + relativeBase,
                                    codeMap.getOrDefault(
                                            codeMap.getOrDefault( machineState + 1, ( long ) 0 ) + relativeBase,
                                            ( long ) 0 ) + codeMap
                                            .getOrDefault( machineState + 2, ( long ) 0 ) );
                            break;

                        case 2:
                            codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ) + relativeBase,
                                    codeMap.getOrDefault(
                                            codeMap.getOrDefault( machineState + 1, ( long ) 0 ) + relativeBase,
                                            ( long ) 0 ) + codeMap
                                            .getOrDefault(
                                                    codeMap.getOrDefault( machineState + 2, ( long ) 0 ) + relativeBase,
                                                    ( long ) 0 ) );
                            break;

                        default:
                            codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ) + relativeBase,
                                    codeMap.getOrDefault(
                                            codeMap.getOrDefault( machineState + 1, ( long ) 0 ) + relativeBase,
                                            ( long ) 0 ) + codeMap
                                            .getOrDefault( codeMap.getOrDefault( machineState + 2, ( long ) 0 ),
                                                    ( long ) 0 ) );
                    }
                }
                else //first param in position mode
                {
                    switch ( secondParamMode )
                    {
                        case 1:
                            codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ) + relativeBase,
                                    codeMap.getOrDefault( codeMap.getOrDefault( machineState + 1, ( long ) 0 ),
                                            ( long ) 0 ) + codeMap
                                            .getOrDefault( machineState + 2, ( long ) 0 ) );
                            break;

                        case 2:
                            codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ) + relativeBase,
                                    codeMap.getOrDefault( codeMap.getOrDefault( machineState + 1, ( long ) 0 ),
                                            ( long ) 0 ) + codeMap
                                            .getOrDefault(
                                                    codeMap.getOrDefault( machineState + 2, ( long ) 0 ) + relativeBase,
                                                    ( long ) 0 ) );
                            break;

                        default:
                            codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ) + relativeBase,
                                    codeMap.getOrDefault( codeMap.getOrDefault( machineState + 1, ( long ) 0 ),
                                            ( long ) 0 ) + codeMap
                                            .getOrDefault( codeMap.getOrDefault( machineState + 2, ( long ) 0 ),
                                                    ( long ) 0 ) );
                    }
                }
                machineState += 4;
            }
            else if ( currentNumberAsString.substring( 4 ).equals( "7" ) || currentNumberAsString.substring( 4 )
                    .equals( "8" ) )
            {
                long firstParamValue;
                long secondParamValue;
                if ( firstParamMode == 1 )
                {
                    firstParamValue = codeMap.getOrDefault( machineState + 1, ( long ) 0 );

                    switch ( secondParamMode )
                    {
                        case 1:
                            secondParamValue = codeMap.getOrDefault( machineState + 2, ( long ) 0 );
                            break;

                        case 2:
                            secondParamValue = codeMap.getOrDefault(
                                    codeMap.getOrDefault( machineState + 2, ( long ) 0 ) + relativeBase, ( long ) 0 );
                            break;

                        default:
                            secondParamValue =
                                    codeMap.getOrDefault( codeMap.getOrDefault( machineState + 2, ( long ) 0 ),
                                            ( long ) 0 );
                    }
                }
                else if ( firstParamMode == 2 )
                {
                    firstParamValue =
                            codeMap.getOrDefault( codeMap.getOrDefault( machineState + 1, ( long ) 0 ) + relativeBase,
                                    ( long ) 0 );

                    switch ( secondParamMode )
                    {
                        case 1:
                            secondParamValue = codeMap.getOrDefault( machineState + 2, ( long ) 0 );
                            break;

                        case 2:
                            secondParamValue = codeMap.getOrDefault(
                                    codeMap.getOrDefault( machineState + 2, ( long ) 0 ) + relativeBase, ( long ) 0 );
                            break;

                        default:
                            secondParamValue =
                                    codeMap.getOrDefault( codeMap.getOrDefault( machineState + 2, ( long ) 0 ),
                                            ( long ) 0 );
                    }
                }
                else
                {
                    firstParamValue =
                            codeMap.getOrDefault( codeMap.getOrDefault( machineState + 1, ( long ) 0 ), ( long ) 0 );

                    switch ( secondParamMode )
                    {
                        case 1:
                            secondParamValue = codeMap.getOrDefault( machineState + 2, ( long ) 0 );
                            break;

                        case 2:
                            secondParamValue = codeMap.getOrDefault(
                                    codeMap.getOrDefault( machineState + 2, ( long ) 0 ) + relativeBase, ( long ) 0 );
                            break;

                        default:
                            secondParamValue =
                                    codeMap.getOrDefault( codeMap.getOrDefault( machineState + 2, ( long ) 0 ),
                                            ( long ) 0 );
                    }
                }

                if ( currentNumberAsString.substring( 4 ).equals( "7" ) )
                {
                    if ( firstParamValue < secondParamValue )
                    {
                        codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ) + relativeBase, ( long ) 1 );
                    }
                    else
                    {
                        codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ) + relativeBase, ( long ) 0 );
                    }
                }
                else
                {
                    if ( firstParamValue == secondParamValue )
                    {
                        codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ) + relativeBase, ( long ) 1 );
                    }
                    else
                    {
                        codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ) + relativeBase, ( long ) 0 );
                    }
                }
                machineState += 4;
            }
            else // opcode is 2
            {
                if ( firstParamMode == 1 )
                {
                    switch ( secondParamMode )
                    {
                        case 1:
                            codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ) + relativeBase,
                                    codeMap.getOrDefault( machineState + 1, ( long ) 0 ) * codeMap
                                            .getOrDefault( machineState + 2, ( long ) 0 ) );
                            break;

                        case 2:
                            codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ) + relativeBase,
                                    codeMap.getOrDefault( machineState + 1, ( long ) 0 ) * codeMap
                                            .getOrDefault(
                                                    codeMap.getOrDefault( machineState + 2, ( long ) 0 ) + relativeBase,
                                                    ( long ) 0 ) );
                            break;

                        default:
                            codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ) + relativeBase,
                                    codeMap.getOrDefault( machineState + 1, ( long ) 0 ) * codeMap
                                            .getOrDefault( codeMap.getOrDefault( machineState + 2, ( long ) 0 ),
                                                    ( long ) 0 ) );
                    }
                }
                else if ( firstParamMode == 2 )
                {
                    switch ( secondParamMode )
                    {
                        case 1:
                            codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ) + relativeBase,
                                    codeMap.getOrDefault(
                                            codeMap.getOrDefault( machineState + 1, ( long ) 0 ) + relativeBase,
                                            ( long ) 0 ) * codeMap
                                            .getOrDefault( machineState + 2, ( long ) 0 ) );
                            break;

                        case 2:
                            codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ) + relativeBase,
                                    codeMap.getOrDefault(
                                            codeMap.getOrDefault( machineState + 1, ( long ) 0 ) + relativeBase,
                                            ( long ) 0 ) * codeMap
                                            .getOrDefault(
                                                    codeMap.getOrDefault( machineState + 2, ( long ) 0 ) + relativeBase,
                                                    ( long ) 0 ) );
                            break;

                        default:
                            codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ) + relativeBase,
                                    codeMap.getOrDefault(
                                            codeMap.getOrDefault( machineState + 1, ( long ) 0 ) + relativeBase,
                                            ( long ) 0 ) * codeMap
                                            .getOrDefault( codeMap.getOrDefault( machineState + 2, ( long ) 0 ),
                                                    ( long ) 0 ) );
                    }
                }
                else
                {
                    switch ( secondParamMode )
                    {
                        case 1:
                            codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ) + relativeBase,
                                    codeMap.getOrDefault( codeMap.getOrDefault( machineState + 1, ( long ) 0 ),
                                            ( long ) 0 ) * codeMap
                                            .getOrDefault( machineState + 2, ( long ) 0 ) );
                            break;

                        case 2:
                            codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ) + relativeBase,
                                    codeMap.getOrDefault( codeMap.getOrDefault( machineState + 1, ( long ) 0 ),
                                            ( long ) 0 ) * codeMap
                                            .getOrDefault(
                                                    codeMap.getOrDefault( machineState + 2, ( long ) 0 ) + relativeBase,
                                                    ( long ) 0 ) );
                            break;

                        default:
                            codeMap.put( codeMap.getOrDefault( machineState + 3, ( long ) 0 ) + relativeBase,
                                    codeMap.getOrDefault( codeMap.getOrDefault( machineState + 1, ( long ) 0 ),
                                            ( long ) 0 ) * codeMap
                                            .getOrDefault( codeMap.getOrDefault( machineState + 2, ( long ) 0 ),
                                                    ( long ) 0 ) );
                    }
                }
                machineState += 4;
            }
        }
    }


}
