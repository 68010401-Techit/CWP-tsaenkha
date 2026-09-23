num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

mult = num1 * num2
print(f"{num1} x {num2} = {mult}")

if mult > 0:
    print("The result is positive.")
elif mult == 0:
    print("The result is positive and negative")
else:
    print("The result is negative")