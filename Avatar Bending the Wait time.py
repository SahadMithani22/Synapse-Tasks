#Task 1.4
customers = [[5,2], [5,4], [10,3], [20,1]]
avg = []
finTime = 0


for i in range(len(customers)):
    initTime = customers[i][0]
    makeTime = customers[i][1]

    if initTime > finTime:
        cookTime = initTime
    else: 
        cookTime = finTime
    
    finTime = cookTime + makeTime
    waitTime = finTime - initTime
    avg.append(waitTime)
    
print(avg)
print(sum(avg)/len(avg))

#Output
# [2, 6, 4, 1]
# 3.25