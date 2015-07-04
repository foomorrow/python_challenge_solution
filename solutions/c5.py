import re,urllib2
import pickle
from utils import get_external_resource
def resolve():
    banner_p = get_external_resource('http://www.pythonchallenge.com/pc/def/banner.p')
    obj = pickle.loads(banner_p)
    for item in obj:
        print "".join(map(lambda p: p[0]*p[1], item))
    return 'channel'

# answer = resolve()
answer = 'channel'
