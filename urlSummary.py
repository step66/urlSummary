import re
from pyteaser import SummarizeUrl
url = raw_input('\nEnter url to be summarized:\n')
print ('\nSummarizing... \n')
summaries = SummarizeUrl(url)
print ('The Summary:\n')
print summaries
print ('\nDone. \n')

