digit =int(input())
#conver digit into string 
digit = str(digit)
#reverse the digit
digit = digit[::-1]
#convert the digit into integer
digit = int(digit)
#compare the digit with the older one
if digit == int(input()):
    print("true")
else:
    print("false")



