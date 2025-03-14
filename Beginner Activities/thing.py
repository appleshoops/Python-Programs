import unittest

def sum(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    return total

print(sum([1, 3, 3]))

class TestSumList(unittest.TestCase):
    def test_sum_positive_numbers(self):
        self.assertEqual(sum([1, 2, 3, 4, 5]), 15)
    
    def test_sum_negative_numbers(self):
        self.assertEqual(sum([-1, -2, -3, -4, -5]), -15)

    def test_sum_mixed_numbers(self):
        self.assertEqual(sum([-1, 2, -3, 4, -5]), -3)

    def test_sum_no_numbers(self):
        self.assertEqual(sum([]), 0)

    def test_sum_one_number(self):
        self.assertEqual(sum([5]), 5)

if __name__ == '__main__':
    unittest.main()