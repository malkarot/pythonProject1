x = int(input("malkush "))
if x > 9999 or x < 1000:
    print("The number you arced is incorrect\n")
else:
    a = int(x//1000)
    b = int((x//100) % 10)
    c = int((x//10) % 10)
    d = int(x % 10)
    s = int(a+b+c+d)
    z = a+10*b+100*c+1000*d
    print("The number you arced is:", x)
    print("Sum of digits the number you have arc is:", s)
    print("The number in reverse order is:", z)

    if a == d and c == b:
        print("The number you arced is polindrom")
    else:
        print("The number you arced is not polindrom")
