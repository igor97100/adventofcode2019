eligible_passwords = 0
for i in range(240298,784956):
    digits = map(int,str(i))
    previous_digit = 0 
    incrementing_digits_count = 0
    double_digits_count = 0
    for digit in digits:
        if digit > previous_digit:
            previous_digit = digit
            incrementing_digits_count += 1
        elif digit == previous_digit:
            previous_digit = digit
            incrementing_digits_count += 1
            double_digits_count += 1
        else:
            break
    if incrementing_digits_count == 6 and double_digits_count > 0:
        eligible_passwords += 1
print(eligible_passwords)
