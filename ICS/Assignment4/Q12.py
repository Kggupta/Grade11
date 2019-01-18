#Write code to show an application of reading, writing, and appending to a text file. Bonus: show use of formatted file rather than just text file!

f = open("pytext.txt","w+")
for i in range(10):
    f.write("This is line %d\r\n" % (i+1))
f.close()
f = open("pytext.txt","r")
filecontent = f.read()
print(filecontent)

f.close()
f = open("pytext.txt","a")
f.write("This is an appended line")
