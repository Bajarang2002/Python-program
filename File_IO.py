# Open And close file
# Read file

f = open("Demo.txt", "r")
data = f.read()
print(data)

# Write File

f = open("Sample.text","w")
data1 = f.write("Python is the high level programming language")
print(data1)

# Append File

f = open("Demo.txt","a")
data2 =f.write(" I love programming")
print(data2)
f.close()

# Using Differnt mode
# r+
f = open("Sample.text","r+")
data3 =f.write("Abcdef")
print(data3)
data4 =f.read()
print(data4)
data5 =f.write("Javala")
print(data5)
f.write("C++ language")
f.read()


#w+
f = open("Sample.text","w+")
data3 =f.write("Abcdef")
print(data3)
f.read()
f.write("Python")

# a+
f = open("Sample.text","a+")
f.write(" High level Language")
f.read()



# By using with keyword

with open("program.txt","r") as f:
    data = f.read()
    print(data)



with open("program.txt","w") as f:
    data = f.write(" . Java is compiled time language ")
    print(data)


with open("program.txt","a") as f:
    data = f.write(" . Java is high level language")
    print(data)


# Deleting File

import os
os.remove("Sample.text")

#  Create a new file "prastice.text" using python Add the following data in it 
''' Hi everyone 
 we are learning file I/OS
 using java 
 I like programming in java '''

with open("pratice.txt","w") as f:
    data = f.write("""Hi everyone 
 we are learning file I/OS
 using java 
 I like programming in java""")
    print(data)



# Wap to replace all occurance of "java" with "python" in above file

with open("pratice.txt","r") as f:
    data = f.read()
new_data = data.replace("java","Python")
print(new_data)


#  Search if the word "learning" exists in the file or not

word ="xlearning"
with open("pratice.txt","r") as f:
    data = f.read()
    
    if word in data:
        print("Word learning is found")
    else:
        print("Word not found")



    word = "learning"
    with open("pratice.txt","r") as f:
        data = f.read()

    if data.find(word)!= -1:
        print("Word found")
    else:
        print("Word not found")


# WAP to find which line of the file does the word "learning" occur first print -1 word not found

def check_line():
    data = True
    line_no = 1
    word = "learning"
    with open("pratice.txt","r") as f:
        
        while data:
            data = f.readline()
            if (word in data):
                print(line_no)
                return
            line_no+=1
    return -1
check_line()

# from a file containing numbers seperated by comma, print the count of even numbers 
count=0
with open("sample.txt", "r") as f:
    data = f.read()

    data1 = data.split()
    print(data1)
    for val in range(0,len(data1)):
        if val %2==0:
            count+=1
print(count)          
            



        
        











