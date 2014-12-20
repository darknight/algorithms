using System;
using System.IO;
using System.Collections.Generic;

class Program
{
    static int Main(string[] args)
    {
        string line;
        int[] arr1 = new int[10];
        int[] arr2 = new int[10];
        StreamReader reader = new StreamReader(args[0]);
        while ((line = reader.ReadLine()) != null)
        {
            //Console.WriteLine(line);
            for(int i = 0; i < 10; i++)
            {
                arr1[i] = arr2[i] = 0;
            }
            for(int j = 0; j < line.Length; j++)
            {
                //Console.WriteLine("{0}", int.Parse(line[j].ToString()));
                int x = int.Parse(line[j].ToString());
                arr1[j] = x;
                arr2[x] += 1;
            }
            bool self_desc = true;
            for(int i = 0; i < 10; i++)
            {
                if(arr1[i] != arr2[i])
                {
                    self_desc = false;
                    break;
                }
            }
            if(self_desc)
            {
                Console.WriteLine("1");
	    }
            else
            {
                Console.WriteLine("0");
            }
        }
        return 0;
    }
}
