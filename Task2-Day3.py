fats = int(input("How many grams of fats have you consumed today? "))
carbs = int(input("How many grams of carbohydrates have you consumed today? "))
calories_from_fats = fats * 9
calories_from_carbs = carbs * 4
total_caloric_intake = calories_from_fats + calories_from_carbs
print("Your caloric intake from fats is ", calories_from_fats)
print("Your caloric intake from carbohydrates is ", calories_from_carbs)
print("Your total caloric intake is " , total_caloric_intake)