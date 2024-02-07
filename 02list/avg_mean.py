def avg_mean(lst):
    sum = 0
    for ele in lst:
        sum += ele
    n = len(lst)
    return sum/n

print(avg_mean([12, 13, 14]))



def average(lst):
    return sum(lst)/len(lst)


print(average([12, 15, 17]))