#!/usr/local/bin/python3
# Made by @swisscoding on Instagram

from colored import stylize, fg

# decoration
print(stylize("\n---- | Get Body-Mass-Index | ----\n", fg("red")))

# class
class BMI:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    # output magic method
    def __repr__(self):
        bmi = self.calculate(self.w, self.h)
        print(stylize(f"\nYour BMI is {bmi}.", fg("red")))
        if bmi < 18.5:
            return "You are underweight.\n"
        elif bmi < 24.9:
            return "You are normal weight.\n"
        else:
            return "You are overweight.\n"


    # methods
    def calculate(self, weight, height):
        return round(weight / (height**2), 2)

# main execution
if __name__ == "__main__":
    # user interaction
    weight = float(input("Weight in kg: "))
    height = float(input("Height in meter: "))

    print(BMI(weight, height))
