def insertion_sort(input):
    n = len(input)
    for i in range(1,n):
        key = input[i]
        j = i-1
        while j>=0 and key<input[j]:
            (input[j+1],input[j]) = (input[j],key)
            j-=1

L = [5,4,3,2,1]
insertion_sort(L)
print(L)


