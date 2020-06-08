import time

def insertion_sort(data,drawData,timeTick):

    for i in range(len(data)):
        j=i

        while j>0 and data[j-1] > data[j]:
            data[j-1],data[j] = data[j],data[j-1]
            j-=1
            drawData(data, ['green' if x==j or x==j+1 else 'red' for x in range(len(data))])
            time.sleep(timeTick)
    drawData(data, ['green' for x in range(len(data))])
