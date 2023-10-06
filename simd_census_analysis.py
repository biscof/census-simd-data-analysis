import csv
import os.path


def skip_lines(file, num_of_lines_to_skip=0):
    """Skips a given number of lines at the beginning of the file."""
    i = 0
    while i < num_of_lines_to_skip:
        skipped_line = file.readline()
        if skipped_line == "":
            return False
        i += 1
    return True


class CensusData():
    """Contains a set of tools that allows to retrieve some information
    from a Census data file.
    """
    def __init__(self, file_name):
        self.file_name = file_name
        self.data_dict = {}

    def __repr__(self):
        s = f"CensusData(file_name=\"{self.file_name}\", "
        s += f"data_dict={self.data_dict})"
        return s

    def load(self):
        """Checks if the .csv file exists, opens it, and reads data.
        Then updates the self.data_dict dictionary that shows the total
        population per range and region.
        """
        if os.path.isfile(self.file_name):
            f = open(self.file_name, "r", encoding="iso-8859-1", newline="")
            skip_lines(f, 4)
            dict_reader = csv.DictReader(f, delimiter=",", quotechar='"')
            for row in dict_reader:
                if row["Region"] in self.data_dict.keys():
                    self.data_dict[row["Region"]].update({row["Range"]: row["All people"]})
                else:
                    self.data_dict[row["Region"]] = {row["Range"]: row["All people"]}
            f.close()
            return True
        else:
            return False

    def regions(self):
        """Returns a list of regions that have been uploaded to
        the self.data_dict dictionary.
        """
        return list(self.data_dict.keys())

    def total_population(self, name_of_region, age_boundary):
        """Returns the population in a certain region
        within a set age range.
        """
        if name_of_region in self.data_dict.keys():
            total_population = 0
            age = 0
            for range, number in self.data_dict[name_of_region].items():
                if range == "All people":
                    continue
                elif range == "Under 1":
                    age = 0
                elif range == "85 to 89":
                    age = 89
                elif range == "90 to 94":
                    age = 94
                elif range == "95 and over":
                    age = 100
                else:
                    age = int(range)

                if age > age_boundary:
                    break

                total_population += int(number)
            return total_population


class SIMD_Data():
    """Contains a set of tools that allows to retrieve some information
    from a SIMD data file.
    """
    def __init__(self, file_name):
        self.file_name = file_name
        self.data_dict = {}

    def __repr__(self):
        s = f"SIMD_Data(file_name=\"{self.file_name}\", "
        s += f"data_dict={self.data_dict})"
        return s

    def load(self):
        """Checks if the .csv file exists, opens it, and reads data.
        Then updates the self.data_dict dictionary that shows the average
        SIMD rank per region.
        """
        if os.path.isfile(self.file_name):
            f = open(self.file_name, "r", encoding="iso-8859-1", newline="")
            dict_reader = csv.DictReader(f, delimiter=",", quotechar='"')

            # Finding all the ranks for each region.
            region_ranks_list = {}
            for row in dict_reader:
                if row["MMWname"] in region_ranks_list.keys():
                    region_ranks_list[row["MMWname"]] += [int(row["SIMD2020v2_Rank"])]
                else:
                    region_ranks_list[row["MMWname"]] = [int(row["SIMD2020v2_Rank"])]

            # Colculating the average rank for each region.
            for region, ranks in region_ranks_list.items():
                if len(ranks) == 0:
                    continue
                avg_rank = sum(ranks) / len(ranks)
                self.data_dict[region] = round(avg_rank, 2)

            f.close()
            return True
        else:
            return False

    def regions(self):
        """Returns a list of regions that have been uploaded to
        the self.data_dict dictionary.
        """
        return list(self.data_dict.keys())

    def lowest_simd(self):
        """Reterns the name of a region with the lowest SIMD rank."""
        try:
            lwst_simd_in_dict = min(self.data_dict.values())
            lwst_simd_ind = list(self.data_dict.values()).index(lwst_simd_in_dict)
            regions_list = list(self.data_dict.keys())
            region = regions_list[lwst_simd_ind]
            return region
        except ValueError:
            return None


def main():
    census_data = CensusData("DC1117SC.csv")
    if not census_data.load():
        return

    simd_data = SIMD_Data("SIMD_2020v2csv.csv")
    if not simd_data.load():
        return

    lwst_simd_reg = simd_data.lowest_simd()
    print(f"The region with the lowest SIMD rank is {lwst_simd_reg}.")
    s = "The lowest average SIMD rank is "
    s += f"{simd_data.data_dict[lwst_simd_reg]}."
    print(s)

    tot_pop_lwst_simd_reg = census_data.total_population(lwst_simd_reg, 15)
    s = "The total population of 15 and under in the region "
    s += f"with the lowest SIMD rank is {tot_pop_lwst_simd_reg}."
    print(s)


if __name__ == "__main__":
    main()
