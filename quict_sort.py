


def quict_sort(alist, start, last):

    if start >= last:
        return


    mid_value = alist[start]
    low = start
    high = last
    while low<high:

        while low<high and alist[high]>=mid_value:
            high -= 1
        alist[low] = alist[high]
        
        while low<high and alist[low]<mid_value:
            low += 1

        alist[high] = alist[low]
    alist[low] = mid_value

    quict_sort(alist, start, low-1)

    quict_sort(alist, low+1, last)

if __name__ == '__main__':
    a = [0,4,5,8,6,4,7,9,1,0]
    quict_sort(a, 0, len(a)-1)
    print(a)
