import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

serviceurl = input('Enter URL: ')
#serviceurl = 'http://py4e-data.dr-chuck.net/comments_42.xml'

try:
    print("Retrieving", serviceurl)
    fil = urllib.request.urlopen(serviceurl)
    data = fil.read()
    print('Retrieved', len(data), 'characters')
    tree = ET.fromstring(data)
    lst = tree.findall('comments/comment')
    print('Comments: ', len(lst))
    total = 0
    for item in lst:
        num = item.find('count').text
        total += int(num)
    print('Total:', total)
except:
    print("Huston, we've got a problem")
