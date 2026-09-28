score = 0

age = int(input("Enter your age: "))
name = input("Enter your name: ")
if age < 18:
    print("You are not eligible to play the game.")
else:
    print(f"Welcome, {name}! You are eligible to play the game.")