import urllib.parse
import requests


main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Manila, Philippines"
dest = "Marikina, Philippines"
key = "AyRhfyHs9PM5gRGGoct61Xt40AyL9FiY"

url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest}) 

json_data = requests.get(url).json()
print(json_data)

print("Done by: ZANDLEX KEANO M. CRUZ | 15-19-2022")

# ZANDLEX KEANO M. CRUZ | 15-19-2022