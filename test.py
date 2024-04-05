name = "Ajiniyaz"
result = 2 + 4
print(name, result)
print("a little name thing".capitalize())


def add_one(num):
    if num >= 9:
        return num + 1

    total = num + 1
    print(total)
    return add_one(total)


mynewtotal = add_one(0)
print(mynewtotal)

# new lines added here/ test
