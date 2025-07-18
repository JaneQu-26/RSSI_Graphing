from  pathlib import Path
import json
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

x = input("which file should be look at?")
filename = "bledoubt_log_" + x + ".json"

with open(filename, "r") as f:
        data = json.load(f)
with open("gt_macs.json", "r") as f:
        datasus = json.load(f)
setsus = datasus[filename]


def make_rssi():
    mac = []
    rssi = []
    time = []
    
    detection = data['detections']
        
    for entry in detection:
        mac.append(entry['mac'])
        rssi.append(entry['rssi'])

        timestamp_str = entry['t']
        timestamp_str_clean = " ".join(timestamp_str.split()[:-2] + [timestamp_str.split()[-1]])
        timestamp = datetime.strptime(timestamp_str_clean, "%a %b %d %H:%M:%S %Y")

        time.append(timestamp)
    return mac, rssi, time

def sort():
    mac, rssi, time = make_rssi()
    fmac = list(set(mac))
    arssi = []
    atime = []
    for i in fmac:
        r = []
        t = []
        for idx, e in enumerate(mac):
            if i == e:
                r.append(rssi[idx])
                t.append(time[idx])
        arssi.append(r)
        atime.append(t)


    return fmac, arssi, atime
         

def findsus():
    macsus = []
    rssisus = []
    timesus = []
    macsafe = []
    rssisafe = []
    timesafe = []
    fmac, arssi, atime = sort()
    for i in fmac:
        idx = fmac.index(i)
        if i in setsus:
            macsus.append(i)
            rssisus.append(arssi[idx])
            timesus.append(atime[idx])
        else:
            macsafe.append(i)
            rssisafe.append(arssi[idx])
            timesafe.append(atime[idx])

    return macsus, rssisus, timesus, macsafe, rssisafe, timesafe
    




def main():
    macsus, rssisus, timesus, macsafe, rssisafe, timesafe = findsus()

    
    plt.figure(figsize=(12, 6))
    plt.xticks(rotation=45)
    
    for i in range(len(macsafe)):
        sorted_pairs = sorted(zip(timesafe[i], rssisafe[i]), key=lambda x: x[0])
        timesafe_paired, rssisafe_paired = zip(*sorted_pairs)
        plt.plot(timesafe_paired, rssisafe_paired, color="blue")


    for i in range(len(macsus)):
        sorted_pairs = sorted(zip(timesus[i], rssisus[i]), key=lambda x: x[0])
        timesus_paired, rssisus_paired = zip(*sorted_pairs)

        plt.plot(timesus_paired, rssisus_paired, color="red")

    plt.title('RSSI Strength')
    plt.xlabel('Time')
    plt.ylabel('RSSI')
    plt.show()
    
if __name__ == "__main__":
    main()

