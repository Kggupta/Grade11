#Make up your own question on a topic not covered in the above questions.

cost = 0
coninustate = ""
people = 0
age = int

def calccost():
   print("There are {} people/person in your party".format(people))
   print("Cost is ${0:.2f}".format(cost))
   print("Total cost with tax is ${0:.2f}".format(cost*1.13))
   exit()

while True:
   age = int(input("Enter your age to know how much your movie ticket costs:"))
   print("Accepted input...")
   break

if age in range(0,6):
   print("This person gets a free movie ticket!")
   people+=1
elif age in range(6,13):
   print("This person's ticket is 12$")
   cost += 12
   print("Cost is: ${0:.2f}".format(cost))
   people+=1
elif age in range(13,19):
   print("This persons ticket is $15")
   cost += 15
   print("Cost is: ${0:.2f}".format(cost))
   people+=1
elif age >= 19:
   print("This persons ticket in $20")
   cost += 20
   print("Cost is ${0:.2f}".format(cost))
   people+=1

calccost()
