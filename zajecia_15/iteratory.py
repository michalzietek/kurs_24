class Iterator:
    # def __iter__(self):
    #     for number in range(6):
    #         yield number

    def __iter__(self):
        return iter([0, 1, 2, 3, 4, 5])


def generator():
    for number in range(6):
        yield number

iterator = Iterator()
for number in iterator:
    print(number)

for number2 in iterator:
    print(number2)
generator = generator()
for number in generator:
    print(number)

#next(generator)
print(iter(iterator))