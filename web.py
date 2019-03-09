from urllib.request import urlopen

response = urlopen("https://en.wikipedia.org/wiki/Google")
html = response.read();

with open("input.txt","wb") as f:
    f.write(html.decode("UTF-8").encode("UTF-8"))
    f.close()
