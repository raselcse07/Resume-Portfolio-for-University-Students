
import datetime

year_dropdown=[]

for y in range(2005,(datetime.datetime.now().year+12)):
    year_dropdown.append((y,y))
