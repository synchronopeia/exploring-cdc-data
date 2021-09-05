import sys
from decouple import config

def get_env(field_name):
    try:
        field_value = config(field_name)
        print(field_name)
        # print(field_name, field_value)
        return field_value
    except decouple.UndefinedValueError as err:
        print("NameError:", "Your project directory must contain a file named \".env\" with an entry for " + field_name + ".")
        raise
    except:
        print("UNKNOWN ERROR")
        raise

def exit_with_error():
    print("CSV data not read. Exiting script without doing anything.")
    sys.exit(1)