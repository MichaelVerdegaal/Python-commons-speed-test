from profilehooks import profile


@profile()
def concat_plus():
    result = ""
    for x in range(1000000):
        result = result + str(x)
    return result

@profile()
def concat_plus_is():
    result = ""
    for x in range(1000000):
        result += str(x)
    return result

@profile()
def concat_join():
    result = ''
    for x in range(1000000):
        result = ''.join(str(x))
    return result


concat_plus()
concat_plus_is()
concat_join()
