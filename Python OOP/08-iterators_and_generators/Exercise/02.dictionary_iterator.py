class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.items = list(dictionary.items())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.items):
            raise StopIteration

        self.index += 1

        return self.items[self.index - 1]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

print()

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)

# test zero
# import unittest
#
#
# class DictionaryIteratorTests(unittest.TestCase):
#     def test_zero(self):
#         result = dictionary_iter({1: "1", 2: "2"})
#         expected = []
#         for x in result:
#             expected.append(x)
#         self.assertEqual(expected, [(1, "1"), (2, "2")])
#
#
# if __name__ == '__main__':
#     unittest.main()
