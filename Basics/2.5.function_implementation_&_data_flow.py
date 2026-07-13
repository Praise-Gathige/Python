# Standard Quest: The Tip Calculator
def calculate_tip(bill_amount, tip_percentage):
    tip_total = bill_amount * tip_percentage
    return tip_total

my_tip = calculate_tip(50, 0.20)

print(my_tip)



# Boss Challenge: The Temperature Converter
celsius = 0

def convert_f_to_c(farenheit):
    celsius = (farenheit - 32) * 5/9
    return celsius

final_temp = convert_f_to_c(100)

print(final_temp)