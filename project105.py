import csv
import math

with open('project105 data.csv','r') as f:#done
    frame = csv.reader(f)
    data = list(frame)
    #print(data)

def mean(data):#done
    datan = data[0]
    sum = 0
    total_count = len(datan)
    for i in range(0,len(datan)):
        sum += float(datan[i])

    mean = sum/total_count
    return mean

def stand_deviate(data, mean):
    #xi is value in data
    sum = 0
    datan = data[0]
    for xi in datan:
        differ = float(xi) - mean
        sqr = differ**2
        sum += sqr#sigma (xi - x)^2
    
    no = len(datan)
    stand = math.sqrt(sum/(no-1))

    return stand

avrg = mean(data)
print("standard devation:",stand_deviate(data,avrg))
print(avrg)