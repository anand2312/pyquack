# Quickstart

## Synchronous
```py
import pyquack

client = pyquack.Client()

response = client.query("DuckDuckGo")

print(response.results)
print(response.definition)
```

For all of the available attributes on the `response` object, refer [Models](models.md#QueryResult)


## Asynchronous
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
