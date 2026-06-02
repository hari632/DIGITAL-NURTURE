from tabulate import tabulate

class Converter:

    def c_to_f(self, c):
        return (c * 9/5) + 32

    def c_to_k(self, c):
        return c + 273.15

    def f_to_c(self, f):
        return (f - 32) * 5/9

    def k_to_c(self, k):
        return k - 273.15


converter = Converter()

print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Celsius to Kelvin")
print("3. Fahrenheit to Celsius")
print("4. Kelvin to Celsius")

choice = int(input("Enter Choice: "))
temp = float(input("Enter Temperature: "))

result = None
conversion = ""

if choice == 1:
    result = converter.c_to_f(temp)
    conversion = "C → F"

elif choice == 2:
    result = converter.c_to_k(temp)
    conversion = "C → K"

elif choice == 3:
    result = converter.f_to_c(temp)
    conversion = "F → C"

elif choice == 4:
    result = converter.k_to_c(temp)
    conversion = "K → C"

else:
    print("Invalid Choice")

if result is not None:

    table = [
        [conversion, f"{temp:.2f}", f"{result:.2f}"]
    ]

    print(
        tabulate(
            table,
            headers=["Conversion", "Input", "Output"],
            tablefmt="grid"
        )
    )