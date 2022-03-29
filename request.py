import requests

nom = "mot"
url=str.format("https://fr.openfoodfacts.org/cgi/search.pl?search_terms={}&search_simple=1&action=process&json=1",nom)
requests.get(url)
