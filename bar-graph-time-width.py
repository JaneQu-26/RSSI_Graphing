from  pathlib import Path
import json
import matplotlib.pyplot as plt
from datetime import datetime

with open("bledoubt_log_a.json", "r") as f:
        data = json.load(f)
with open("gt_macs.json", "r") as f:
        datasus = json.load(f)
setsus = datasus["bledoubt_log_a.json"]


def make_rssi():
    mac = []
    rssi = []
    
    
    detection = data['detections']
        
    for entry in detection:
        mac.append(entry['mac'])
        rssi.append(entry['rssi'])

    return mac, rssi

def time():
    w = []
    mac, rssi = make_rssi()
    fmac = list(set(mac))
    arssi = []
    for i in fmac:
        r = 0
        for e in mac:
            if i == e:
                r = r + rssi[mac.index(e)]
                next
            else:
                next
        w.append(mac.count(i))
        arssi.append(r/w[fmac.index(i)])
   
    return fmac, arssi, w

def long():    
    macsus, rssisus, wsus, macsafe, rssisafe, wsafe = findsus()
    for i in wsafe:
        if i < 60:
            wsafe.remove(i)
            macsafe.remove(macsafe[wsafe.index(i)])
            rssisafe.remove(rssisafe[wsafe.index(i)])
        else:
            next
    return macsafe, rssisafe, wsafe

 
def findsus():
    macsus = []
    rssisus = []
    wsus = []
    macsafe = []
    rssisafe = []
    wsafe = []
    fmac, arssi, w = time()
    for i in fmac:
         for e in setsus:
                if i == e:
                    macsus.append(i)
                    rssisus.append(arssi[fmac.index(i)])
                    wsus.append(w[fmac.index(i)])
                else:
                    macsafe.append(i)
                    rssisafe.append(arssi[fmac.index(i)])
                    wsafe.append(w[fmac.index(i)])
    print(macsus, rssisus, wsus, macsafe, rssisafe, wsafe)
    return macsus, rssisus, wsus, macsafe, rssisafe, wsafe
    




def main():
    macsus, rssisus, wsus, macsafe, rssisafe, wsafe  = findsus()
    macsafe, rssisafe, wsafe = long()

    
    sorted_pairs = sorted(zip(macsafe, rssisafe), key=lambda x: x[0])
    macsafe,rssisafe = zip(*sorted_pairs)
    plt.xticks([])
    plt.plot(wsafe, rssisafe, color="yellow", edgecolor='black', linewidth=1.5)
    plt.ploy(wsus, rssisus, color="blue", edgecolor='black', linewidth=1.5)
    plt.title('RSSI Strength')
    plt.xlabel('MAC Address')
    plt.ylabel('RSSI')
    plt.show()
    
if __name__ == "__main__":
    main()
