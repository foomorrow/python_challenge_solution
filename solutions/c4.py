import re,urllib2

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s'
pattern = re.compile(r'[\d]+')


def fetch_linkedlist(value='12345'):
    response = urllib2.urlopen(url % value)
    content = response.read()
    print value,' : ',content
    if content == 'Yes. Divide by two and keep going.':
        return fetch_linkedlist(value=int(value)/2)

    groups = pattern.findall(content)

    if len(groups) == 0:
        return content
    else:
        return fetch_linkedlist(value=groups[-1])

# answer = fetch_linkedlist()
answer = 'peak.html'
