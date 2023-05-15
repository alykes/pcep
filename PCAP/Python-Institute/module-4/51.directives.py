# Quick example on how to use directives when displaying the date
from datetime import date

d = date(2020, 1, 4)
print(d.strftime('%Y/%m/%d'))
