"""URL Canonicalization & Deduplication Filter.
100% Python Standard Library.
"""

import urllib.parse

class URLCanonicalizer:
    """Normalizes URL strings by stripping tracking tokens, ordering params, and resolving paths."""
    TRACKING_PARAMS = {"utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content", "fbclid", "gclid"}

    @classmethod
    def canonicalize(cls, url):
        parsed = urllib.parse.urlparse(url)
        netloc = parsed.netloc.lower()
        if netloc.startswith("www."):
            netloc = netloc[4:]
        query_dict = urllib.parse.parse_qs(parsed.query)
        cleaned_query = {k: v for k, v in query_dict.items() if k.lower() not in cls.TRACKING_PARAMS}
        sorted_query = urllib.parse.urlencode(sorted(cleaned_query.items()), doseq=True)
        path = parsed.path or "/"
        if path != "/" and path.endswith("/"):
            path = path[:-1]
        return urllib.parse.urlunparse((parsed.scheme.lower(), netloc, path, "", sorted_query, ""))
