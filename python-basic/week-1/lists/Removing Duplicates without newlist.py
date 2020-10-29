nums=input()
nums[:]=list(OrderedDict.fromkeys(nums))
print(nums)
