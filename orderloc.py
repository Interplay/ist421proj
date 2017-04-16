#!/usr/bin/env python3

import os
from random import randrange, uniform

irand = randrange(0, 11)
dayCount = randrange(2,7)
ecoast = randrange(0,11)
o = 0
i = 0

fromCity=''
toCity=''

if irand == 0:
	fromCity="Portland"
elif irand == 1:
	fromCity="Spokane"
elif irand == 2:
	fromCity="Sacramento"
elif irand == 3:
	fromCity="Fresno"
elif irand == 4:
	fromCity="Oakland"
elif irand == 5:
	fromCity="San Bernardino"
elif irand == 6:
	fromCity="Los Angeles"
elif irand == 7:
	fromCity="San Diego"
elif irand == 8:
	fromCity="Chicago"
elif irand == 9:
	fromCity="El Paso"
elif irand == 10:
	fromCity="Seattle"
elif irand == 11:
	fromCity="Albuquerque"

if ecoast == 0:
	toCity="New York City"
elif ecoast == 1:
	toCity="Philadelphia"
elif ecoast == 2:
	toCity="Columbus"
elif ecoast == 3:
	toCity="Charlotte"
elif ecoast == 4:
	toCity="Chicago"
elif ecoast == 5:
	toCity="Detroit"
elif ecoast == 6:
	toCity="Baltimore"
elif ecoast == 7:
	toCity="Memphis"
elif ecoast == 8:
	toCity="Boston"
elif ecoast == 9:
	toCity="Louisville"
elif ecoast == 10:
	toCity="Raleigh"
elif ecoast == 11:
	toCity="Miami"



while os.path.exists("OrderLocation%s.txt" % i):
    i += 1
    o += 1

fh = open("OrderLocation%s.txt" % i, "w")
rs = ("\n"+"Order Number:%s has departed from" %o+" "+fromCity+" and will arrive at "+toCity+ " in "+str(dayCount)+" days."+"\n")
fh.writelines(rs)
fh.close()

