# pyquack
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Simple Python sync/async duckduckgo API wrapper.

[Documentation](https://pyquack.anand2312.tech)

## Quickstart

Synchronous:
```py
import pyquack

client = pyquack.Client()

response = client.query("DuckDuckGo")

print(response.results)
print(response.definition)
```

Async:
```py
import asyncio

import pyquack

async def main() -> None:
    client = pyquack.AsyncClient()

    response = await client.query("DuckDuckGo")

    print(response.results)
    print(response.definition)

asyncio.run(main())
```
