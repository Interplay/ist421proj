#!/usr/bin/env python3

import os
from random import randrange, uniform

irand = randrange(0, 11)
o = 0
i = 0

str = ''


if irand == 0:
	str="Item Ordered: Egyptian Cotten Sheets"
elif irand == 1:
	str="Item Ordered: LED Crystal Lamp"
elif irand == 2:
	str="Item Ordered: Ultrasonic Pest Repellent"
elif irand == 3:
	str="Item Ordered: Stainless Steel Kitchen Sink Strainer"
elif irand == 4:
	str="Item Ordered: Digital Cooking Meat Thermometer"
elif irand == 5:
	str="Item Ordered: Wooden Clothes Hangers"
elif irand == 6:
	str="Item Ordered: Natural Cow Hooves for Dogs"
elif irand == 7:
	str="Item Ordered: Sweet Almond Oil"
elif irand == 8:
	str="Item Ordered: WindTunnel Vacuum Cleaner"
elif irand == 9:
	str="Item Ordered: MAX Lithium Ion Chainsaw"
elif irand == 10:
	str="Item Ordered: Burner Cart Gas Grill"
elif irand == 11:
	str="Item Ordered: Noggenfrogger Elixir"

while os.path.exists("AprilOrder%s.txt" % i):
    i += 1
    o += 1

fh = open("AprilOrder%s.txt" % i, "w")
rs = ("\n"+"Order Number:%s is confirmed and on the way" %o+ "\n"+ str+"\n")
fh.writelines(rs)
fh.close()
