from calculator import operations


def parse(inputs, verbose=False):
    """Parse the input provided
    :param: input: input parameters for the calculation
    :type input: sorted iterable of strings
    :param: verbose: Verbosity setting
    :type verbose: boolean
    :rtype float"""
    result = None
    operation = None
    operation_map = {
        "+": operations.add,
        "-": operations.subtract,
        "*": operations.multiply,
        "/": operations.devide
    }

    for input in inputs:
        if input in operation_map:
            operation = operation_map[input]
            if result == None:
                raise(Exception("Provided operations without arguments"))
        else:
            try:
                tmp_input = float(input)
            except ValueError as e:
                raise (Exception(
                    "Provided input not understood. Either the operation is not supported or the input is malformed %s" % input))
            if result == None:
                result = tmp_input
            else:
                result = operation(result, tmp_input)
    return result