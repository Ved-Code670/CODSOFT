import json

FILE = "history.json"

# Load previous history
try:
    with open(FILE, "r") as f:
        history = json.load(f)
except:
    history = []

print("Previous History:")
for i in history:
    print(i)

print("\n1.Add  2.Subtract  3.Multiply  4.Divide")
choice = input("Choose operation👉: ")

a = float(input("Enter number 1: "))
b = float(input("Enter number 2: "))

if choice == "1":
    result = a + b
    Operator = "+"
elif choice == "2":
    result = a - b
    Operator = "-"
elif choice == "3":
    result = a * b
    Operator = "*"
elif choice == "4":
    if b == 0:
        print("Cannot divide by zero❌")
        exit()
    result = a / b
    Operator = "/"
else:
    print("Invalid choice❕")
    exit()

expression = f"{a} {Operator} {b} = {result}"
print("Result:", result)

history.append(expression)

with open(FILE, "w") as f:
    json.dump(history, f)
