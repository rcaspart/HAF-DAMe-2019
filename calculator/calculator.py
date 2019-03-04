import argparse
import parse_input
import logging


def main():
    cli = argparse.ArgumentParser('')
    cli.add_argument(
        '-v', '--verbose',
        dest="verbose",
        help="Enable verbose output",
        default=False,
        action="store_true"
    )
    cli.add_argument(
        'operations',
        metavar="N",
        type=str,
        nargs="+",
        help="Operation to be performed"
    )
    options = cli.parse_args()

    logger = logging.getLogger("calculator")
    fh = logging.FileHandler("calculator.log", mode="w")
    if options.verbose:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    ch = logging.StreamHandler()
    logger.addHandler(ch)
    logger.addHandler(fh)

    result = parse_input.parse(options.operations)
    logger.info("the result of %s is %s" % (" ".join(options.operations), result))


if __name__ == "__main__":
    main()
