

import java.util.HashMap;

/**
 * @author josiah.filleul
 */
public class IntCodeMap<K,V> extends HashMap<K,V>
{

    public long getLong(long key)
    {
        if( !this.containsKey( key ) )
        {
            return  0;
        }

        return Long.parseLong( this.get( key ).toString() );
    }

}
