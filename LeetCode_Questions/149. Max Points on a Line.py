# Input: points = [[1,1],[2,2],[3,3]]
# Output: 3

# Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4

"""
Approach:
1.
2.
3.
"""

def maxPoints(points):
    maxCount = 0
    points_dict = {}

    for i in range(len(points)-1):
        x1, y1 = points[i][0], points[i][1]
        for j in range(i+1, len(points)):
            x2, y2 = points[j][0], points[j][1]
            try:
                slope = (y2 - y1)/(x2 - x1)  ## (y2-y1)/(x2-x1)
            except:
                slope = "inf"
            if slope in points_dict:
                # # slope_dir = str((x1,y1)) + "-->" + str((x2,y2))
                points_dict[slope].append((x1,y1))
                points_dict[slope].append((x2,y2))
                # cnt = points_dict[slope] + 1
                # points_dict.update({slope:cnt})
            else:
                # slope_dir = str((x1,y1)) + "-->" + str((x2,y2))
                points_dict.update({slope:[(x1,y1),(x2,y2)]})
                # points_dict.update({slope:1})

    print(points_dict)

    for i in points_dict.keys():
        if len(set(points_dict[i])) >= maxCount:
            maxCount = len(set(points_dict[i]))
    
    return maxCount


if __name__ == "__main__":
    points = [[1,1],[2,2],[3,3]]
    print(maxPoints(points))

    points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    print(maxPoints(points))