import datetime, os, webuntis.objects, random, getpass

from dotenv import load_dotenv
from prettytable import PrettyTable

load_dotenv()
SRV = os.getenv('SRV')
USR = os.getenv('USR')
PWD = os.getenv('PWD')
SHO = os.getenv('SHO')
USRA = os.getenv('USRA')
STS = os.getenv('STS')

s = webuntis.Session(
        server=SRV,
        username=USR,
        password=PWD,
        school=SHO,
        useragent=USRA
    )

s.login()

print("TBZ Mitte DoorSign Server v0.1\nby ingressy\n")
time = datetime.datetime.now()
chtime = (time.strftime("%H%M"))
chdate = (time.strftime("%Y-%m-%d"))
choose = "2.311"
#choose = input("From which room would you like to have the timetable? ")
#chtime = input("What time is it? ")
start = datetime.datetime.now()
end = start + datetime.timedelta(days=4)

rooms = s.rooms().filter(name=choose)

tt = s.timetable(room=rooms[0], start=start, end=end)
tt = sorted(tt, key=lambda x: x.start)
#print(tt)

time_format_end = "%H%M"
time_format_start = "%Y-%m-%d " + time_format_end

for po in tt:
    s = po.start.strftime(time_format_start)
    e = po.end.strftime(time_format_end)
    k = " ".join([k.name for k in po.klassen])
    t = " ".join([t.name for t in po.teachers])
    r = " ".join([r.name for r in po.rooms])
    sub = " ".join([r.name for r in po.subjects])
    c = "(" + po.code + ")" if po.code is not None else ""

    if chtime < e:
        print(s + "-" + e, k, sub, t, r, c)
