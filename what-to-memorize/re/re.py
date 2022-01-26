import re

text = "010-1!!((234-1*!$@243"
# text = re.sub(r'[!!((*!$@]', '', text)
text = re.sub(r'[^0-9-]', '', text)
# return 값은 문자열
print(text)
