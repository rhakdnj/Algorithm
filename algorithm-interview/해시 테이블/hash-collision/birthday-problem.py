import random


TRIALS: int = 100000
same_birthdays: int = 0

for _ in range(TRIALS):
    birthdays = []
    # When 23 people gather and they have the same birthday, same_birthdays += 1
    for i in range(23):
        birthday = random.randint(1, 365)
        if birthday in birthdays:
            same_birthdays += 1
            break
        birthdays.append(birthday)

print(f'{same_birthdays / TRIALS * 100:.2f}%')
