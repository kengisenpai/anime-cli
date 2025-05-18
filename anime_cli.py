import argparse
from api import search_anime, get_top_anime
from utils import print_anime_list

def main():
    parser = argparse.ArgumentParser(description="Anime CLI Tool")
    parser.add_argument("command", choices=["search", "top"], help="Command to run")
    parser.add_argument("query", nargs="?", help="Anime name (for search)")

    args = parser.parse_args()

    if args.command == "search":
        if not args.query:
            print("Please provide an anime name to search.")
            return
        results = search_anime(args.query)
        print_anime_list(results)

    elif args.command == "top":
        results = get_top_anime()
        print_anime_list(results)

if __name__ == "__main__":
    main()
