sum=0
prices=[7,1,5,3,6,4]
for i in  range(1,len(prices)):
    if prices[i]>prices[i-1]:
        sum+=prices[i]-prices[i-1]
print(sum)
