
def getMedian(arr1,arr2,n):
    # if arr1[n-1]<arr2[0]:
    #     return (arr1[n-1]+arr2[0])/2;
    # elif arr2[n-1]<arr1[0]:
    #     return (arr2[n - 1] + arr1[0]) / 2;
    # else:
    #     if (arr1[0]<arr2[0]):
    #         start=0;
    #         end=n-1
    #
    #         while(start<end):
    #             mid = int((start + end) / 2)
    #             if arr1[mid]<arr2[0]:
    #                 print("x")
    #                 return (arr1[mid] + arr2[0]) / 2;
    #             end=mid
    #     else:
    #         start = 0;
    #         end = n - 1
    #         while (start < end):
    #             mid = int((start + end) / 2)
    #             if arr2[mid] < arr1[0]:
    #
    #                 return (arr2[mid] + arr1[0]) / 2;
    #             end = mid
    # x=0
    # start1=0
    # end1=n-1
    # start2=0
    # end2=n-1
    # if arr1[end1] < arr2[start2]:
    #     return arr1[end1] + arr2[start2] / 2
    #     return arr2[end2] + arr1[start1] / 2
    #
    # while(True):
    #     mid1=int((end1-start1)/2)    # elif arr2[end2] < arr1[start1]:

    #     mid2 = int((end2 - start2) / 2)
    #     print("mid1= ",mid1)
    #     print("mid2= ",mid2)
    #     if arr1[mid1]<arr2[start2]:
    #         x=x+(mid1-start1)
    #         if x==n-1:
    #
    #             return int((arr1[mid1]+arr2[start2])/2)
    #         print("here")
    #         start1=mid1
    #     else:
    #         x=x+(mid2-start2)
    #         if x==n-1:
    #             print("mid2= ",arr2[mid2],"start1= ",arr1[start1], "x= ",x,"  start1=",start1)
    #             return int((arr2[mid2]+arr1[start1])/2)
    #         start2=mid2

    if n==0:
        return -1

    if n==1:
        return int((arr1[0]+arr2[0])/2)

    if n==2:
        return int((max(arr1[0],arr2[0])+min(arr1[1],arr2[1]))/2)

    m1=Median(arr1,n)
    m2=Median(arr2,n)

    if m1>m2:
        if n%2 is 0:
            return getMedian(arr1[:int(n/2)+1],arr2[int(n/2)-1:],int(n/2)+1)
        else:
            return getMedian(arr1[:int(n/2)+1],arr2[int(n/2):],int(n/2)+1)
    else:
        if n%2 is 0:
            return  getMedian(arr1[int(n/2-1):],arr2[:int(n/2+1)],int(n/2)+1)
        else:
            return getMedian(arr1[int(n/2):],arr2[:int(n/2)+1],int(n/2)+1)


def Median(arr,n):

    if n%2==0:
        return (arr[int(n / 2)] + arr[int(n / 2) - 1]) / 2
    else:
        return arr[int(n/2)]



if __name__=="__main__":
    arr1 = [1, 2, 3, 6]
    arr2 = [4, 6, 8, 10]
    n = len(arr1)
    print(int(getMedian(arr1, arr2, n)))