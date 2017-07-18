import os
import person
from human import woman

def dumpTxtFile(fn):
	with open(fn, "r") as f:
		for line in f:
			print line

dumpTxtFile("test.txt")

a = person.shirley()

a.introduce()
