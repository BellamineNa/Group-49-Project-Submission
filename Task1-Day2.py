number_of_books = int(input("Enter the number of books you have purchased this month: "))
message = ""

if number_of_books < 0:
    message = "Please enter a positive number."
              
else:
    message = "You have been awarded "

    if number_of_books >= 0 and number_of_books <= 0:
        message += "0 "
    elif number_of_books >= 1 and number_of_books <= 1:
        message += "6 "
    elif number_of_books >= 2 and number_of_books <= 2:
        message += "16 "
    elif number_of_books >= 3 and number_of_books <= 3:
        message += "32 "
    elif number_of_books >= 4:
        message += "60 "

    message += "points."

print(message)