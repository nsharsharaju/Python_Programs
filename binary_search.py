def BS(arr,l,r,x):
    if r>=l:
        mid = l+(r-l)//2

        if x==arr[mid]:
            return mid
        elif x<arr[mid]:
            return BS(arr,l,mid-1,x)
        else:
            return BS(arr,mid+1,r,x)
    else:
        return -1


arr1 = [2,3,5,6]

print(BS(arr1,0,len(arr1)-1,6))