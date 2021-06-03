- Python code to remove HTML tags from a string
```
# Using a regex, you can clean everything inside <> :

import re

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext
```
