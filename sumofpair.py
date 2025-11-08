num = [3,4,6,7,1]

for i in range(len(num)):
    for j in range(1,len(num)):
        if num[i]+num[j]==7:
            print(num[i],num[j])