from datetime import date

def days_diff(date1, date2):
    """
        Find absolute diff in days between dates
    """
    date1=date(date1[0],date1[1],date1[2])
    date2=date(date2[0],date2[1],date2[2])

    diff=(date1-date2)

    return abs(diff.days)
