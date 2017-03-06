class Interval(object):
	def __init__(self,start,end):
		self.start = start
		self.end = end

class Solution:
	def insert(self,intervals,newInterval):
		results = []
		flag = False
		for x in intervals:
			if not flag:
				if newInterval.end < x.start:
					results.append(newInterval)
					results.append(x)
					flag = True
				elif x.end < newInterval.start:
					results.append(x)
				elif newInterval.start <= x.start and newInterval.end <= x.end:
					results.append(Interval(newInterval.start,x.end))
					flag = True
				elif newInterval.start >= x.start and newInterval.end <= x.end:
					results.append(x)
					flag = True
				elif newInterval.end > x.end:
					results.append(Interval(x.start if x.start < newInterval.start else newInterval.start,newInterval.end))
					flag = True
			else:
				lastInterval = results[-1]
				if lastInterval.end >= x.start:
					lastInterval.end = (x.end if x.end > lastInterval.end else lastInterval.end)
				else:
					results.append(x)
		if not flag:
			results.append(newInterval)

		
		return results

solution = Solution()
results = solution.insert()



   