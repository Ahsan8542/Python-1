import datetime
import calendar

temperature = float(input("Enter the temperature in Celsius: "))
city = input("Enter the city name: ")

if temperature > 20:
    print(f"It is boiling outside in {city}.")
elif temperature > 10:
    print(f"It is warm outside in {city}.")
elif temperature > 5:
    print(f"It is fine outside in {city}.")
elif temperature < 2:
    print(f"It is freezing outside in {city}.")
else:
    print(f"It is cold outside in {city}.")

import datetime
import calendar

print("Current date and time:", datetime.datetime.now())
print("Current year:", datetime.datetime.now().year)
print("Current month:", datetime.datetime.now().month)