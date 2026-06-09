# variables

name = "jobhn" # name stores john 
a = 25 # a stores age
price = 89 # price stores 89

print(name,a,price)


# Why Variables Are Important

# Variables help you:

# Store data
# Reuse data
# Update data
# Make programs dynamic and flexible
# Example of Updating a Variable
score = 10
score = score + 5

print(score)

# 1

x = 10
y = x
x = 20

print(y)


#2

a, b, c = 1, 2, 3

print(a)
print(b)
print(c)

#3

x = 5
y = 10
x, y = y, x
print(x, y)

bramhdev, vaishnavi, rupali = 1, 2, 3
print(bramhdev)
print(vaishnavi)
print(rupali)

#4 Chained Assignment

a = b = c = 100

b = 50

print(a)
print(b)
print(c)

# type chnage

data = 100
data = "python"

print(type(data))


# 6. Local Scope


x = 10

def show():
    x = 20
    print(x)

show()
print(x)

# varibales advance realworld questions

# 1 In an e-commerce website, which variables would you need to calculate the final price after applying discounts, taxes, and shipping charges?

product_amount = int(input("Enter the price ="))
discount = int(input("Enter the discount amount = "))
taxes = int(input("Enter the taxes amount = "))
shipping = int(input("Enter the shipping amount = "))

final_price = " Final Price =", product_amount - discount + taxes + shipping

print(final_price)

# 2 In a banking application, how would you use variables to track a customer's account balance after multiple deposits and withdrawals?
balance = 1000  # Initial balance

# Deposit money
balance = balance + 500
# Withdraw money
balance = balance - 200

# Deposit again
balance = balance + 500
print(balance)


#3 In a food delivery app, what variables would be required to calculate the estimated delivery time?
preparation_time = 20
distance = 5
delivery_speed = 30  # km/h
traffic_delay = 10

delivery_time = (distance / delivery_speed) * 60  # Convert hours to minutes

estimated_delivery_time = preparation_time + delivery_time + traffic_delay

print(estimated_delivery_time)