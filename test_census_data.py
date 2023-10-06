import unittest
import simd_census_analysis


class TestCensusData(unittest.TestCase):
    """Contains tests for the class CensusData."""

    def setUp(self):
        self.census = simd_census_analysis.CensusData("data/census_data_sample.csv")

    def test_regions_loaded(self):
        """Tests that the returned list of regions contains all expected
        regions, with the file being loaded.
        """
        self.census.load()
        regions = self.census.regions()
        tested_regions = ["Cherryville", "Appleburgh", "Pearlin"]
        self.assertEqual(tested_regions, regions)

    def test_regions_unloaded(self):
        """Tests that the function returns an empty list if
        no .csv file has been loaded.
        """
        regions = self.census.regions()
        self.assertEqual(regions, [])

    def test_total_population_loaded_all(self):
        """Tests the total polulation of a region."""
        self.census.load()
        total_pop = self.census.total_population("Cherryville", 100)
        self.assertEqual(total_pop, 115_700)

    def test_total_population_loaded_2(self):
        """Tests the population of the region under the age of 2."""
        self.census.load()
        total_pop = self.census.total_population("Appleburgh", 2)
        self.assertEqual(total_pop, 46_000)

    def test_total_population_unloaded(self):
        """Tests that the function returns None if
        no .csv file has been loaded.
        """
        total_pop = self.census.total_population("Pearlin", 100)
        self.assertEqual(total_pop, None)

    def test_total_population_loaded_not_in_list(self):
        """Tests that the function returns None if
        region value is not in the .csv file.
        """
        self.census.load()
        total_pop = self.census.total_population("Melonshire", 100)
        self.assertEqual(total_pop, None)


if __name__ == "__main__":
    unittest.main()
