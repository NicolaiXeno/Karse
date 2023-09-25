
from labquest import LabQuest
import logging
# import time
# import csv
logging.basicConfig()
logging.getLogger("labquest").setLevel(logging.INFO)

lq = LabQuest()
print(lq.open())
lq.select_sensors(ch1='Light 1 lux')

'''
with open('energidrikk.csv','w') as csvfile:
    # fieldnames = ['tid', 'lux']
    writer = csv.writer(csvfile, delimiter=',')
    

    


    s = 1000 #ms til sekund
    minutt = s*60 #min kan ikke brukes som variabelnavn
    # h = minutt*60
    # dag = h*24

    lq.start(s*4)
    print("start")
    print(lq.sensor_info("ch1"))

    list = []

    for i in range(10):
        data = lq.read("ch1",0)
        list.append(data)
    writer.writerow(list) #data)

    # print(list)


    lq.stop()
    lq.close()
'''
lq.stop()
lq.close()