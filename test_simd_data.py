import unittest
import simd_census_analysis


class TestSIMD_Data(unittest.TestCase):
    """Contains tests for the class SIMD_Data."""

    def setUp(self):
        self.simd_data = simd_census_analysis.SIMD_Data("data/simd_data_sample.csv")

    def test_regions_loaded(self):
        """Tests that the returned list of regions contains all expected
        regions, with the file being loaded.
        """
        self.simd_data.load()
        regions = self.simd_data.regions()
        tested_regions = ["Cherryville", "Appleburgh", "Pearlin"]
        self.assertEqual(tested_regions, regions)

    def test_regions_unloaded(self):
        """Tests that the function returns an empty list if
        there has been no .csv file loaded.
        """
        regions = self.simd_data.regions()
        self.assertEqual(regions, [])

    def test_lowest_simd_loaded(self):
        """Tests the function lowest_simd of the class SIMD_Data,
        with a .csv file being loaded.
        """
        self.simd_data.load()
        region = self.simd_data.lowest_simd()
        self.assertEqual(region, "Pearlin")

    def test_lowest_simd_unloaded(self):
        """Tests the function lowest_simd of the class SIMD_Data,
        with no .csv file being loaded.
        """
        region = self.simd_data.lowest_simd()
        self.assertEqual(region, None)


if __name__ == "__main__":
    unittest.main()
