using System;
using System.IO;
using System.Text;
using System.Collections.Generic;

class MainClass
{
    public static int Main (string[] args)
    {
        string line;
        StreamReader reader = new StreamReader(args[0]);
        while((line = reader.ReadLine()) != null)
        {
            if(line.Length < 1)
                continue;
            StringBuilder sb = new StringBuilder();
            char current = line[0];
            for(int i = 1; i < line.Length; i++)
            {
                if(line[i] != current)
                {
                    sb.Append(current);
                    current = line[i];
                }
            }
            sb.Append(current);
            if(current != line[line.Length - 1])
                sb.Append(line[line.Length - 1]);
            Console.WriteLine(sb.ToString());
        }
        return 0;
    }
}
