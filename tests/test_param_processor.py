"""
Unit tests for param_processor module.
"""

import os
import tempfile
import unittest
from unittest.mock import patch

from src.param_processor import process_parameters


class TestParamProcessor(unittest.TestCase):
    """
    Test cases for process_parameters function.
    """

    def setUp(self) -> None:
        """
        Set up test environment.
        """
        # Create a temporary file to simulate the original file
        self.original_file = tempfile.NamedTemporaryFile(delete=False)
        self.original_file_path = self.original_file.name
        self.original_file.write(b"Test content\n")
        self.original_file.close()

        # Create another temporary file to simulate the new file
        self.new_file = tempfile.NamedTemporaryFile(delete=False)
        self.new_file_path = self.new_file.name
        self.new_file.close()

    def tearDown(self) -> None:
        """
        Clean up after test.
        """
        if os.path.exists(self.original_file_path):
            os.remove(self.original_file_path)
        if os.path.exists(self.new_file_path):
            os.remove(self.new_file_path)

    @patch('builtins.input', lambda *args: 'n')
    def test_confirm_overwrite_no(self) -> None:
        """
        Test process_parameters function when overwrite is not confirmed.
        """
        with self.assertRaises(FileExistsError):
            with patch('sys.argv', ['main.py', '--original', self.original_file_path, '--new', self.new_file_path]):
                process_parameters()

    @patch('builtins.input', lambda *args: 'y')
    def test_confirm_overwrite_yes(self) -> None:
        """
        Test process_parameters function when overwrite is confirmed.
        """
        with patch('sys.argv', ['main.py', '--original', self.original_file_path, '--new', self.new_file_path]):
            original_path, new_path, confirm = process_parameters()
            self.assertEqual(original_path, self.original_file_path)
            self.assertEqual(new_path, self.new_file_path)
            self.assertIsNone(confirm)

    def test_confirm_parameter_yes(self) -> None:
        """
        Test process_parameters function with confirm parameter set to yes.
        """
        with patch('sys.argv', ['main.py', '--original', self.original_file_path, '--new', self.new_file_path, '--confirm', 'yes']):
            original_path, new_path, confirm = process_parameters()
            self.assertEqual(original_path, self.original_file_path)
            self.assertEqual(new_path, self.new_file_path)
            self.assertEqual(confirm, 'yes')

    def test_confirm_parameter_all(self) -> None:
        """
        Test process_parameters function with confirm parameter set to all.
        """
        with patch('sys.argv', ['main.py', '--original', self.original_file_path, '--new', self.new_file_path, '--confirm', 'all']):
            original_path, new_path, confirm = process_parameters()
            self.assertEqual(original_path, self.original_file_path)
            self.assertEqual(new_path, self.new_file_path)
            self.assertEqual(confirm, 'all')


if __name__ == '__main__':
    unittest.main()
