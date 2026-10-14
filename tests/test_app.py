import unittest

from app import add, is_even, summarize


class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(7))

    def test_summarize(self):
        self.assertEqual(
            summarize([1, 2, 3, 4]),
            {"count": 4, "sum": 10, "average": 2.5},
        )

    def test_summarize_empty(self):
        self.assertEqual(
            summarize([]),
            {"count": 0, "sum": 0, "average": 0.0},
        )


if __name__ == "__main__":
    unittest.main()