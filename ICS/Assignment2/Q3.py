#Write a program to verify that a person has entered a valid percentage mark. Ask for the mark, then output “Thank you” if it is between 0 and 100 or “Invalid mark” if it is outside that range.

mark= int(input("What is your mark?"))
if mark>=0 and mark<=100:
    print("Thank You")
else:
    print("Invalid Mark")
