#!/usr/bin/env python3

import argparse
import string
import json


def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using BM25")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()

    match args.command:
        case "search":
            # print the search query here
            print("Searching for:", args.query)
            result = []
            with open("data/movies.json") as f:
                movies_json = json.load(f)
                all_movies = movies_json["movies"]
                for i in range(len(all_movies)):
                    table = str.maketrans("", "", string.punctuation)
                    query = args.query.lower().translate(table)
                    title = all_movies[i]["title"].lower().translate(table)
                    # if query in title:
                    #     result.append(all_movies[i])
                    # if args.query.lower() in all_movies[i]["title"].lower():
                    #     result.append(all_movies[i])

                    query_token = query.split()
                    title_token = title.split()

                    # for q in range(len(query_token)):
                    for q in query_token:
                        for t in title_token:
                            if q in t:
                                result.append(all_movies[i])
                                break
            # if query_token[q] in title_token:
            #     result.append(all_movies[i])

            for i in range(len(result)):
                print(result[i]["id"], result[i]["title"])
                if i == 4:
                    break
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
