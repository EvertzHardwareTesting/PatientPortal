#!/usr/bin/python

import random
import string
import datetime
from datetime import timedelta

def GetRandomIndexFromList(list):
	return str(random.randint(1,len(list)-1))

def GetDaysAddToCurrentDateInDict(addDays):
        nextDt = datetime.datetime.now() + timedelta(days=int(addDays))
        Month=nextDt.strftime("%B")
        Year=nextDt.strftime("%Y")
        Day=int(nextDt.strftime("%d"))
        return {'Month': nextDt.strftime("%B"), 'Year': nextDt.strftime("%Y"), 'Day':int(nextDt.strftime("%d"))}

def GenerateRandomString(length):
        return ''.join(random.choice(string.lowercase) for i in range(int(length)))

def IsDateGreaterThanCurrentDate(strDtTm):
        strToDtTm=datetime.datetime.strptime(strDtTm, "%d %B %Y %I:%M %p")
        if datetime.datetime.now()<strToDtTm:
                return True
        else:
                return False
        
        
    
        
        
                
                
        
        
