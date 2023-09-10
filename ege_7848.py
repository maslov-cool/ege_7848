with open('17_7848.txt') as f:
    A = [int(i) for i in f]
sum_min = sum(
    [int(i) for i in str(min(filter(lambda x: [int(i) for i in str(x)] == sorted([int(i) for i in str(x)])[::-1]
                                              and len([int(i) for i in str(x)]) == len(set([int(i) for i in str(x)])),
                                    A)))])
B = []
for i in range(len(A) - 1):
    s = ([int(i) for i in str(A[i])] == sorted([int(i) for i in str(A[i])])
                                              and len([int(i) for i in str(A[i])]) == len(set([int(i) for i in str(A[i])])))\
        + ([int(i) for i in str(A[i + 1])] == sorted([int(i) for i in str(A[i + 1])])
                                              and len([int(i) for i in str(A[i + 1])]) == len(set([int(i) for i in str(A[i + 1])])))
    if s == 1 and A[i] * A[i + 1] % sum_min == 0:
        B.append(A[i] + A[i + 1])
print(len(B), min(B))



