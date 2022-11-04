from typing import List, Tuple, Dict
from urllib.parse import urlparse, urlunparse, parse_qs

__all__ = [
    "get_host_url",
    "get_query_params",
    "strip_query_params",
    "breakdown"
]


def get_host_url(url: str):
    urlp = urlparse(url)
    return f"{urlp.scheme}://{urlp.hostname}"


def get_query_params(url: str) -> Dict[str, List[str]]:
    parsed_url = urlparse(url)
    parsed_qs = parse_qs(parsed_url.query)
    return parsed_qs or dict()


def breakdown(url: str) -> Tuple[str, Dict[str, List[str]]]:
    """
    Splits the URL into the bare URL and the query params
    :param url: URL may or may not containing the query params
    :return: The bare URL and the dictionary of query params
    """
    params = get_query_params(url)
    return strip_query_params(url), params


def strip_query_params(url: str):
    parsed_url = urlparse(url)
    return urlunparse((parsed_url.scheme, parsed_url.hostname, parsed_url.path, "", "", ""))
