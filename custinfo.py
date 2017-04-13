#!/usr/bin/env python3

import os
from random import randrange, uniform

irand = randrange(0, 20)
custspend = randrange(100,999)
o = 0
i = 0

name = ''

if irand == 0:
	name ="Guy Rivera"
elif irand == 1:
	name="Customer Name: Harold Gross"
elif irand == 2:
	name="Customer Name: Ellen Strokes"
elif irand == 3:
	name="Customer Name: Aubrey Rowe"
elif irand == 4:
	name="Customer Name: Harvey Fletcher"
elif irand == 5:
	name="Customer Name: Angie Gibbs"
elif irand == 6:
	name="Customer Name: Howie Andersen"
elif irand == 7:
	name="Customer Name: Tom Mato"
elif irand == 8:
	name="Customer Name: Van Nunez"
elif irand == 9:
	name="Customer Name: Lola Anderson"
elif irand == 10:
	name="Customer Name: Al Coholic"
elif irand == 11:
	name="Customer Name: Ollie Tabooger"
elif irand == 12:
	name="Customer Name: Anita Braig"
elif irand == 13:
	name="Customer Name: Ayma Dommy"
elif irand == 14:
	name="Customer Name: Casey Deeya"
elif irand == 15:
	name="Customer Name: Chi Spurger"
elif irand == 16:
	name="Customer Name: Duncan Disorderly"
elif irand == 17:
	name="Customer Name: Ellis Dee"
elif irand == 18:
	name="Customer Name: Liz Onnia"
elif irand == 19:
	name="Customer Name: Brandon Iyon"
elif irand == 20:
	name="Customer Name: Donnie Buie"

while os.path.exists("CustOrder%s.txt" % i):
    i += 1
    o += 1

fh = open("CustOrder%s.txt" % i, "w")
rs = ("\n"+name+"has spent a total of $"+ str(custspend) +" on Order Number: %s" %o+ "\n")
fh.writelines(rs)
fh.close()
