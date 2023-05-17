# An example on displaying a calendar and changing the first weekday from Monday(default) to Sunday
import calendar

calendar.setfirstweekday(calendar.SUNDAY)
# This is the exact same line of code as the one above as "calendar.SUNDAY = 6"
calendar.setfirstweekday(6)

calendar.prmonth(2020, 12)