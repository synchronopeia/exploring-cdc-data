"""Quick Look at CSV Data

This script prints a summary of the CSV file named in the variable
COVID_CASES_FILENAME located in the directory specified in the
environment variable DATASET_DIR.

This script requires that a .env file be present in its directory.
The .env file must specify DATASET_DIR. For example:

DATASET_DIR=~/datasets/cdc

This script requires that `pandas` and `decouple` be installed within the Python
environment you are running this script in.
"""

import decouple
import pandas as pd
import os
import sys

# These are the variable declarations

COVID_CASES_FILENAME = "United_States_COVID-19_Cases_and_Deaths_by_State_over_Time.csv"
DATASET_DIR = ''
data = None

# This is the only function definition

def load_data(csv_path):
    """Attempt to read CSV file at csv_path and return a Pandas CSV data frame."""
    try:
        csv = pd.read_csv(csv_path)
        print("OK")
        return csv
    except FileNotFoundError as err:
        print("Unable to find CSV file '" + csv_path + "'.")
        raise
    except:
        print("ERROR")

# # # # # # # # # # #
#  --The Script--   #
# # # # # # # # # # #

# Try to set DATASET_DIR from .env
try:
    DATASET_DIR = decouple.config('DATASET_DIR')
except decouple.UndefinedValueError as err:
    print("NameError:", "Your project directory must contain a file named \".env\" with an entry for DATASET_DIR specifying the directory containing your CDC data files (e.g. DATASET_DIR=~/datasets/cdc).")
    sys.exit(1)

# Try to load the CSV data into a Pandas data frame
try: 
    data = load_data(os.path.join(DATASET_DIR, COVID_CASES_FILENAME))
except:
    print("CSV data not read. Exiting script without doing anything")
    sys.exit(1)

# At this point, the variable `data` contains the CSV table and we can do some analysis!

print(data.describe())
