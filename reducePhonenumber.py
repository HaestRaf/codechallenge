def reduce_phoneNumber(x):
    total = ""
    while x > 9:
        for i in range(0, len(str(x)), 2):
            if i+1 < len(str(x)):
                total += str(int(str(x)[i]) + int(str(x)[i+1]))
            else:
                total += str(int(str(x)[-1]))
        x = int(total)   
        total = ""
    return x


print(reduce_phoneNumber(4783926))


