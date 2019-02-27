import argparse
import parse_input

def main():
    CLI = argparse.ArgumentParser('')
    CLI.add_argument(
        '-v', '--verbose',
        dest="verbose",
        help="Enable verbose output",
        default=False,
        action="store_true"
    )
    CLI.add_argument(
        'operations',
        metavar="N",
        type=str,
        nargs="+",
        help="Operation to be performed"
    )
    options = CLI.parse_args()
    return parse_input.parse(options.operations, options.verbose)

if __name__ == "__main__":
    main()