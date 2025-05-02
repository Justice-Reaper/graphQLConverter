# graphQLConverter

This script converts a GraphQL JSON into an x-www-form-urlencoded format, commonly used in HTTP requests with Content-Type: application/x-www-form-urlencoded. It also cleans the JSON of unnecessary characters (like line breaks, tabs, and multiple spaces) to ensure the resulting string is valid and optimized for web requests.

## Features

### JSON to URL-encoded Conversion
   - Transforms a GraphQL JSON string into an x-www-form-urlencoded string

### JSON Cleaning
   - Removes unnecessary characters like line breaks (\n), tabs (\t), multiple spaces, and other control characters that could affect JSON validity

### Easy to Use
   - The script runs from the command line and accepts JSON as an argument
   - Provides a help panel (-h) to guide the user

### Robust
   - Validates the input JSON and displays a clear error message if the JSON is invalid
   - Handles additional arguments and shows help if argument errors are detected

## Help Panel

```
# python graphQLConverter.py -h
usage: graphQLConverter.py [-h] [json]

convert a GraphQL JSON to URL encoded format

positional arguments:
  json        GraphQL JSON as a string. example: '{"query": "{ me { name } }"}'

options:
  -h, --help  show this help message and exit

example: python graphQLConverter.py '{"query": "{ me { name } }"}'
```

## Usage Example

```
git clone https://github.com/Justice-Reaper/graphQLConverter.git
cd graphQLConverter
python GraphQLConverter.py '{"query":"\n    mutation changeEmail($input: ChangeEmailInput!) {\n        changeEmail(input: $input) {\n            email\n        }\n    }\n","operationName":"changeEmail","variables":{"input":{"email":"testing@gmail.com"}}}'
URL Encoded Data:
query=mutation+changeEmail%28%24input%3A+ChangeEmailInput%21%29+%7BchangeEmail%28input%3A+%24input%29+%7Bemail%7D%7D&operationName=changeEmail&variables=%7B%22input%22%3A+%7B%22email%22%3A+%22testing%40gmail.com%22%7D%7D
```
