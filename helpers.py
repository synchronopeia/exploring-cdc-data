import decouple

def get_env(field_name):
    try:
        field_value = decouple.config(field_name)
        return field_value;
    except decouple.UndefinedValueError as err:
        print("NameError:", "Your project directory must contain a file named \".env\" with an entry for " + field_name + ".")
        raise
    except:
        print("UNKNOWN ERROR")
        raise