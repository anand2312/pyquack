"""
MIT License

Copyright (c) 2021-present Anand Krishna

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import argparse

from pyquack import __version__
from .sync import Client, query

parser = argparse.ArgumentParser()

parser.add_argument(
    "query",
    help="Search a specific query on duckduckgo. Enter 'repl' to start a REPL session.",
)

args = parser.parse_args()


if args.query == "repl":
    client = Client()
    print(
        f"pyquack {__version__}\nType your search queries in.\nEnter 'exit' or CTRL + C to exit."
    )

    while True:
        try:
            query = input(">>> ")
        except KeyboardInterrupt:
            break

        if query.lower().strip() == "exit":
            break

        response = client.query(query)

        print(response.abstract)
        print(response.answer)

        for i in response.results:
            print(i)

        print(f"Result type: {response.type}")
else:
    response = query(args.query)

    print(response.abstract)
    print(response.answer)

    for i in response.results:
        print(i)

    print(f"Result type: {response.type}")
