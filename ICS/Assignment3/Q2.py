#Write a program that reads words entered one at a time and counts how many words the user has entered before you give a signal word such as "quit" or “exit” to stop the loop.
#Remember to output the total number of words after the loop has finished.

#if you put more than one word in a line it will not count them. For this, we would need to count the number of spaces as well as entered values
wordcount = 0
wordinput = ""
while True:
    wordinput = input("Input a word. input quit or exit to end the loop: ")
    wordcount += 1
    if wordinput == "quit" or wordinput == "exit":
        break
wordcount -=1
print("There are {} words in all the words you inputted".format(wordcount))
