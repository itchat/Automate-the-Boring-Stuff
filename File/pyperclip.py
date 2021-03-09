import re, pyperclip

# 423-322-2323, 121-1212, (322) 121-1212, 244-4545 ext 12345, ext. 12345, x12345
phoneRegex = re.compile(r'''
(
((\d\d\d) | (\(\d\d\d\)))? # optional area code \( and \) with ?
(\s|-) # first separator it might just be a blank
\d\d\d # first three digits 
- # separator
\d\d\d\d # last four digits
(((ext (\.)?\s)|x) # extra word part
(\d{2,5}))? #extra number part 
)
''',re.VERBOSE)

text = pyperclip.paste()

extractedPhone = phoneRegex.findall(text)

allPhone = []
for phoneRegex in extractedPhone:
    allPhone.append(phoneRegex[0])

result = '\n'.join(allPhone)
pyperclip.copy(result)
