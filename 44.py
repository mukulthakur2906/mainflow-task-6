def largest_histogram_area(heights):
    stack, area = [], 0
    heights.append(0)
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            H = heights[stack.pop()]
            W = i if not stack else i - stack[-1] - 1
            area = max(area, H * W)
        stack.append(i)
    heights.pop()
    return area

def maximal_rectangle(matrix):
    if not matrix:
        return 0
    n = len(matrix[0])
    heights = [0] * n
    max_area = 0
    for row in matrix:
        for i in range(n):
            heights[i] = heights[i] + 1 if row[i] == '1' else 0
        max_area = max(max_area, largest_histogram_area(heights))
    return max_area

if __name__ == "__main__":
    r = int(input("Enter number of rows: "))
    c = int(input("Enter number of columns: "))
    matrix = [input(f"Row {i+1} (0/1 separated by space): ").split() for i in range(r)]
    print("Largest rectangle area:", maximal_rectangle(matrix))
