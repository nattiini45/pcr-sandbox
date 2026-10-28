def unsafe_divide(value):
    return 10 / value


def existing_caller():
    return unsafe_divide(1)


def new_caller(value):
    return unsafe_divide(value)
