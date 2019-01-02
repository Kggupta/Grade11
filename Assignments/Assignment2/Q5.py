#Write an efficient program (based on your answer to #8 above) that will ask for the price of someone’s purchase and tell them how much they can save.
#If it is under $25, there is no savings, if it is between $25 and $50, there is 10% savings, between $50 and $75 a 20% savings, between $75 and $100 a 30% savings and over $100 a 40% savings.
#Calculate and display their final cost after the savings (don’t worry about taxes for this program)

price = float(input("Enter the input of the price of your product:"))

if price <=0:
   print("Invalid input! Go buy something and come back!")
elif price < 25:
   print("There is no savings.")
elif price >= 25 and price < 50:
   print("There is a 10% savings. You saved ${0:.2f}".format(price*0.1))
   print("Your final charge is: ${0:.2f}".format(price-(price*0.1)))
elif price >=50 and price < 75:
   print("There is a 20% savings. You saved ${0:.2f}".format(price*0.2))
   print("Your final charge is: ${0:.2f}".format(price - (price * 0.2)))
elif price >= 75 and price < 100:
   print("There is a 30% savings. You saved ${0:.2f}".format(price*0.3))
   print("Your final charge is: ${0:.2f}".format(price - (price * 0.3)))
elif price >= 100:
   print("Wow! There is a 40% saving. You saved ${0:.2f}".format(price*0.4))
   print("Your final charge is: ${0:.2f}".format(price - (price * 0.4)))
