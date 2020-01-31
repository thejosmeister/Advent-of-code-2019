
public class Day4
{
    public static void main( String[] args )
    {
        int total = 0;
        boolean bool = true;
        for(int i = 246540; i < 787420; i++)
        {
            String j = Integer.toString( i );
            if( Integer.parseInt( j.substring(0,1) ) > Integer.parseInt( j.substring(1,2) )
                    || Integer.parseInt( j.substring(1,2) ) > Integer.parseInt( j.substring(2,3) )
                    || Integer.parseInt( j.substring(2,3) ) > Integer.parseInt( j.substring(3,4) )
                    || Integer.parseInt( j.substring(3,4) ) > Integer.parseInt( j.substring(4,5) )
                    || Integer.parseInt( j.substring(4,5) ) > Integer.parseInt( j.substring(5,6) ))
            {
                continue;
            }

            for( int k = 0; k<5; k++)
            {
                if( j.substring( k,k+1 ).equals( j.substring( k+1,k+2 ) ) )
                {
                    if(k == 0)
                    {
                        if(j.substring( 1, 2 ).equals( j.substring( 2, 3 ) ))
                        {
                            continue;
                        }
                    }
                    else if( k == 4 )
                    {
                        if( j.substring( 3,4 ).equals( j.substring( 4,5 ) ) )
                        {
                            continue;
                        }
                    }
                    else if( j.substring( k + 1, k + 2 ).equals( j.substring( k + 2, k + 3 ) ) || j.substring( k-1, k )
                            .equals( j.substring( k, k+1 ) ) )
                    {
                        continue;
                    }
                    bool = false;
                }
            }

            if(!bool)
            {
                total++;
                System.out.println(j);
            }

            bool = true;
        }
        System.out.println(total);
    }
}
