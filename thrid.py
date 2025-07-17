from  pathlib import Path
import json
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np


with open("bledoubt_log_a.json", "r") as f:
        data = json.load(f)
with open("gt_macs.json", "r") as f:
        datasus = json.load(f)
setsus = datasus["bledoubt_log_a.json"]


def make_rssi():
    mac = []
    rssi = []
    time = []
    
    detection = data['detections']
        
    for entry in detection:
        mac.append(entry['mac'])
        rssi.append(entry['rssi'])
        timestamp_str = entry['t'][:-8]

        timestamp = datetime.strptime(timestamp_str, "%a %B %d %H:%M:%S ")

        time.append(timestamp)
    return mac, rssi, time

def sort():
    mac, rssi, time = make_rssi()
    fmac = list(set(mac))
    arssi = []
    for i in fmac:
        r = []
        for e in mac:
            if i == e:
                r.append(rssi[mac.index(i)])
        arssi.append(r)

    print(fmac, arssi, time)
    return fmac, arssi, time
         

def findsus():
    macsus = []
    rssisus = []
    timesus = []
    macsafe = []
    rssisafe = []
    timesafe = []
    fmac, arssi, time = sort()
    for i in fmac:
         for e in setsus:
                if i == e:
                    macsus.append(i)
                    rssisus.append(arssi[fmac.index(i)])
                    timesus.append(time[fmac.index(i)])
                else:
                    macsafe.append(i)
                    rssisafe.append(arssi[fmac.index(i)])
                    timesafe.append(time[fmac.index(i)])
    return macsus, rssisus, timesus, macsafe, rssisafe, timesafe
    




def main():
    macsus, rssisus, timesus, macsafe, rssisafe, timesafe = findsus()

    sorted_pairs = sorted(zip(timesafe, rssisafe), key=lambda x: x[0])
    timesafe,rssisafe = zip(*sorted_pairs)
    plt.xticks([])
    
    
    plt.plot(timesafe, rssisafe)
    plt.plot(timesus, rssisus)

    plt.title('RSSI Strength')
    plt.xlabel('MAC Address')
    plt.ylabel('RSSI')
    plt.show()
    
if __name__ == "__main__":
    main()
