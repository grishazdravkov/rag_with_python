import argparse
import json
from lib.keyword_search import search_command, build_command


def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    build_parser = subparsers.add_parser("build", help="Build Keyword Search command" )
    search_parser = subparsers.add_parser("search", help="Search movies using keywords")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()

    match args.command:
        case "search":
            search_command_result = search_command(args.query)
            print(f"Searching for: {args.query}")
            for index, item in enumerate(search_command_result):
                print(f"{index+1}. {item['title']}")
        case "build":
            build_command_result = build_command()
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
