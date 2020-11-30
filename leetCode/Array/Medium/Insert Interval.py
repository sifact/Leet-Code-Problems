import bisect


def insert(intervals, newInterval):
    bisect.insort(intervals, newInterval)
    print(intervals)
    i = 0
    while i < len(intervals) - 1:
        if intervals[i][1] >= intervals[i + 1][0]:
            intervals[i][1] = max(intervals[i][1], intervals[i + 1][1])
            intervals.remove(intervals[i + 1])
        else:
            i += 1
    return intervals


a = []
for _ in range(int(input())):
    a.append(list(map(int, input().split())))
newA = list(map(int, input().split()))

print(insert(a, newA))
