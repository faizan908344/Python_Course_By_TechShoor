#(1) ARITHMETIC OPERATORS
print("=================================================================================")
print("ARITHMATIC OPERATIONS")
print("=================================================================================")
number1 = 25
number2 = 5
print("THE FIRST NUMBER IS: ", number1)
print("THE SECOND NUMBER IS: ", number2)
print("THE ADDITION OF", number1 ," AND ", number2, "IS:", (number1+number2))
print("THE SUBTRACTION OF", number1 ," AND ", number2, "IS:", (number1-number2))
print("THE MULTIPLICATION OF", number1 ," AND ", number2, "IS:", (number1*number2))
print("THE DIVISION OF", number1 ," AND ", number2, "IS:", (number1/number2))
print("THE REMAINDER DIVISION OF", number1 ," AND ", number2, "IS:", (number1%number2))
print("THE POWER OF", number1 ," AND ", number2, "IS:", (number1**number2))
print("THE MUPLTIPLES OF", number1 ," AND ", number2, "IS:", (number1//number2))
print("=================================================================================")

#(2) ASSIGNMENT OPERETORS
print("=================================================================================")
print("ASSIGNMENT OPERATIONS")
print("=================================================================================")
number3 = 99
number4 = 12
print("THE THIRD NUMBER IS: ", number3)
print("THE FOURTH NUMBER IS: ", number4)
number3 += number4
print("THE INCREMENTED VALUE OF NUMBER3 WHICH WAS 99 IS NOW: ", number3)
number3 -= number4
print("THE DECREMENTED VALUE OF NUMBER3 WHICH WAS 111 IS NOW: ", number3)
number3 *= number4
print("THE INCREMENTED VALUE OF NUMBER3 WHICH WAS 99 IS NOW: ", number3)
number3 /= number4
print("THE NEW VALUE OF NUMBER3 WHICH WAS 1188 IS: ", number3)
number3 %= number4
print("THE INCREMENTED VALUE OF NUMBER3 WHICH WAS 99 IS: ", number3)
print("=================================================================================")

#(3) COMPARASION OPERATORS
print("=================================================================================")
print("COMPARISON OPERATIONS")
print("=================================================================================")
number5 = 101
number6 = 100
print("THE FIFTH NUMBER IS: ", number5)
print("THE SIXTH NUMBER IS: ", number6)
print("IS", number5 ," LESSER THEN ", number6, ":", (number5<number6))
print("IS", number5 ," GREATER THEN ", number6, ":", (number5>number6))
print("IS", number5 ," EQUAL TO ", number6, ":", (number5==number6))
print("IS", number5 ," LESSER THEN EQUAL TO ", number6, ":", (number5<=number6))
print("IS", number5 ," GREATER THEN EQUAL TO ", number6, ":", (number5>=number6))
print("=================================================================================")

#(4) LOGICAL OPERATIONS
print("=================================================================================")
print("LOGICAL OPERATIONS")
print("=================================================================================")
number7 = 15
number8 = 14
print("THE SEVENTH NUMBER IS: ", number7)
print("THE EIGHTH NUMBER IS: ", number8)
print(number7 and number8)
print(number7 or number8)
print("=================================================================================")

#(5) IDENTITY OPERATIONS
print("=================================================================================")
print("IDENTITY OPERATIONS")
print("=================================================================================")
name1 = "MUHAMMAD FAIZAN"
name2 = "MASJID UL AQSA"
print("THE FIRST NAME IS: ", name1)
print("THE SECOND NAME IS: ", name2)
print(name1 is name2) # HERE IN THIS STATEMENT THE SECOND NAME WAS CHECKED THAT IS THE SECOND NAME IS SIMILAR TO THE FIRST ONE
print(name1 is not name2) #THE SAME PROCESS WILL BE FOLLOWED HERE IF THE STATEMENT IS TRUE SO TRUE WILL BE PRINTED OTHER WISE FALSE
print("=================================================================================")

#(6) MEMBERSHIP OPERATIONS
print("=================================================================================")
print("MEMBERSHIP OPERATIONS")
print("=================================================================================")
list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(5 in list)
print(19 in list)
print(55 in list)
print(91 in list)
print(5 not in list)
print(19 not in list)
print(55 not in list)
print(91 not in list)
print("=================================================================================")

#(7) BITWISE OPERATIONS
print("=================================================================================")
print("BITWISE OPERATIONS")
print("=================================================================================")
print(0 | 2)
print(1 & 1)
print("=================================================================================")
