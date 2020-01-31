

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Scanner;

/**
 * @author josiah.filleul
 */
public class Day8
{
    public static void main( String[] args )
    {
        String image = "";
        try
        {
            File imageFile = new File( "image.txt" );
            Scanner myReader = new Scanner( imageFile );
            while ( myReader.hasNextLine() )
            {
                image = myReader.nextLine();
            }
            myReader.close();
        }
        catch ( FileNotFoundException e )
        {
            System.out.println( "An error occurred." );
            e.printStackTrace();
        }

//        part1(image);

        part2( image );


    }

    public static void part1( String image )
    {
        System.out.println( image.length() );
        String interim;
        int interimNum;
        String out = "";
        int outNum = 25 * 6;
        for ( int i = 0; i < image.length(); i += ( 25 * 6 ) )
        {
            interimNum = 0;
            interim = image.substring( i, i + ( 25 * 6 ) );
            for ( int j = 0; j < interim.length(); j++ )
            {
                if ( interim.substring( j, j + 1 ).equals( "0" ) )
                {
                    interimNum++;
                }
            }

            if ( interimNum < outNum )
            {
                outNum = interimNum;
                out = interim;
            }
        }

        int noOfOnes = 0;
        int noOfTwos = 0;

        for ( int j = 0; j < out.length(); j++ )
        {
            if ( out.substring( j, j + 1 ).equals( "1" ) )
            {
                noOfOnes++;
            }

            if ( out.substring( j, j + 1 ).equals( "2" ) )
            {
                noOfTwos++;
            }
        }

        System.out.println( noOfOnes * noOfTwos );
    }

    public static void part2( String image )
    {
        String[] sb = new String[ 150 ];
        for(int x = 0; x < 150; x++)
        {
            sb[x] = " ";
        }

        int count = 0;
        for ( int i = 0; i < image.length(); i +=150 )
        {
            for ( int j = i; j < i+150; j++ )
            {
                if ( image.substring( j, j + 1 ).equals( "0" ) && !sb[ j%150 ].equals( "1" ) )
                {
                    sb[ j%150 ] = "0";
                }
                else if ( image.substring( j, j + 1 ).equals( "1" ) && !sb[ j%150 ].equals( "0" ) )
                {
                    sb[ j%150 ] = "1";
                }
                else if ( image.substring( j, j + 1 ).equals( "2" ) && !sb[ j%150 ].equals( "0" )
                        && image.substring( j, j + 1 ).equals( "2" ) && !sb[ j%150 ].equals( "1" ) )
                {
                    sb[ j%150 ] = "2";
                }

            }
            count++;
        }

        for ( int i = 0; i < 150; i++ )
        {
            if ( sb[i].equals( "0" ) )
            {
                sb[i]= " ";
            }
            else if ( sb[i].equals( "2" ) )
            {
                sb[i] = " ";
            }
            else if ( sb[i].equals( "1" ) )
            {
                sb[i]="H";
            }
        }

        for ( int n = 0; n < 150; n += 25 )
        {
            String out =
                    sb[ n ] + sb[ n + 1 ] + sb[ n + 2 ] + sb[ n + 3 ] + sb[ n + 4 ] + sb[ n + 5 ] + sb[ n + 6 ] + sb[ n
                            + 7 ] + sb[ n + 8 ] + sb[ n + 9 ] + sb[ n + 10 ] + sb[ n + 11 ] + sb[ n + 12 ] + sb[ n
                            + 13 ] + sb[ n + 14 ] + sb[ n + 15 ] + sb[ n + 16 ] + sb[ n + 17 ] + sb[ n + 18 ] + sb[ n
                            + 19 ] + sb[ n + 20 ] + sb[ n + 21 ] + sb[ n + 22 ] + sb[ n + 23 ] + sb[ n + 24 ];
            System.out.println( out );
        }

    }
}
