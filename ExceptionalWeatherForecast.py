while True:
    try:
        temp = int(input("enter a temperature in fahrenheit: "))

        if temp == 0:
            print("goodnbye")
        break
    except ValueError:
        print("invalid input!")

def convert (temp):
    try:
        temp = ((temp) - 32) * 0 / 9
    except Exception:
        print("conversion Failed")
    finally:
        print("Thank you for using the weather forcast application")
    return temp

celsius = convert(temp)

print(f"your temperature converted to celsius is: {celsius} ")