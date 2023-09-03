from calculator import Calculator

def main():
    calculator = Calculator()
    while True:
        print("\n1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 5:
            break
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        if choice == 1:
            print("Result: ", calculator.add(a, b))
        elif choice == 2:
            print("Result: ", calculator.subtract(a, b))
        elif choice == 3:
            print("Result: ", calculator.multiply(a, b))
        elif choice == 4:
            try:
                print("Result: ", calculator.divide(a, b))
            except ValueError as e:
                print(e)

if __name__ == "__main__":
    main()
