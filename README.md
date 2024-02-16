# Python Gale-Shapley Algorithm from .CSV file

This is a Python implementation of the Gale-Shapley algorithm to solve the stable marriage problem. The algorithm is
implemented using a .CSV file as input.

## ⚠️ DISCLAIMER

This implementation is not optimized and is not meant to be used in a production environment. It was also partially
generated through ChatGPT 3.5.

## Installation

This script requires Python 3.9 or later.

This script uses `csv` and `collections` libraries, which are part of the Python standard library and should not require
any additional installation.

## Usage

The .CSV file should be named `preferences.csv`, stored in the root of the repository and contain the following:

- The first row should contain the names of the groups, with an **unused cell** in the first column.
- The second row should contain the number of person per groups in the same order as the first row, with an **unused
  cell**
  in the first column.
- The following rows should contain the preferences of the individuals for each group. The first
  column should contain the name of the individual.

It should then look like this:

|           | Group 1 | Group 2 | Group 3 |
|-----------|---------|---------|---------|
| Team size | 2       | 1       | 1       |
| User 1    | 2       | 3       | 1       |
| User 2    | 1       | 2       | 3       |
| User 3    | 3       | 1       | 2       |
| User 4    | 3       | 1       | 2       |

Or in .CSV format:

```csv
,Group 1,Group 2,Group 3
Team size,2,1,1
User 1,2,3,1
User 2,1,2,3
User 3,3,1,2
User 4,3,1,2
```

The algorithm will then output the stable matches in the console, like:

```text
Group 1 : User 2, User 4, 
Group 2 : User 3, 
Group 3 : User 1, 
```