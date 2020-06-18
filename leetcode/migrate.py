import re
import os

NAME = re.compile("(p\d{4})-.+\.py")
PRINT = re.compile("print ")


def rename_and_convert():
    filelist = os.listdir(".")
    for pyname in filelist:
        res = NAME.search(pyname)
        if res is None:
            continue
        new_text = ['#!/usr/bin/env python3\n', '\n']
        with open(pyname, 'r') as f:
            text = f.readlines()
            for line in text:
                is_print = PRINT.search(line)
                if is_print is None:
                    new_text.append(line)
                else:
                    new_line = re.sub(PRINT, "print(", line)[:-1] + ")\n"
                    new_text.append(new_line)
        with open(pyname, 'w') as fw:
            fw.writelines(new_text)


if __name__ == '__main__':
    rename_and_convert()
