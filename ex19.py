#defines the function cheese_and_crackers with two arguments saved as two different variables
#prints the value of cheese_count that got passed with function call
#prints the value of boxes_of_crackers that got passed with function call
#prints a string
#prints a string with new line escape formating
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket. \n")


def myfunction(type, x, y):
    print(f"Hello so you're an: {type}")
    print(f"How many fingers do you have?: {x}")
    print(f"How many toes do you have?: {y} \n")




print("We can just give the function numbers directly:")
#calls the function cheese_and_crackers while giving the value 20 to cheese_count and 30 to boxes_of_crackers
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
#calls the function while passing the values of the two recently created variables and store them in the functionargvariables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
#calls the function with 10+20 and 5+6
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
#combines the two past function calls and use both variables and math in a function call
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print("-" * 5 + "MYFUNCTION CODE BELOW" + "-" * 5)


myfunction("goat", 10, 5)   #1 hardcode
myfunction("Hi"+"!!", 10 + 2, 5 - 1) #2 string+arithmetic math

input1 = input("What are you?: ") #3 user input
input2 = input("How many fingers?: ")
input3 = input("How many toes?: ")
myfunction(input1, input2, input3)
