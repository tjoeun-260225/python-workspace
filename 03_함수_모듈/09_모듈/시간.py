import datetime

def 현재시간():
    지금 = datetime.datetime.now()
    return f"{지금.hour}:{지금.minute:02d}"


