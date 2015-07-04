from urllib2 import urlopen 
def get_external_resource(url,read=True):
    response = urlopen(url)
    if read:
        return response.read()
    else:
        return response
