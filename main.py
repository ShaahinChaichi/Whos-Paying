import random


# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

last_person = len(names)

random_person = random.randint(0, last_person)

print(f"{names[random_person]} is going to buy the meal today")



