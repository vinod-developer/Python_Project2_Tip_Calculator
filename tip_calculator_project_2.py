print("Welcome to the Tip Calculator")

bill_as_float = float(input("Please enter the bill?$"))
tip_percentage_as_int = int(input("Please enter the tip %"))
total_amt_with_tip = bill_as_float * (1 + tip_percentage_as_int/100)
no_of_ppl_as_int = int(input("Please entet no. of ppl"))
amt_to_split_per_person = total_amt_with_tip/no_of_ppl_as_int
#format_to_two_decimals = round(amt_to_split_per_person,2)
# When input is integer and want to print output in 2 decimal float, use below
total_amt_after_rounded_off = "{:.2f}".format(amt_to_split_per_person)
print(f"Each person has to pay {total_amt_after_rounded_off}")