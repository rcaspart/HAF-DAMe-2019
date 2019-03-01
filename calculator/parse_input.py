import logging

import operations


def parse(inputs):
    """Parse the input provided
    :param: inputs: input parameters for the calculation
    :type inputs: sorted iterable of strings
    :rtype float"""
    logger = logging.getLogger("calculator")
    result = None
    operation = None
    operation_map = {
        "+": operations.add,
        "-": operations.subtract,
        "x": operations.multiply,
        "/": operations.devide
    }
    logger.debug("Initiating input parsing")

    for ip in inputs:
        logger.debug("Parsing input %s"%ip)
        if ip in operation_map:
            operation = operation_map[ip]
            logger.debug("Found operation, using %s" %operation.__name__)
            if result == None:
                logger.error("Provided operations without arguments, exiting")
                raise(Exception("Provided operations without arguments"))
        else:
            try:
                tmp_ip = float(ip)
            except ValueError as e:
                logger.error("Provided input not understood. Either the operation is not supported or the input is malformed %s" % ip)
                raise (Exception(
                    "Provided input not understood. Either the operation is not supported or the input is malformed %s" % ip))
            if result == None:
                logger.debug("left-hand argument %s" % ip)
                result = tmp_ip
            else:
                logger.debug("right-hand argument %s" % ip)
                result = operation(result, tmp_ip)
                logger.debug("intermediate result %s" % ip)
    return result