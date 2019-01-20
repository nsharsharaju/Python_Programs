def selection_sort(input):
    n = len(input)

    for i in range(n-1):
        min_index = i

        for j in range(i+1,n):
            if input[min_index]>input[j]:
                min_index = j

        (input[i],input[min_index]) = (input[min_index], input[i])


L = [5,4,3,2,1,5,6,5]



selection_sort(L)

print(L)