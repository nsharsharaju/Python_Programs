def bubble_sort(input):
    n = len(input)
    for i in range(n):
        for j in reversed(range(n-1)):
            if(input[j]>input[j+1]):
                (input[j],input[j+1]) = (input[j+1],input[j])


L = [5,4,3,2,1]

bubble_sort(L)

print(L)

