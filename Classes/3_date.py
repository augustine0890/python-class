def other_method(val):
    print(f"other_method: {val}")

class Date:
    total = 0
    
    def __init__(self, Year, Month, Day):
        self.year = Year
        self.month = Month
        self.day = Day
        Date.total += 1

    def __str__(self):
        return "Date({}, {}, {})".format(self.year, self.month, self.day)

    def set_date(self, y, m, d):
        self.year = y
        self.month = m
        self.day = d
    
    @classmethod
    def get_total(cls):
        print(cls)
        return cls.total

    @classmethod
    def from_str(cls, date_str):
        """
        d = Date.from_str('2020-11-20')
        """
        print(f"from_str: {cls}")
        year, month, day = map(int, date_str.split('-'))

        other_method(43)

        if cls.is_valid_date(year, month, day):
            return cls(year, month, day)
        else:
            raise Exception("Invalid date")

    @staticmethod
    def is_valid_date(year, month, day):
        if 0 <= year <= 3000 and 1 <= month <= 12 and 1 <= day <= 31:
            return True
        else:
            return False


d1 = Date(2020, 7, 12)
print(d1)
print(Date.get_total())
print(Date.total)

print("-----" * 5)
d2 = Date(2020, 7, 15)
print(d2)
print(Date.get_total())
print(Date.total)

print("-----" * 5)
dd = Date.from_str('2020-12-25')
print(dd)
print(Date.is_valid_date(2020, 7, 20))
print(Date.is_valid_date(2020, 7, 32))

print("-----" * 5)
test = Date.from_str('2020-14-23')