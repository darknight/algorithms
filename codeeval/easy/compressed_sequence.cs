using System;
using System.IO;
using System.Collections.Generic;

class MainClass
{
    public static int Main (string[] args)
    {
        string line;
        StreamReader reader = new StreamReader (args [0]);
        while ((line = reader.ReadLine ()) != null)
        {
            string[] nums = line.Split (new Char[] {' '});
            if (nums.Length == 1) 
            {
                Console.WriteLine ("1 {0}", nums [0]);
                continue;
            }
            List<string> listArr = new List<string> ();
            int current_times = 1;
            string current_num = nums [0];
            for (int i = 1; i < nums.Length; i++)
            {
                if (nums [i] != current_num)
                {
                    listArr.Add (String.Format ("{0} {1}", current_times, current_num));
                    current_num = nums [i];
                    current_times = 1;
                }
                else
                {
                    current_times += 1;
                }
            }
	    listArr.Add (String.Format ("{0} {1}", current_times, current_num));
            string[] strArr = listArr.ToArray ();
            Console.WriteLine (String.Join (" ", strArr));
        }
        return 0;
    }
}
