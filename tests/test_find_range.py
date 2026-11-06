from types import SimpleNamespace
import unittest

from algoBreno import find_range


class FindRangeTests(unittest.TestCase):
    def setUp(self):
        self.outputs = [
            SimpleNamespace(amount=5, timestamp=10),
            SimpleNamespace(amount=9, timestamp=20),
        ]

    def test_considers_the_earliest_output(self):
        self.assertEqual(find_range(self.outputs, 5), [10, 10])

    def test_returns_the_start_before_the_end(self):
        self.assertEqual(find_range(self.outputs, 14), [10, 20])

    def test_returns_empty_when_total_is_insufficient(self):
        self.assertEqual(find_range(self.outputs, 15), [])
