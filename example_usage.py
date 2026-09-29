from client import URLCanonicalizer

url = "https://www.GitHub.com/alphaparkinc/repo/?utm_campaign=spring&id=42&fbclid=123"
canonical = URLCanonicalizer.canonicalize(url)
print("Canonical Clean URL:", canonical)
