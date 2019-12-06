eligible_passwords = 0
for i in range(240298,784956):
#i = 123444
    digits = map(int,str(i))
    previous_digits= [[],[],[]]
    previous_digit = 0
    incrementing_digits_count = 0
    double_digits_count = 0
    for digit in digits:
        found = False
        if digit > previous_digit:
            previous_digit = digit
            incrementing_digits_count += 1
        elif digit == previous_digit:
            previous_digit = digit
            for j in previous_digits:
                if digit in j:
                    j.append(digit)
                    found = True
            if not found:
                previous_digits[previous_digits.index([])].append(digit)
            incrementing_digits_count += 1
            double_digits_count += 1
        else:
            break
    adjacents_count = 3 - len([i for i, e in enumerate(previous_digits) if e == []])
    at_least_one_couple = False
    for some in range(adjacents_count):
        if len(previous_digits[some]) == 1: 
            at_least_one_couple = True
    #if adjacents_count == 1:
     #   number_of_digits = len(previous_digits[0]) +1
      #  if number_of_digits > 2:
       #     continue
        
    if incrementing_digits_count == 6 and at_least_one_couple:
        eligible_passwords += 1
print(eligible_passwords)
