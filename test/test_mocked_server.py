import unittest
from unittest.mock import MagicMock, patch

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

from app import add_user, Users
from nutritionix import get_nutrition_values

INPUT = "INPUT"
EXPECTED_OUTPUT = "EXPECTED_OUTPUT"


class UpdateDBIDsTests(unittest.TestCase):
    def setUp(self):
        self.db_mock = [
            Users(
                username="Gyan",
                password="sha256:260000$Qh4nQsnGVhS19nZQ$535be7292b3afa38647e950ff51e63b1eccb5578090d90e7f39a9b414736c2a1",
            )
        ]

    def mock_add_to_db(self, artist):
        self.db_mock.append(artist)

    def mock_db_commit(self):
        pass

    def test_update_db_user(self):
        with patch("app.db.session.add", self.mock_add_to_db) as mock_query:
            with patch("app.db.session.commit", self.mock_db_commit):
                mock_filtered = MagicMock()
                mock_filtered.all.return_value = self.db_mock
                add_user("Test", "test123456")
                self.assertEqual(len(self.db_mock), 2)
                self.assertEqual(self.db_mock[1].username, "Test")


class GetNutritionValuesTests(unittest.TestCase):
    def test_get_nutrition_values(self):
        with patch("nutritionix.requests.get") as mock_requests_get:
            mock_response = MagicMock()
            # side_effect lets us set a list of return values.
            # Each successive call to mock_response.all() will generate the next
            # side effect
            mock_response.json.side_effect = [
                {
                    "hits": [
                        {
                            "fields": {
                                "nf_calories": "120",
                                "nf_total_fat": "10",
                                "nf_serving_size_qty": "1",
                            }
                        }
                    ]
                }
            ]
            mock_requests_get.return_value = mock_response
            output = f"Calories: 120, Total Fat: 10, Serving Size: 1"

            self.assertEqual(get_nutrition_values("Tacos"), output)

            mock_response.json.side_effect = [{"hits": []}]
            self.assertEqual(
                get_nutrition_values("a food item that does not exist"),
                "Nutrition information for this item is currently not available",
            )


if __name__ == "__main__":
    unittest.main()
