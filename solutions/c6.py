from zipfile import ZipFile
import re

from utils import get_external_resource
pattern = re.compile(r'[\d]{2,5}')
def resolve():
    with open('channel.zip','w') as channelZip:
        channelZip.write(get_external_resource('http://www.pythonchallenge.com/pc/def/channel.zip'))
    with ZipFile('channel.zip','r') as channel:
        return find_next(channel)


def find_next(zip_file, name='readme', comments=[]):
    file_name = '%s.txt' % name
    content = zip_file.read(file_name)
    comment = zip_file.getinfo(file_name).comment
    groups = pattern.findall(content)
    if len(groups) == 0:
        print ''.join(comments)
        return set(filter(lambda x:x.isalpha(),comments))
    else:
        return find_next(zip_file,name=groups[-1],comments=comments + [comment] )
# answer = resolve()
answer = 'oxygen'
