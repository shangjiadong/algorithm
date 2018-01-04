"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
"""

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []
        if len(intervals) == 1:
            return intervals
        else:
            intervals = sorted(intervals, key = lambda x: x.start)
            stack = [intervals[0]]
            for idx in range(1, len(intervals)):
                if intervals[idx].start <= stack[-1].end and intervals[idx].end >= stack[-1].end:
                    stack[-1].end = intervals[idx].end
                if intervals[idx].start <= stack[-1].end and intervals[idx].end <= stack[-1].end:
                    stack[-1] = stack[-1]
                else:
                    stack.append(intervals[idx])
            return stack
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervalsNew = intervals
        intervalsNew.append(newInterval)
        return self.merge(intervalsNew)

def stringToInterval(input):
    tokens = json.loads(input)
    return Interval(tokens[0], tokens[1])

def stringToIntervalArray(input):
    intervalArrays = json.loads(input)
    nodes = []
    for intervalArray in intervalArrays:
        nodes.append(stringToInterval(json.dumps(intervalArray)))
    return nodes

def intervalToString(interval):
    return "[{}, {}]".format(interval.start, interval.end)

def intervalArrayToString(intervalArray):
    serializedIntervals = []
    for interval in intervalArray:
        serializedInterval = intervalToString(interval)
        serializedIntervals.append(serializedInterval)
    return "[{}]".format(', '.join(serializedIntervals))

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            intervals = stringToIntervalArray(line)
            line = lines.next()
            newInterval = stringToInterval(line)
            
            ret = Solution().insert(intervals, newInterval)

            out = intervalArrayToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()