class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self.number:
            raise StopIteration

        self.index += 1
        self.number -= 1
        if self.index == len(self.sequence):
            self.index = 0

        return self.sequence[self.index - 1]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')

print()

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')
