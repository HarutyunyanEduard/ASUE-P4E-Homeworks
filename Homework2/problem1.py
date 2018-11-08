while True:
    try:
        num = int(input("Please inpute a number\n"))
        x = num % 2
        if x > 0:
          print("Odd number")
        else:
          print("Even number")
    except ValueError:
        print("Its not a number(\n")
    else:
        break
 

