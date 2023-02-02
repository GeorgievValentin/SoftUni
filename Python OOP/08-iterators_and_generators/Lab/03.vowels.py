class vowels:
    def __init__(self, text: str):
        self.text = text
        self.vowels = "AEOUYIaeouyi"
        self.result = [el for el in self.text if el in self.vowels]
        self.start = 0
        self.end = len(self.result)

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == self.end:
            raise StopIteration

        index = self.start
        self.start += 1

        return self.result[index]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
