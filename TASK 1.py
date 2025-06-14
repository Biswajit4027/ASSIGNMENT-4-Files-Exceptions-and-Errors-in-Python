'''
Task 1: Read a File and Handle Errors
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
'''

try:
   file=open('sample.txt','r')
   file1=file.readlines()
   print("Reading File content.......\n")
   c=1
   for i in file1:
       print(f"Line{c}: ", i)
       c+=1
   file.close()
except FileNotFoundError:
       print("ERROR: The file 'sample.txt' was not found")


