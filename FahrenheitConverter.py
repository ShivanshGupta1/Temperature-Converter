#!/usr/bin/env python
# coding: utf-8

# In[12]:


celciusList = [element.strip() for element in open("temps.txt","r")]#This is creating the list with all the elements required using list comprehension. It uses the ".strip" method which clears out all the outer spaces
convertedList = []#This is the list needed later
convertedFile = open("fTemps.txt","a")#This is where we add all the new stuff
for temp in celciusList:#This is running the for loop:
    temp = int(temp)#It converts it into a int for appending
    temp = (temp * 9/5) + 32#It converts into Fahrenheit
    convertedList.append(temp)#Here it appends
for convertedTemp in convertedList::#This is running the for loop to add in the file
    convertedTemp = str(convertedTemp)#This is converting into a string
    convertedFile.write(convertedTemp+"\n") #This is appending in the file in new lines
convertedFile.close()#This is closing

