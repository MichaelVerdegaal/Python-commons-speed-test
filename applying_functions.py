from profilehooks import profile


@profile()
def apply_map():
    old_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    result = []
    for x in range(1000000):
        result = map(str.upper, old_list)
    return result


@profile()
def generator_expression():
    old_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    result = []
    for x in range(1000000):
        result = (char.upper() for char in old_list)
    return result


@profile()
def list_comprehension_no_dots():
    old_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    result = []
    up = str.upper
    for x in range(1000000):
        result = [up(char) for char in old_list]
    return result


@profile()
def list_comprehension():
    old_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    result = []
    for x in range(1000000):
        result = [char.upper() for char in old_list]
    return result


@profile()
def for_loop_no_dots():
    old_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    result = []
    up = str.upper
    for x in range(1000000):
        result = []
        for char in old_list:
            result.append(up(char))
    return result


@profile()
def simple_for_loop():
    old_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    result = []
    for x in range(1000000):
        result = []
        for char in old_list:
            result.append(char.upper())
    return result


simple_for_loop()
for_loop_no_dots()
list_comprehension()
list_comprehension_no_dots()
generator_expression()
apply_map()
