import copy

cost = list(map(float, input().split()))  # h, c, a cost of enclosure
Area = list(map(float, input().split()))  # max allotable area
hn, ha = (map(float, input().split()))  # min number and area
cn, ca = (map(float, input().split()))
an, aa = (map(float, input().split()))
ta = round(float(input()))  # zoo area

ma = []
ma.append(round(hn * ha))
ma.append(round(cn * ca))
ma.append(round(an * aa))
ac = ma[0] + ma[1] + ma[2]  # area occupied
tc = ma[0] * cost[0] + ma[1] * cost[1] + ma[2] * cost[2]  # total cost


if ta - ac > Area[cost.index(min(cost))] - ma[cost.index(min(cost))]:
	tc += min(cost) * (Area[cost.index(min(cost))] - ma[cost.index(min(cost))])
	ac += Area[cost.index(min(cost))] - ma[cost.index(min(cost))]
	sc = copy.deepcopy(cost)
	sc.sort()
	if ta - ac > Area[cost.index(sc[1])] - ma[cost.index(sc[1])]:
		tc += sc[1]*(Area[cost.index(sc[1])] - ma[cost.index(sc[1])])
		ac += Area[cost.index(sc[1])] - ma[cost.index(sc[1])]
		tc += max(cost)*(ta - ac)
		print(round(tc))
	else:
		tc += sc[1]*(ta-ac)
		print(round(tc))
else:
	tc += min(cost) * (ta - ac)
	print(round(tc))
