import datetime as DT #importinf datetime


def sun_angle(time):
    start = '06:00' #start hour is 6:00

    t1 = DT.datetime.strptime(time, '%H:%M')  #calculating amount of minutes since start hour till hour provided by user
    t2 = DT.datetime.strptime(start, '%H:%M')

    minutes_since_start = ((t1 - t2).total_seconds() / 60.0)

    if minutes_since_start < 0 or minutes_since_start > 720: #return info about not seeing the sun when it's before 6:00 or after 18:00
        return "I don't see the sun!"
    else:
        return minutes_since_start * 0.25 #else return amounts of minutes * 0.25 (15 degrees == 60 minutes)
