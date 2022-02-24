age =  int(input("Enter Your Age:"))
height =  int(input("Enter Your Height:"))

if age > 18:
    print('NESTED IF STATEMENT IS COMMING NOW')
    if height > 5:
        print('You are now eligible to participate in the party arrangement')
    else:
        print('You are not eligible to participate in the party arrangement')
else:
    print('NESTED IF STATEMENT IS NOT COMMING NOW')