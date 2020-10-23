# counting sundays
# 1 Jan 1900 - Monday (numeration - from 0 - of week starts at Sun)
weekdays = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

months = {"Jan": 31, "Feb": 28, "Mar": 31, "Apr": 30, "May": 31, "Jun": 30, "Jul": 31, "Aug": 31, "Sep": 30, "Okt": 31, "Nov": 30, "Dec": 31}
months_leap = {"Jan": 31, "Feb": 29, "Mar": 31, "Apr": 30, "May": 31, "Jun": 30, "Jul": 31, "Aug": 31, "Sep": 30, "Okt": 31, "Nov": 30, "Dec": 31}
month_names = list(months.keys())

from modulo import Modulo

class Date:
    def __init__(self):
        self.weekday = Modulo(7, 1)
        self.year = 1900

    def __repr__(self):
        return weekdays[self.weekday.value] + " " + str(self.year)

    def isSUN(self):
        if self.weekday == Modulo(7, 0): return True
        else: return False

    def isLeapYear(self):
        if self.year % 4 == 0:
            if self.year % 100 == 0:
                if self.year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    def countSundays(self):
        for mon in months:   # 1900 is not a leap year and not part of the 20th century
            self.weekday.add(months[mon])
        self.year += 1
        # now in the 20th century
        count = 0
        print(self)
        if self.isSUN(): count += 1
        for i in range(100):
            if not self.isLeapYear():
                for mon in months:
                    self.weekday.add(months[mon])
                    if self.isSUN():
                        count +=1
                        print(month_names[Modulo(12, month_names.index(mon)).add(1).value]+ ": ", self)
            else:
                for mon in months_leap:
                    self.weekday.add(months_leap[mon])
                    if self.isSUN():
                        count +=1
                        print(month_names[Modulo(12, month_names.index(mon)).add(1).value]+ ": ", self)
            self.year += 1
        return count

d = Date()
print(d.countSundays())
print(month_names[Modulo(12, 10).add(1).value])
