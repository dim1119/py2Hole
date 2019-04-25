import argparse
import Parser


def main():
    # using argparse for the arguments
    parser = argparse.ArgumentParser(description="Pihole API interface")
    parser.add_argument('-v', '--version', action='version',version='%(prog)s 1.0')
    parser.add_argument('command',
                        choices=Parser.FUNCTION_MAP.keys())  # getting the appropriate functions from FUNCTION_MAP
    args=parser.parse_args()
    func = Parser.FUNCTION_MAP[args.command]  # calling the appropriate function
    print(func())


if __name__ == "__main__":
    main()


