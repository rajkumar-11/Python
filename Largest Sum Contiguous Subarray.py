
def maxSubArraySum(a,len):
    max=a[0]
    max_so_far=a[0]
    start=0
    end=0
    start_max=0
    end_max=0
    for i in range(1,len):
        if max<=0:
            start=i
            end=i
            max=0
        max=max+a[i]
        if max>max_so_far:
            max_so_far=max;
            start_max=start
            end_max=i
    print("max contiguous sum is ",max_so_far)
    print("starting index= ",start_max)
    print("ending index= ",end_max)


if __name__=="__main__":
    a = [-1,-1,-1,-1,-1,-1,-1,3,-2,5,-3,9,4,-12]
    print("Maximum contiguous sum is", maxSubArraySum(a, len(a)))