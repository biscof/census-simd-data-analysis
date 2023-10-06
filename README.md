# Scotland's Census and SIMD Data Analysis


## Overview

This repository contains a Python data analysis project developed as part of a student coursework. The project includes two classes, `CensusData` and `SIMD_Data`, that provide tools for retrieving and analyzing data from [Scotlans's Census](https://www.scotlandscensus.gov.uk) and [SIMD](https://simd.scot) (Scottish Index of Multiple Deprivation) data files. These classes load data from CSV files, calculate averages, and provide insights into population demographics and SIMD rankings for regions.

The project also includes comprehensive unit tests for both `CensusData` and `SIMD_Data` classes.


## Features:

- Load and analyze Census data, including total population by age range for various regions.
- Load and analyze SIMD data, calculating the average SIMD rank per region.
- Identify regions with the lowest SIMD rank and retrieve demographic information.


## Usage:

1. Clone the repository:
```
git clone https://github.com/biscof/census-simd-data-analysis.git
```
2. Run the main script:
```
python simd_census_analysis.py
```
3. Run the unit tests (optionally):
```
python -m unittest discover -v
```