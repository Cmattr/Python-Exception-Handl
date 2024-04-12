# Task 1: Start

try:
    original = int(input("please enter the number of servings the dish was originally intended for: "))
    
    servings = int(input("please enter the number of servings you wish to make: "))
except ValueError:
    print("please try again and enter an interger")

# Task 2: Quantity Calculation
def ratio(original, servings):
    try:
        adjustment = original / servings
    except Exception:
        print("an error has occured. please try again.")
   
   # Task 3: Serving Success
    finally: 
        print("Thank you for your input please enjoy your recipe.")
    return(adjustment)


new_recipe = ratio(original, servings)

print(f"the adjustment factor for your recipe is {new_recipe}")

