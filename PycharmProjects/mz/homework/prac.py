import re
data='<content>aaaa<content>'
a=re.match(r'<content>(.*)<content>',data)
print(a.group(1))