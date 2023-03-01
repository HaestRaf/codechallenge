def reduce_phoneNumber(phoneNr):
    total = ""
    while phoneNr > 9:
        for number in range(0, len(str(phoneNr)), 2):
            if number+1 < len(str(phoneNr)):
                phone_number = str(phoneNr)
                digit_1 = int(phone_number[number])
                digit_2 = int(phone_number[number+1])
                digit_sum = digit_1 + digit_2
                total += str(digit_sum)
            else:
                phone_number = str(phoneNr)
                final_digit = int(phone_number[-1])
                total += str(final_digit)
        phoneNr = int(total)   
        total = ""
    return phoneNr


print(reduce_phoneNumber(4783926))
