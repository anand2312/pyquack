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

from dataclasses import dataclass
from enum import Enum
from typing import List, Union


@dataclass(frozen=True)
class Abstract:

    html: Union[str, None]
    text: Union[str, None]
    source: Union[str, None]
    url: Union[str, None]
    image_url: Union[str, None]
    heading: Union[str, None]


@dataclass(frozen=True)
class Definition:

    text: Union[str, None]
    source: Union[str, None]
    url: Union[str, None]


@dataclass(frozen=True)
class Answer:

    text: Union[str, None]
    type: Union[str, None]


@dataclass(frozen=True)
class Icon:

    url: Union[str, None]
    height: Union[int, None]
    width: Union[int, None]


@dataclass(frozen=True)
class Result:

    # the `result` field has been omitted as they are HTML links which will be the same as `first_url`
    first_url: Union[str, None]
    icon: Icon
    text: Union[str, None]


RelatedTopic = Result  # they both have the same structure


class ResultType(Enum):
    """
    Enumeration representing the type of the QueryResult.
    """

    ARTICLE = "A"
    DISAMBIGUATION = "D"
    CATEGORY = "C"
    NAME = "N"
    EXCLUSIVE = "E"
    NOTHING = ""


@dataclass(frozen=True)
class QueryResult:

    abstract: Abstract
    answer: Answer
    definition: Definition
    related_topics: List[RelatedTopic]
    results: List[Result]
    type: ResultType
    redirect: Union[str, None]


def _parse_response(resp: dict) -> QueryResult:
    """
    Parses the raw response sent by the API into a QueryResult object.
    """

    abstract = Abstract(
        html=resp.get("Abstract"),
        text=resp.get("AbstractText"),
        source=resp.get("AbstractSource"),
        url=resp.get("AbstractURL"),
        image_url=resp.get("Image"),
        heading=resp.get("Heading"),
    )

    answer = Answer(text=resp.get("Answer"), type=resp.get("AnswerType"))

    definition = Definition(
        text=resp.get("Definition"),
        source=resp.get("DefinitionSource"),
        url=resp.get("DefinitionURL"),
    )

    related_topics = [
        RelatedTopic(
            first_url=i.get("FirstURL"),
            text=i.get("Text"),
            icon=_parse_icon(i.get("Icon", {})),
        )
        for i in resp.get("RelatedTopics", [])
    ]

    results = [
        Result(
            first_url=i.get("FirstURL"),
            text=i.get("Text"),
            icon=_parse_icon(i.get("Icon")),
        )
        for i in resp.get("Results", [])
    ]

    _type = ResultType(resp.get("Type", ""))
    redirect = resp.get("Redirect")

    return QueryResult(
        abstract=abstract,
        answer=answer,
        definition=definition,
        related_topics=related_topics,
        results=results,
        type=_type,
        redirect=redirect,
    )


def _parse_icon(raw_dict: dict) -> Icon:
    return Icon(
        url=raw_dict.get("URL"),
        height=raw_dict.get("Height"),
        width=raw_dict.get("Width"),
    )
