import Image,re
from utils import get_external_resource

pattern = re.compile(r'\[(.*)\]')

def resolve():
    with open('oxygen.png','w') as img:
        img.write(get_external_resource('http://www.pythonchallenge.com/pc/def/oxygen.png'))
    img = Image.open("oxygen.png")
    w,h = img.size
    info = ''.join([chr(img.getpixel((i,h//2))[0]) for i in range(0,w,7)])
    return ''.join(map(chr,map(int,pattern.findall(info)[0].split(','))))
# answer = resolve()
answer = 'integrity'
