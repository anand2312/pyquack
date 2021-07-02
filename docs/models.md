# Models

All models are based on the raw API response itself sent. Refer [DuckDuckGo API page](https://duckduckgo.com/api) for more details.

## pyquack.response.QueryResult

| Name           | Type                                |
|----------------|-------------------------------------|
| abstract       | pyquack.response.Abstract           |
| answer         | pyquack.response.Answer             |
| definition     | pyquack.response.Definition         |
| related_topics | List[pyquack.response.RelatedTopic] |
| results        | List[pyquack.response.Result]       |
| type           | pyquack.response.ResultType         |
| redirect       | Optional[str]                       |

## pyquack.response.Abstract

| Name      | Description                                    |
|-----------|------------------------------------------------|
| html      | topic summary (can contain HTML, e.g. italics) |
| text      | topic summary (with no HTML)                   |
| source    | name of Abstract source                        |
| url       | deep link to expanded topic page               |
| image_url | link to image that goes with Abstract          |
| heading   | name of topic                                  |

## pyquack.response.Definition

| Name      | Description                                    |
|-----------|------------------------------------------------|
| html      | topic summary (can contain HTML, e.g. italics) |
| text      | topic summary (with no HTML)                   |
| source    | name of Abstract source                        |
| url       | deep link to expanded topic page               |

## pyquack.response.Answer

| Name      | Description                                               |
|-----------|-----------------------------------------------------------|
| text      | instant answer                                            |
| type      | type of answer                                            |

## pyquack.response.Icon

| Name      | Description                           |
|-----------|---------------------------------------|
| url       | URL to the image                      |
| height    | Height of image in pixels             |
| width     | Width of image in pixels              |

## pyquack.response.Result

| Name      | Description                           |
|-----------|---------------------------------------|
| first_url | first URL in the result               |
| icon      | pyquack.response.Icon                 |
| text      | text from first URL                   |

!!! note
    `pyquack.response.RelatedTopic` has the same structure as [`pyquack.response.Result`](#pyquack.response.Result)

## _enum_ pyquack.response.ResultType

| Name           | Value         |
|----------------|---------------|
| ARTICLE        | "A"           |
| DISAMBIGUATION | "D"           |
| CATEGORY       | "C"           |
| NAME           | "N"           |
| EXCLUSIVE      | "E"           |
| NOTHING        | ""            |
