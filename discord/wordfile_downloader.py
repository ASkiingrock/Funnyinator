import requests

words_file_url = "https://github.com/ASkiingrock/Funnyinator/raw/main/words.json"

r = requests.get(words_file_url, allow_redirects=True)
open("words.json", "wb").write(r.content)
