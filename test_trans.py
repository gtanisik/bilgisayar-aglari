import urllib.request, urllib.parse, json

def translate(text):
    url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=tr&dt=t&q=" + urllib.parse.quote(text)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req)
    data = json.loads(response.read().decode('utf-8'))
    return "".join(i[0] for i in data[0])

print(translate("Computer Networks and Internets"))
