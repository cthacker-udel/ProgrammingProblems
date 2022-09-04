using System;
using System.Collections.Generic;
using System.Linq;

public static class Kata
{
    public static IEnumerable<IEnumerable<object>> GroupWhile(
        this IEnumerable<object> coll,
        Func<object, bool> pred
    )
    {
        List<object> listArray = new List<object>();
        List<List<object>> listTwoDArray = new List<List<object>>();
        foreach (object eachObj in coll)
        {
            if (pred(eachObj))
            {
                listArray.Add(eachObj);
            }
            else
            {
                if (listArray.Count > 0)
                {
                    listTwoDArray.Add(listArray);
                    listArray = new List<object>();
                    listArray.Add(eachObj);
                    if (!pred(eachObj))
                    {
                        listTwoDArray.Add(listArray);
                        listArray = new List<object>();
                    }
                }
                else
                {
                    listArray.Add(eachObj);
                    listTwoDArray.Add(listArray);
                    listArray = new List<object>();
                }
            }
        }
        if (listArray.Count > 0)
        {
            listTwoDArray.Add(listArray);
        }
        return listTwoDArray;
    }
}
