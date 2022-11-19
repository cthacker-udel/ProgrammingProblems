
from typing import List


class Box:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth


def boxes(stack: List[Box]) -> int:
    n = len(stack)
    boxes: List[Box] = []
    for eachbox in stack:
        boxes.append(eachbox) ## the box
        boxes.append(Box(min(eachbox.height, eachbox.depth), eachbox.width, max(eachbox.height, eachbox.depth))) ## the box rotated, with width as height, width as min(height, depth) and depth as min(height, depth)
        boxes.append(Box(min(eachbox.height, eachbox.width), eachbox.depth, max(eachbox.height, eachbox.width))) ## the box rotated, with depth as height, width as min(height, width), and depth as min(height, width)
    n *= 3

    boxes.sort(key=lambda b: b.depth * b.width, reverse=True)

    msh = [0] * n

    for i in range(len(msh)):
        msh[i] = boxes[i].height
    
    for i in range(1, n):
        for j in range(0, i):
            if boxes[i].width < boxes[j].width and boxes[i].depth < boxes[j].depth: ## if the current target box's width is less then the subproblem box width, and depth likewise
                if msh[i] < msh[j] + boxes[i].height: ## we can make a taller combination if the current dp target solution is less then the smaller dp solution + the target box height
                    msh[i] = msh[j] + boxes[i].height ## we assign the target problem the result of subproblem j's solution + the target box's height

    return max(msh) ## return the max height, which is the last element in the dp table


if __name__ == '__main__':
    arr = [Box(6, 4, 7), Box(2, 1, 3), Box(5, 4, 6), Box(12, 10, 32)]
    print(boxes(arr))
