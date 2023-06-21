import requests

# contoh penggunaan requests

url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
res = requests.get(url)

# cek status code
if res.status_code != 200:
    print('Error')
else:
    print('Isi Source Code Website wikipedia: ', res.text) # jika status code website adalah 200 maka akan mencetak isi source website

