import re


numberRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = numberRegex.search('405-555-9987')
print(mo.group())

