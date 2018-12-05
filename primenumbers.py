PrimeNumberList = []

def CalculateIfPrime(UserValue):
   if UserValue > 1:
       # check for factors
       for iteration in range(2, UserValue):
           if (UserValue % iteration) == 0:
               print("That is NOT prime")
               break
       else:
           print("That IS prime")
           PrimeNumberList.append(UserValue)

while True:
   UserInputNumber = int(input("Enter a positive integer value: "))
   CalculateIfPrime(UserInputNumber)
