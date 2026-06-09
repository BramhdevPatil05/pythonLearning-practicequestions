#string #list # tuple practise 

# Store the name Rahul Sharma in a variable called customer_name

customer_name ="rahul"

print(customer_name)

# How many characters are in "Pune"?

city = "pune"

print(len(city))

# Check whether "discount" appears in the message "Festival discount available today".
message = "Festival discount available today"

print("discount" in message)

# Convert "invoice paid" to uppercase.

word = "invoice paid"

word = word.upper()

print(word)

# From "Rahul Sharma", extract the first name.

name = "Rahul Sharma"

first_name = name.split()[0]
print(first_name)

# Replace "pending" with "paid" in "Order status: pending".

word = "pending"

word = word.replace("pending", "paid")

print(word)





#list


# Create a list with "milk", "bread", and "eggs"


grocery = ["milk", "bread", "eggs"]

print(grocery)

# Add "butter" to the shopping cart.
grocery.append("butter")

print(grocery)

# Remove "bread" from the cart.

grocery.remove("bread")

print(grocery)
# Print the second item in [10, 20, 30, 40].

numbers = [10, 20, 30, 40]

print(numbers[1])

# Given item prices [120, 80, 250, 50], find the total.

grocery_prices = [120, 80, 250, 50]

grocery_prices = sum(grocery_prices)
print(grocery_prices)

# Sort [78, 92, 85, 60] in ascending order.

num =[78, 92, 85, 60] 
num.sort()
print(num)

# How many times does "apple" appear in ["apple", "banana", "apple", "mango", "apple"]?

str = ["apple", "banana", "apple", "mango", "apple"]

count = str.count("apple")

print(count)



# tuple

# Q14. Store fixed GPS coordinates

# Question

# Store latitude 18.5204 and longitude 73.8567 in a tuple.


gps_coordinates = (18.5204, 73.8567)

print(gps_coordinates)




# Q15. Unpack tuple values

# Question

# Extract latitude and longitude into separate variables.



gps_coordinates = (18.5204, 73.8567)

latitude, longitude = gps_coordinates

print("Latitude:", latitude)
print("Longitude:", longitude)



# Q16. Access tuple elements

# Question

# Print the first value of (101, "Rahul", "Pune").


data = (101, "Rahul", "Pune")

print(data[0])



# Q17. Try to modify a tuple

# What happens here?

# Python raises a TypeError because tuples are immutable (cannot be changed after creation).


data = (101, "Rahul", "Pune")
data[0] = 102


# Q18. Count and find index

# Question

# For (1, 2, 2, 3, 2):

# Count how many times 2 appears.

# Find the index of the first 2.

numbers = (1, 2, 2, 3, 2)

print(numbers.count(2))
print(numbers.index(2))

