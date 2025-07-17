from  pathlib import Path
import json
import matplotlib.pyplot as plt

path = Path(__file__).parent / 'bledoubt_log_a.json'

def read_json():
    with path.open('r') as file:
        data = json.load(file)
    return data

def make_rssi():
    time = []
    rssi = []
    
    with path.open('r') as file:
        data = json.load(file)

    for detection in data['detections']:
            timestamp_str = detection['t']
            timestamp = datetime.strptime(timestamp_str, "%a %b %d %H:%M:%S %Z %Y")

            time.append(timestamp)
            rssi.append(detection['rssi'])
    return time, rssi

def main():
    read
    time, rssi = make_rssi()
    print(time, rssi)
    sorted_pairs = sorted(zip(time, rssi), key=lambda x: x[0])
    time,rssi = zip(*sorted_pairs)
    
    plt.figure(figsize = (12,6))
    plt.plot(time, rssi, linestyle = "-", color="blue")
    plt.xlabel("Time")
    plt.ylabel("RSSI")
    plt.title("RSSI Over Time")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
if __name__ == "__main__":
    main()
