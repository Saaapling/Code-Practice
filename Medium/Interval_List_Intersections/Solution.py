from operator import truediv
from pyexpat import native_encoding
from unicodedata import name


class Solution:

    """
        Problem: https://leetcode.com/problems/interval-list-intersections/
        Time Taken: 40 minutes
        Complexity: O(n), potentially slowed down by expensive function calls and swap operatons

        Improved solution: 
            Rational: There is the idea that the interval with the smallest endpoint can only
                intersect one other interval. Check that interval for intersection, 'discard'
                the original smallest interval, and repeat. 
            Complexity: O(m+n), the same big-O notation, but without any of the expensive swaps
                This solution also avoids having to keep track of state, and the issue of
                repeatedly reassigning existing variables (max_index)
            Space Compexity: O(1)
        
        Comments: For future problems, should try to keep in mind that for leetcode, there usual
            exists an elegant solution, and to think about how to minimize the space-complexity,
            for the two usually go hand in hand. There is still the question of how much time
            to dedicate to thinking about an optimal solution before jumping to the naive implementation
    """

    def check_intersection(self, interval_1, interval_2):
        if interval_1[0] <= interval_2[1]:
            if interval_2[0] <= interval_1[1]:
                return True
        return False

    def swap(self, list_a, list_b, curr_index, other_index, state):
        if state == 1:
            # Search list is currently list_b
            return (list_a, other_index, curr_index)
        else:
            # Search list is current list_a
            return (list_b, other_index, curr_index)

    def naive_traversal(self, first_list, second_list):
        # Check for empty lists
        if len(first_list) == 0 or len(second_list) == 0:
            return []

        # State indicates the current search list 
        if first_list[0][0] < second_list[0][0]:
            state = 1
            curr_interval = first_list[0]
            search_list = second_list
        else:
            state = -1
            curr_interval = second_list[0]
            search_list = first_list

        max_index = len(search_list)
        curr_index = 0
        other_index = 0

        intersections = []
        while curr_index < max_index:
            interval = search_list[curr_index]
            # print(str(interval) + ", " + str(state))

            if self.check_intersection(curr_interval, interval):
                intersections.append([max(curr_interval[0], interval[0]), min(curr_interval[1], interval[1])])

            if interval[1] > curr_interval[1]:
                curr_interval = interval
                search_list, curr_index, other_index = self.swap(first_list, second_list, curr_index, other_index, state)
                max_index = len(search_list)
                state *= -1

            curr_index += 1

        return intersections

    def check_minimum_endpoints(self, list_a, list_b):
        index_a = 0
        index_b = 0

        intersections = []
        while index_a < len(list_a) and index_b < len(list_b):
            max_floor = max(list_a[index_a][0], list_b[index_b][0])
            min_ceiling = min(list_a[index_a][1], list_b[index_b][1])
            if max_floor <= min_ceiling:
                intersections.append([max_floor, min_ceiling])
            if list_a[index_a][1] < list_b[index_b][1]:
                index_a += 1
            else:
                index_b += 1

        return intersections

    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        return self.check_minimum_endpoints(firstList, secondList)

test = Solution()
list_1 = [[0,2],[5,10],[13,23],[24,25], [50,60], [63,74]]
list_2 = [[1,5],[8,12],[15,24],[25,26], [55,63], [70,72]]
result = test.intervalIntersection(list_1, list_2)
print(result)