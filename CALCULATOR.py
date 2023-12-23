print('''
+ add
- subtract
* mutiply
/ divide
''')
P = int(input("enter the number:-1"))
Q = int(input("enter the number:-2"))
OPR = input("enter the OPR(+,-,*,/)")
if OPR =="+":
    print(P+Q)
elif OPR =="-":
    print(P-Q)
elif OPR == "*":
    print(P*Q)
elif OPR == "/":
    print( P/Q)
else:
    print("invalid choice")
