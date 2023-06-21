import requests # <- import modul yang telah diinstall

# contoh penggunaan requests

url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
res = requests.get(url)

# cek status code
print("Status Code Situs: {}".format(res.status_code))


