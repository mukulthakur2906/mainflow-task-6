def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

if __name__ == "__main__":
    n = int(input("Enter number of intervals: "))
    intervals = []
    for i in range(n):
        start, end = map(int, input(f"Interval {i+1} (start end): ").split())
        intervals.append([start, end])
    print("Merged Intervals:", merge_intervals(intervals))
