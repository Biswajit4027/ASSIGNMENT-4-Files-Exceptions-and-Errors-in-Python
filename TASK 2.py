'''
Task 2: Write and Append Data to a File

Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.

'''

file=open('output.txt','w')
file1=input(f"Enter text to write to file: ")
file.write(file1)
print("Data successfully written to output.txt")
file.close()

file=open('output.txt','a')
file1=input("Enter additional text to append: ")
file.write('\n')
file.write(file1)
print("Data successfully appended \n")
file.close()
print("Final content of the file 'output.txt' ")
print("----------------------------------------------\n")
file=open('output.txt','r')
file1=file.readlines()
for i in file1:
    print(i)
file.close()
