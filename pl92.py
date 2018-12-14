while True:
    try:
        decimal_num = int(raw_input( ), 2)
    except ValueError:
        print "Your input is not a binary number! Please try again."
    else:
        break
print decimal_num
