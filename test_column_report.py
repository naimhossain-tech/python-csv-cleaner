import unittest

from clean_csv import count_empty_cells


class TestColumnReport(unittest.TestCase):
    def test_counts_empty_cells_by_column(self):
        headers = ["Name", "Email", "City"]
        rows = [
            ["Naim", "naim@example.com", "Dhaka"],
            ["Rahim", "", "Chittagong"],
            ["Karim", "karim@example.com", ""],
            ["Sadia", "   ", "Khulna"],
        ]

        result = count_empty_cells(headers, rows)

        self.assertEqual(
            result,
            {
                "Name": 0,
                "Email": 2,
                "City": 1,
            },
        )

    def test_counts_none_and_empty_values(self):
        headers = ["A", "B"]
        rows = [
            [None, "value"],
            ["", None],
        ]

        self.assertEqual(
            count_empty_cells(headers, rows),
            {"A": 2, "B": 1},
        )

    def test_empty_dataset(self):
        self.assertEqual(
            count_empty_cells(["Name", "Email"], []),
            {"Name": 0, "Email": 0},
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
