fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
print(fruits)


####RANGE####
# for number in range (a,b):
#     print number

# For loop with Range 1 to 10
# (1, 11, 3) to step 3 every time
for number in range (1,11):
    print(number )

total = 0
for number in range(1, 101):
    total += number
print(total)



################Exercise-1 Average Height#################
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total_height = 0
student_number = 0
for student in student_heights:
    total_height += student
    student_number += 1

average = round(total_height / student_number)
print(average)

################Exercise-2 High Score#################
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

high_score = 0

for score in student_scores:
    if score > high_score:
        high_score = score

print(f"The highest score in the class is: {high_score}")


################Exercise-3 Adding Even Numbers#################
#Write your code below this row 👇
total = 0
for number in range(0, 101,2):
    # print(number)
    total += number
print(total)

################Exercise-4 FizzBuzz#################
#Write your code below this row 👇

for number in range(1, 101):
    if (number % 3 == 0) and (number % 5 == 0):
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)



