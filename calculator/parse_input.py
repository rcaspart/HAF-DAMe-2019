from calculator import operations

import operations


def parse(inputs):
    """Parse the input provided
    :param: inputs: input parameters for the calculation
    :type inputs: sorted iterable of strings
    :rtype float"""
    result = None
    operation = None
    operation_map = {
        "+": operations.add,
        "-": operations.subtract,
        "x": operations.multiply,
        "/": operations.devide
    }

    for ip in inputs:
        if ip in operation_map:
            operation = operation_map[ip]
            if result == None:
                raise(Exception("Provided operations without arguments"))
        else:
            try:
                tmp_ip = float(ip)
            except ValueError as e:
                raise (Exception(
                    "Provided input not understood. Either the operation is not supported or the input is malformed %s" % ip))
            if result == None:
                result = tmp_input
            else:
                result = operation(result, tmp_input)
    return result