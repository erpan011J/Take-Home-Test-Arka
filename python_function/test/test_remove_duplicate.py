import unittest
from python_function.remove_duplicate import remove_duplicates

class TestRemoveDuplicates(unittest.TestCase):

    def test_remove_duplicates(self):
        # Test case 1: List with duplicates
        input_list_1 = [1, 2, 3, 2, 4, 3]
        expected_output_1 = [1, 2, 3, 4]
        self.assertEqual(remove_duplicates(input_list_1), expected_output_1)

        # Test case 2: List without duplicates
        input_list_2 = [1, 2, 3, 4, 5]
        expected_output_2 = [1, 2, 3, 4, 5]
        self.assertEqual(remove_duplicates(input_list_2), expected_output_2)

        # Test case 3: Empty list
        input_list_3 = []
        expected_output_3 = []
        self.assertEqual(remove_duplicates(input_list_3), expected_output_3)

        # Test case 4: List with all duplicates
        input_list_4 = [1, 1, 1, 1]
        expected_output_4 = [1]
        self.assertEqual(remove_duplicates(input_list_4), expected_output_4)

        # Test case 5: List with no elements
        input_list_5 = []
        expected_output_5 = []
        self.assertEqual(remove_duplicates(input_list_5), expected_output_5)
