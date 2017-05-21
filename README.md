# urlSummary

Implementation of pyteaser

$ sudo pip install pyteaser


```
import re
from pyteaser import SummarizeUrl
url = raw_input('\nEnter url to be summarized:\n')
print ('\nSummarizing... \n')
summaries = SummarizeUrl(url)
print ('The Summary:\n')
print summaries
print ('\n')
print ('Done. \n')
```
