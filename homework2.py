numbers = []
while True:
    try:
        user_input = input("Give a number list: ")
        if user_input.lower() == 'exit':
            break
        numbers = list(map(int, user_input.split()))
        break
    except ValueError:
        print("Type only numbers divided by spaces!")
        print("(type Exit to end the program)")

print(numbers)
