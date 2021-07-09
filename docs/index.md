# pyquack

A simple Python sync/async duckduckgo API wrapper.

## Installation

By default, pyquack will be synchronous and will use the [`requests`](https://requests.readthedocs.io) libary.
```
pip install -U pyquack
```

For async support,
```
pip install -U pyquack[async]
```
## Quickstart

### Synchronous
```py
import pyquack

client = pyquack.Client()

response = client.query("DuckDuckGo")

print(response.results)
print(response.definition)
```
For one-off queries,
```py
import pyquack

response = pyquack.query("DuckDuckGo")
```

For all of the available attributes on the `response` object, refer [Models](models.md#QueryResult)


### Asynchronous
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

### CLI
Pyquack also offers a CLI.
```
python -m pyquack
```

## Contact
Feel free to raise issues or contribute on [GitHub](https://github.com/anand2312/pyquack)

Contact me on Discord: anand#8837
