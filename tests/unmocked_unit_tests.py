import unittest
import sys
import os

# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))

# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)

# adding the parent directory to
# the sys.path.
sys.path.append(parent)

from nutritionix import extract_nutrition_values
from documenu import extract_menu_items

INPUT = "INPUT"
EXPECTED_OUTPUT = "EXPECTED_OUTPUT"


class GetNutritionDataTests(unittest.TestCase):
    def setUp(self):
        self.success_test_params = [
            {
                INPUT: {},
                EXPECTED_OUTPUT: (None, None, None),
            },
            {
                INPUT: {
                    "hits": [
                        {
                            "fields": {
                                "nf_calories": "120",
                                "nf_total_fat": "25",
                                "nf_serving_size_qty": "1",
                            }
                        }
                    ]
                },
                EXPECTED_OUTPUT: ("120", "25", "1"),
            },
            {
                INPUT: {
                    "hits": [],
                },
                EXPECTED_OUTPUT: (
                    None,
                    None,
                    None,
                ),
            },
        ]

    def test_extract_nutrition_data(self):
        for test in self.success_test_params:
            self.assertEqual(
                extract_nutrition_values(test[INPUT]), test[EXPECTED_OUTPUT]
            )


class GetMenuItemsDataTests(unittest.TestCase):
    def setUp(self):
        self.success_test_params = [
            {
                INPUT: {
                    "menu_items": [
                        {
                            "name": "Tacos",
                            "pricing": [{"priceString": "$10"}],
                            "description": "a wheat tortilla",
                        }
                    ]
                },
                EXPECTED_OUTPUT: ("Tacos", "$10", "a wheat tortilla"),
            },
            {
                INPUT: {"menu_items": []},
                EXPECTED_OUTPUT: (None, None, None),
            },
            {
                INPUT: {
                    "menu_items": [
                        {
                            "name": "Chicken Quesadilla",
                            "pricing": [{"priceString": "$12"}],
                            "description": "",
                        }
                    ]
                },
                EXPECTED_OUTPUT: ("Chicken Quesadilla", "$12", ""),
            },
        ]

    def test_get_menu_items(self):
        for test in self.success_test_params:
            self.assertEqual(extract_menu_items(test[INPUT]), test[EXPECTED_OUTPUT])


if __name__ == "__main__":
    unittest.main()
