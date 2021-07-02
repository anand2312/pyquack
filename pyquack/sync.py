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
import requests

from .models import _parse_response, QueryResult


__version__ = "0.2.1"


class Client:
    """
    A synchronous API client which uses the `requests` module.
    """

    BASE_API_URL = "https://api.duckduckgo.com"

    def __init__(
        self, *, safesearch: bool = True, html: bool = False, meanings: bool = True
    ) -> None:
        """
        Initialize the client.

        Arguments:
            safesearch: Whether safesearch should be enabled.
            html: Whether there should be HTML in the API response.
            meanings: Whether to include disambiguations.
        """
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": f"pyquack {__version__}"})

        self._safesearch = safesearch
        self._html = html
        self._meanings = meanings

    def _params(self, query: str) -> dict:
        return {
            "q": query,
            "format": "json",
            "no_html": "0" if self._html else "1",
            "no_redirect": "1",
            "d": "0" if self._meanings else "1",
            "kp": "1" if self._safesearch else "-1",
        }

    def query(self, _query: str) -> QueryResult:
        """
        Run a query against the DuckDuckGo API.

        Arguments:
            _query: The query to be searched.

        Returns:
            [`QueryResult`](/pyquack/models/#pyquackresponsequeryresult) object containing the parsed API response.
        """
        params = self._params(_query)
        r = self.session.get(Client.BASE_API_URL, params=params)

        return _parse_response(r.json())


def query(
    _query: str, *, safesearch: bool = True, html: bool = False, meanings: bool = True
) -> QueryResult:
    """
    Function to make a one-off search query.

    !!! warning
        If you expect to be making many queries, use [`pyquack.Client`](/pyquack/api_reference/#pyquack.sync.Client) instead.
        `pyquack.Client` uses `requests.Session` internally, giving improved performance for multiple queries.
    Arguments:
        _query: The query to be searched.

    Returns:
        [`QueryResult`](/pyquack/models/#pyquackresponsequeryresult) object containing the parsed API response.
    """

    params = {
        "q": _query,
        "format": "json",
        "no_html": "0" if html else "1",
        "no_redirect": "1",
        "d": "0" if meanings else "1",
        "kp": "1" if safesearch else "-1",
    }

    r = requests.get(Client.BASE_API_URL, params=params)

    return _parse_response(r.json())
