

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class testing
{
    public static void main( String[] args )
    {
        int[][] test = new int[3][3];
        System.out.println( Arrays.toString(test[0]) );

        Set<String> set = new HashSet<String>(  );
        set.add( "a" );
        set.add( "b" );

        List<String> list = new ArrayList<String>( set );
        System.out.println(Arrays.toString( list.toArray() ) );


    }
}
