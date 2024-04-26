from django.test import TestCase
from .models import sportsData

class SportsLeagueDataTestCase(TestCase):
    def test_data_saved_in_db(self):
        # Create a sample data instance
        data = sportsData.objects.create(
            league_id=4,
            league_name="Euro Championship",
            league_country="World"
        )

        # Retrieve the data from the database
        saved_data = sportsData.objects.get(id=data.id)

        # Assert that the data saved matches the data we created
        self.assertEqual(saved_data.league_id, 4)
        self.assertEqual(saved_data.league_name, "Euro Championship")
        self.assertEqual(saved_data.league_country, "World")