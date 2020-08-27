# Python3 program to Grouping list
# elements based on frequency
from collections import OrderedDict


def group_list(lst):
	res = [(el, lst.count(el)) for el in lst]
	return list(OrderedDict(res).items())


# Driver code
lst = [1, 3, 4, 4, 1, 5, 3, 1]
print(group_list(lst))

#listcount and orderedDict

