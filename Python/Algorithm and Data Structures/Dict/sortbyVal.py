
import collections


# def sort_by_val():

#     pass

numDict = {"a":2,"b":1,"c":3}

sorted_vals = sorted(numDict.values())

sorted_dict = {}

# for i in sorted_vals:
#     for k in numDict.keys():
#         if numDict[k] == i:
#             sorted_dict[k] = i

# print(sorted_dict)

sorted_keys = sorted(numDict, key=numDict.get)

for k in sorted_keys:
    sorted_dict[k] = numDict[k]

print(sorted_dict)

