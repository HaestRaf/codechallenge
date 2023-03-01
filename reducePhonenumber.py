def reduce_phoneNumber(phoneNr):
    total = ""
    while phoneNr > 9:
        for number in range(0, len(str(phoneNr)), 2):
            if number+1 < len(str(phoneNr)):
                total += str(int(str(phoneNr)[number]) + int(str(phoneNr)[number+1]))
            else:
                total += str(int(str(phoneNr)[-1]))
        phoneNr = int(total)   
        total = ""
    return phoneNr


print(reduce_phoneNumber(4783926))


