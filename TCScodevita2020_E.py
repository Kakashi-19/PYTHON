import copy
cost = list(map(int, input().split()))    #h, c, a cost of enclosure
Area = list(map(int, input().split()))    #max allotable area
hn, ha = (map(int, input().split()))      #min number and area
cn, ca = (map(int, input().split()))
an, aa = (map(int, input().split()))
ta = int(input())                         #zoo area

ac = hn*ha + cn*ca + an*aa          #area occupied
tc = hn*ha*cost[0] + cn*ca*cost[1] + an*aa*cost[2]  #total cost

if cost.index(min(cost)) == 0:
	if ta - ac > Area[cost.index(min(cost))] - hn*ha:
		tc += min(cost)*(Area[cost.index(min(cost))] - hn*ha)
		ac += Area[cost.index(min(cost))] - hn*ha
		sc = copy.deepcopy(cost)
		sc.sort()
		tc += (ta - ac) * sc[1]
		print(tc)
			
	else:
		tc += min(cost)*(ta-ac)
		print(tc)

elif cost.index(min(cost)) == 1:
	if ta - ac > Area[cost.index(min(cost))] - cn*ca:
		tc += min(cost) * (Area[cost.index(min(cost))] - cn * ca)
		ac += Area[cost.index(min(cost))] - cn * ca
		sc = copy.deepcopy(cost)
		sc.sort()
		tc += (ta - ac) * sc[1]
		print(tc)
	else:
		tc += min(cost)*(ta-ac)
		print(tc)

elif cost.index(min(cost)) == 2:
	if ta - ac > Area[cost.index(min(cost))] - an*aa:
		tc += min(cost) * (Area[cost.index(min(cost))] - an * aa)
		ac += Area[cost.index(min(cost))] - an * aa
		sc = copy.deepcopy(cost)
		sc.sort()
		tc += (ta - ac) * sc[1]
		print(tc)
	else:
		tc += min(cost) * (ta - ac)
		print(tc)
