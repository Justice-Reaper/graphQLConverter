import json
import urllib.parse
import argparse
import sys
import re

def clean_json_string(json_str):
    cleaned_str = re.sub(r'[\n\r\f\t\v]', '', json_str)
    cleaned_str = re.sub(r'\s{2,}', '', cleaned_str)
    return cleaned_str

def json_to_urlencoded(data):
    payload = {}

    for key, value in data.items():
        if isinstance(value, dict):
            payload[key] = clean_json_string(json.dumps(value))

        elif isinstance(value, str):
            payload[key] = clean_json_string(value)

        else:
            payload[key] = value

    urlencoded_data = urllib.parse.urlencode(payload)

    return urlencoded_data

def main():
    parser = argparse.ArgumentParser(
        description="convert a GraphQL JSON to URL encoded format",
        epilog='example: python graphQLConverter.py \'{"query": "{ me { name } }"}\''
    )

    parser.add_argument(
        "json",
        type=str,
        nargs="?",
        help='GraphQL JSON as a string. example: \'{"query": "{ me { name } }"}\''
    )

    args, unknown = parser.parse_known_args()

    if unknown or args.json is None:
        parser.print_help()
        sys.exit(1)

    try:
        cleaned_json_str = clean_json_string(args.json)
        graphql_json = json.loads(cleaned_json_str)

    except json.JSONDecodeError:
        print("Error: Invalid JSON provided")
        parser.print_help()
        sys.exit(1)

    urlencoded_result = json_to_urlencoded(graphql_json)
    
    print("URL Encoded Data:")
    print(urlencoded_result)

if __name__ == "__main__":
    main()
