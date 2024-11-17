
from random import randint

numbers = []
for i in range(10):
    numbers.append(f"{randint(0, 9)}")
numbers = ','.join(numbers)
with open("data.txt", "a") as file:
    file.write(numbers)
    file.write("\n")