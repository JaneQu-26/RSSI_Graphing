import json
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import sys

def openfile(filename1, filename2, filename3):
    with open(filename1, "r") as f:
        data1 = json.load(f)
    with open(filename2, "r") as d:
        data2 = json.load(d)
    with open(filename3, "r") as j:
        data3 = json.load(j)
    with open("gt_macs.json", "r") as g:
        datasus = json.load(g)
    setsus1 = datasus[filename1]
    setsus2 = datasus[filename2]
    setsus3 = datasus[filename3]
    return data1, data2, data3, setsus1, setsus2, setsus3

#note: change function to takes in variable
def make_rssi(data):
    mac = []
    rssi = []
    time = []

    detection = data['detections']
        
    for entry in detection:
        mac.append(entry['mac'])
        rssi.append(entry['rssi'])

        timestamp_str = entry['t']
        timestamp_str_clean = timestamp_str[11:19]
        timestamp = datetime.strptime(timestamp_str_clean, "%H:%M:%S")

        time.append(timestamp)
    print(time)
    return mac, rssi, time


#note: change function to takes in variable
def sort(mac, rssi, time):
    
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
         
#note: change function to takes in variable
def findsus(setsus, fmac, arssi, atime):
    macsus = []
    rssisus = []
    timesus = []
    macsafe = []
    rssisafe = []
    timesafe = []


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

    return macsus, rssisus, timesus
    
#note: change function to takes in variable
# new plot function to simplify main()    
def plot(data, setsus, color1):
    mac, rssi, time = make_rssi(data)
    fmac, arssi, atime = sort(mac, rssi, time)
    macsus, rssisus, timesus, = findsus(setsus, fmac, arssi, atime)

    plt.plot(timesus[0], rssisus[0], color=color1, label=("Suspicious Devices", len(macsus)))

    for i in range(len(macsus)):
        sorted_pairs = sorted(zip(timesus[i], rssisus[i]), key=lambda x: x[0])
        timesus_paired, rssisus_paired = zip(*sorted_pairs)
        plt.plot(timesus_paired, rssisus_paired, color=color1)
        


def main():
    if len(sys.argv) < 4:
        print("Usage: python3 time-of-day.py <file1> <file2> <file3>")
        return
    filename1 = sys.argv[1]
    filename2 = sys.argv[2]
    filename3 = sys.argv[3]
    data1, data2, data3, setsus1, setsus2, setsus3 = openfile(filename1, filename2, filename3)

    plt.rc('legend',fontsize=15)
    plt.figure(figsize=(12, 6))
    plt.xticks(rotation=45)
    plt.title('RSSI Strength from Three Files')
    plt.xlabel('Time')
    plt.ylabel('RSSI')
    plot(data1, setsus1, "blue")
    plot(data2, setsus2, "indigo")
    plot(data3, setsus3, "purple")

    plt.legend()
    plt.tight_layout()
    plt.show()
    
if __name__ == "__main__":
    main()

