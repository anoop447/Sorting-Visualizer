import time

def merge_sort(data, drawData, timeTick):
    merge_sort_alg(data, 0, len(data)-1, drawData, timeTick)


def merge_sort_alg(data, left, right, drawData,timeTick):
    if left < right:
        middle = (left+right)//2
        merge_sort_alg(data, left, middle, drawData, timeTick)
        merge_sort_alg(data, middle+1, right, drawData, timeTick)
        merge(data, left, middle, right, drawData, timeTick)

def merge(data, left, middle, right, drawData,timeTick):
    leftPart = data[left:middle+1]
    rightPart = data[middle+1:right+1]

    leftIndx = rightIndx = 0

    for dataIndx in range(left, right+1):
        if leftIndx < len(leftPart) and rightIndx < len(rightPart):
            if leftPart[leftIndx] <= rightPart[rightIndx]:
                data[dataIndx] = leftPart[leftIndx]
                leftIndx+=1
            else:
                data[dataIndx] = rightPart[rightIndx]
                rightIndx+=1
        
        elif leftIndx < len(leftPart):
            data[dataIndx] = leftPart[leftIndx]
            leftIndx+=1

        else:
            data[dataIndx] = rightPart[rightIndx]
            rightIndx+=1

    drawData(data, ['green' if x>=left and x <= right else 'red' for x in range(len(data))])
    time.sleep(timeTick)



