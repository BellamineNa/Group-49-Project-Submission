#write a program that asks the user to enter the square feet of wall space to bepainted and the price of paint per gallon
#115 square feet = 1 gallon + 8 hours of labor(labor is $20 per hour)
determined_wall_space= 115
estimated_hours_of_labor= 8
estimated_number_of_galloon= 1
labor_charges_per_hour= 20
square_feet_of_wall_space_to_painted= int(input("enter number of squre feet  of wall to be painted"))
price_of_gallons_required=int(input("enter price of pain per gallon"))

number_of_gallon_required = square_feet_of_wall_space_to_painted/determined_wall_space
print("number of gallons required:", number_of_gallon_required)

hours_of_labor= square_feet_of_wall_space_to_painted*estimated_hours_of_labor/determined_wall_space
print("hours of labor required:",hours_of_labor)

cost_of_paint=price_of_gallons_required*estimated_number_of_galloon
print("cost of paint:", cost_of_paint)

labor_charges=estimated_hours_of_labor*labor_charges_per_hour 
print("labor charges:",labor_charges)

total_cost_of_paint_job=labor_charges + cost_of_paint
print("total cost of paint job is $:",total_cost_of_paint_job)