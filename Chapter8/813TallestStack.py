import unittest
from functools import reduce

def tallest_stack(boxes):
    boxes.sort(reverse=True)
    def tallest_for_bottom(cur_stack, cur_box_idx):
        if cur_box_idx == len(boxes):
            return reduce(lambda x,y: x+y.height, cur_stack, 0)
        else:
            if (cur_stack[-1].height > boxes[cur_box_idx].height and
                cur_stack[-1].width > boxes[cur_box_idx].width and
                cur_stack[-1].depth > boxes[cur_box_idx].depth):
                return tallest_for_bottom(cur_stack+[boxes[cur_box_idx]],
                                          cur_box_idx+1)
            else:
                return tallest_for_bottom(cur_stack,
                                          cur_box_idx+1)
    largest_height = 0
    for i in range(len(boxes)):
        largest_height = max(largest_height,
                             tallest_for_bottom([boxes[i]], i+1))
    return largest_height

class Box:
    def __init__(self, height, width, depth):
        self.height = height
        self.width = width
        self.depth = depth

    def __lt__(self, other):
        return self.height < other.height

    def __eq__(self, other):
        return self.height == other.height

class TestSuite(unittest.TestCase):
    def test_null(self):
        self.assertEqual(tallest_stack([]), 0)

    def test_single_box(self):
        self.assertEqual(tallest_stack([Box(3,2,1)]), 3)

    def test_two_conflicting_boxes(self):
        self.assertEqual(tallest_stack([Box(3,2,1), Box(5,4,1)]), 5)

    def test_two_stackable_boxes(self):
        self.assertEqual(tallest_stack([Box(3,2,1), Box(6,5,4)]), 9)

if __name__ == '__main__':
    unittest.main()
