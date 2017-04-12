#!/usr/bin/env python3

import os

i = 0
while os.path.exists("sample%s.xml" % i):
    i += 1

fh = open("sample%s.xml" % i, "w")
rs = "test post plz work"
fh.writelines(rs)
fh.close()
