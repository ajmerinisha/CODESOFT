def calculator():
    print("Welcome to Simple Calculator\n")
    
    try:
    
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        
        print("\nSelect operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        
        choice = input("Enter choice (1/2/3/4): ")
        
    
        print("\n" + "-"*50)
        print(f"{'Input (num1, num2)':<20} | {'Operation':<15} | {'Result'}")
        print("-"*50)

        
        if choice == '1':
            result = num1 + num2
            print(f"{f'{num1}, {num2}':<20} | {'Addition':<15} | {result}")
        
        elif choice == '2':
            result = num1 - num2
            print(f"{f'{num1}, {num2}':<20} | {'Subtraction':<15} | {result}")
        
        elif choice == '3':
            result = num1 * num2
            print(f"{f'{num1}, {num2}':<20} | {'Multiplication':<15} | {result}")
        
        elif choice == '4':
            if num2 == 0:
                print(f"{f'{num1}, {num2}':<20} | {'Division':<15} | Error: Divide by 0")
            else:
                result = num1 / num2
                print(f"{f'{num1}, {num2}':<20} | {'Division':<15} | {result}")
        
        else:
            print(f"{f'{num1}, {num2}':<20} | {'Invalid':<15} | Invalid operation!")

        print("-"*50)

    except ValueError:
        print("\n" + "-"*50)
        print(f"{'Invalid input':<20} | {'Error':<15} | Please enter valid numbers")
        print("-"*50)


calculator()
