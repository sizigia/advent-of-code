import unittest
from day6 import get_answer_count, get_everyone_answer_count


class TestAnswersCount(unittest.TestCase):
    def test_anyone_valid_count(self):
        ans_toy = ['abc', 'a\nb\nc', 'ab\nac', 'a\na\na\na', 'b']
        result = sum([get_answer_count(g) for g in ans_toy])
        self.assertEqual(
            result, 11, "Count must be 11.")

    def test_everyone_valid_count(self):
        ans_toy = ['abc', 'a\nb\nc', 'ab\nac', 'a\na\na\na', 'b']
        result = sum([get_everyone_answer_count(g) for g in ans_toy])
        self.assertEqual(
            result, 6, "Count must be 11.")
