
class datehelpers:
    @classmethod
    def date_diff(cls, date1, date2, units):
        '''return the difference between date1 and date2 in the requested units where:
            date1 and date2 are instances of datetime
            units is a string in ('days','months','years')'''
        conversions = { 'days': 1, 'months': 30.4, 'years': 365.25 }
        return (abs((date2 - date1).days) / conversions[units])

    @classmethod
    def dates_within(cls, date1, date2, limit, units):
        '''return True if date1 and date2 are within limit units where:
            date1 and date2 are instances of datetime
            limit is a number
            units is a string in ('days','months','years')'''
        return datehelpers.date_diff(date1, date2, units) <= limit