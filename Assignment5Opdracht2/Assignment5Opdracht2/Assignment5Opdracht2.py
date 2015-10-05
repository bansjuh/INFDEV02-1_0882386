#-----------------------------------------------------------------------------------------------------
#
# Created by:           Julian Mansveld
# Time Created:         30/10/2015
# Class:                INV1B
# Student Number:       0882386
#
#------------------------------------------------------------------------------------------------------

import re

while True:
    p = raw_input ("Enter a new password: \n")
    pLength = len(p)
    pStr = 0
    if 4 <= pLength:
        break
    print "This password must contain 4 or more characters!\n"

if pLength >= 15:
    pStr = pStr + 3
elif 10 <= pLength < 15:
    pStr = pStr + 2
elif pLength < 10:
    pStr = pStr + 1

if re.search(r'[a-z]', p):
    pStr = pStr + 2
else:
    pStr = pStr + 0

if re.search(r'[A-Z]', p):
    pStr = pStr +2
else:
    pStr = pStr + 0

if re.search(r'[0-9]', p):
    pStr = pStr + 3
else:
    pStr = pStr + 0

if re.search(r'[^a-zA-Z0-9_]', p):
    pStr = pStr + 4
else:
    pStr = pStr + 0

if pStr <= 6:
    print " You're password is weak \n."
elif 7 <= pStr < 10:
    print " You're password is medium \n."
elif pStr >= 11:
    print "Great job,  you're password is strong \n."

print " Thanks for submitting your password!"