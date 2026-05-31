# 1. Email Generator

# Take the user's first name and last name as input and generate an email address.
first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")

email = first_name.lower() + "." + last_name.lower() + "@gmail.com"

print("Email:", email)


# 2. Username Creator

# Take a full name as input and create a username by:

# Converting to lowercase
# Replacing spaces with underscores


full_name = input("Enter Full Name: ")

username = full_name.lower().replace(" ", "_")

print("Username:", username)

# 3. Resume Headline Generator

# Take:

# Name
# Skill

name = input("Enter Name: ")
skill = input("Enter Skill: ")

print(name + " | Aspiring " + skill)

# 4. Word Counter

# Take a sentence from the user and print:

# Total number of characters
# Total number of words (Hint: use count(" ") + 1)

sentence = input("Enter a sentence: ")

characters = len(sentence)
words = sentence.count(" ") + 1

print("Characters:", characters)
print("Words:", words)

# 5. Password Strength Checker
# Take a password and print Also print the first and last character.


password = input("Enter Password: ")

print("Length:", len(password))
print("First Character:", password[0])
print("Last Character:", password[-1])


# 6. YouTube Title Formatter

# Take a title as input and:

# Remove extra spaces from start and end
# Convert it to Title Case


title = input("Enter Title: ")

formatted_title = title.strip().title()

print("Formatted Title:", formatted_title)


# 7. Shopping Bill Generator

# Take:

# Product Name
# Price


product = input("Enter Product Name: ")
price = int(input("Enter Price: "))

print("Product:", product)
print("Price: ₹" , price)

# 8 social media bio formatter

Name = input("Enter your full name: ")
Profession = input("Enteryour profession: ")

print("👤", Name)
print("💼", Profession)



# 9. Find a Word

# Take a sentence and print the position of the word "Python".

sentence = input("Enter your sentence")

position = sentence.find("python")
print("position", position)


# 10. Certificate Generator
# Take:

# Student Name
# Course Name
student_name = input("Enter Student Name: ")
course_name = input("Enter Course Name: ")

certificate = f"""
Certificate of Completion

This is to certify that {student_name}
has successfully completed the
{course_name} course.
"""

print(certificate)

