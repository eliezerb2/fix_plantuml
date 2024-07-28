"""
Unit tests for remove_adjacent_duplicates module.
"""

import os
import unittest

from src.remove_adjacent_duplicates import remove_adjacent_duplicates


class TestRemoveAdjacentDuplicates(unittest.TestCase):
    """
    Test cases for remove_adjacent_duplicates function.
    """

    def setUp(self) -> None:
        """
        Set up test environment.
        """
        self.input_sample_file = 'tests/test_files/input_sample.plantuml'
        self.output_sample_file = 'tests/test_files/output_sample.plantuml'
        self.output_file = 'tests/test_files/output.plantuml'

    def test_remove_adjacent_duplicates(self) -> None:
        """
        Test remove_adjacent_duplicates function.
        """
        remove_adjacent_duplicates(self.input_sample_file, self.output_file)

        with open(self.output_file, 'r', encoding="utf-8") as f:
            output_lines = f.readlines()

        with open(self.output_sample_file, 'r', encoding="utf-8") as f:
            expected_lines = f.readlines()

        self.assertEqual(output_lines, expected_lines)

    def tearDown(self) -> None:
        """
        Clean up after test.
        """
        if os.path.exists(self.output_file):
            os.remove(self.output_file)


if __name__ == '__main__':
    unittest.main()
