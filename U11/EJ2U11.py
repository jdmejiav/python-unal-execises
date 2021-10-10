from datetime import datetime


n = int(input())

dic = {
    "true vampires" : 0,
    "early birds" : 0,
    "sunny warmers" : 0,
    "lunch workers" : 0,
    "sunset lovers" : 0,
    "prime timers" : 0
}


for i in range(0,n):
    entrada = input()
    fecha = datetime.strptime(entrada,'%Y-%m-%d %H:%M:%S')
    if fecha.hour >= 0 and fecha.hour < 4:
        dic["true vampires"] += 1
    elif fecha.hour >= 4 and fecha.hour < 8:
        dic["early birds"] += 1
    elif fecha.hour >= 8 and fecha.hour < 12:
        dic["sunny warmers"] += 1
    elif fecha.hour >= 12 and fecha.hour < 16:
        dic["lunch workers"] += 1
    elif fecha.hour >= 16 and fecha.hour < 20:
        dic["sunset lovers"] += 1
    elif fecha.hour >= 20 and fecha.hour < 24:
        dic["prime timers"] += 1

print("true vampires "+str(dic["true vampires"]))
print("early birds "+str(dic["early birds"]))
print("sunny warmers "+str(dic["sunny warmers"]))
print("lunch workers "+str(dic["lunch workers"]))
print("sunset lovers "+str(dic["sunset lovers"]))
print("prime timers "+str(dic["prime timers"]))
