#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("welcome to the tip calculator!")
bill = float(input(" what is the total bill? $"))

tip = int(input("Home much tip would you like to give? 10,20,or 30? "))


People = int(input("How man people to slipt the bill??"))

tip_as_percentage = tip / 100
total_tip_amount = bill * tip_as_percentage
total_bill = bill + total_tip_amount

bill_per_person = total_bill / People

final_amount = "{:.2f}".format(bill_per_person)

print("each person should pay ${final_amount}")
print(final_amount)


