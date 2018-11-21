from profilehooks import profile


@profile()
def format_f_string():
    result = ""
    for x in range(1000000):
        result = f"{x}"
    return result

@profile()
def format_dot_format():
    result = ""
    for x in range(1000000):
        result = "".format(x)
    return result

@profile()
def format_percentage():
    result = ""
    for x in range(1000000):
        result = "%s" % x
    return result


format_f_string()
format_dot_format()
format_percentage()
