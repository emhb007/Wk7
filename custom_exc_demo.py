from person import Person, InsufficientSweetsException

fred = Person("Fred","M")
wilma = Person("Wilma","F",5)
print(fred)
print("Fred gets 10 sweets -->")
fred.give_sweets(10)
print(fred)
print("Fred eats 6 sweets -->")
print(fred.eat_sweets(6))
try:
    print(wilma)
    print("Wilma eats 6 sweets -->")
    print(wilma.eat_sweets(6))
except InsufficientSweetsException as e:
    print(e)
finally:
    print(wilma)

print("Done.")