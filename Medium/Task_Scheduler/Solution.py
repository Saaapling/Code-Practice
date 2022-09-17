from collections import defaultdict
import queue
from re import T
from collections import Counter

class Solution:

    """
        Problem: https://leetcode.com/problems/task-scheduler/
        Time Taken: ad infinity (for optimal solution)
        Comments: 
            - Naive Solution: Iteration -> high to low
                - Iterate through the list and make a tally of task counts
                - Store tallies as tuples (count, remaining_cooldown)
                - Result: Time Out - Too Slow
                    - Max 26 different tasks (if this was not a constraint, could use a seg-tree for optimization)
                    - Possble optimizations: binary-tree for tasks, queue for cooldown
            - Improved Solution: Heap + Queue
                - I am faily confident that this solution works, and is a general improvment, but it times out
                - Time complexity: O(nlogn)
                - Many expensive operations moving around the heap and queue
                - In worse case scenarios (n is large (>26)), there are many wasted operations that lead to slow runtimes
            - Optimal Solution: Math
                - Consider the splitting the task list into unique rows of tasks > n
                - The minimum number of rows is the number of times the most frequent task appears
                    - The total time spend is then (approximately) (n+1) * freq_max + length of last row
                    - The above equation's 'n+1' can change is n is sufficiently small such that there are multiple tasks with frequency >= 'n+1'
                    - The 'remaining' can be caluated as such. Take the full square without the last row (n+1) * (max_freq-1, take the remaining
                            empty slots (not filled by max_freq) and subtract the remaining elements from that total
                        - If there are more slots in that square, take that square as the size, otherwise, take the remaining. 
                        - The rational for taking the remaining is that after the square is completed, extra elements can be tacked on
                                any row of that square without breaking any rules, and there will never be an instance where an extra row is needed,
                                since the number of rows the the max_freq of the task list    
    """
    tasks_processed = 0

    def naive_solution(self, tasks, n):
        task_dict = defaultdict(lambda: [0,0])

        for task in tasks:
            task_dict[task][0] += 1

        # Iterate and execute
        index = 0
        time = 0
        while index < len(tasks):
            max = 0
            next_task = "IDLE"
            for task in task_dict:
                if task_dict[task][0] > max and task_dict[task][1] == 0:
                    max = task_dict[task][0]
                    next_task = task

                if task_dict[task][1] > 0:
                    task_dict[task][1] -= 1

            # print(next_task)
            if next_task != "IDLE":
                index += 1
                task_dict[next_task][0] -= 1
                task_dict[next_task][1] += n

            time += 1

        return time

    def heap_and_queue(self, tasks, n):
        task_count = defaultdict(lambda: 0)
        task_wait = defaultdict(lambda: 0)
        for task in tasks:
            task_count[task] += 1

        task_heap = [0]

        def add(n):
            if n[0] == 'null':
                return

            index = len(task_heap)
            task_heap.append(n)
            while index > 1 and task_count[n] > task_count[task_heap[index >> 1]]:
                task_heap[index] = task_heap[index >> 1]
                index >>= 1
                task_heap[index] = n

        def pop():
            if len(task_heap) == 2:
                self.tasks_processed += 1
                return task_heap.pop()

            temp = task_heap[1]
            task_heap[1] = task_heap.pop()

            index = 1
            while (index << 1) < len(task_heap) and task_count[task_heap[index]] < task_count[task_heap[index << 1]]:
                temp = task_heap[index]
                task_heap[index] = task_heap[index<<1]
                index <<= 1
                task_heap[index] = temp

            self.tasks_processed += 1
            return temp

        for task in task_count:
            add(task)

        time = 0
        wait_queue = []
        while self.tasks_processed < len(tasks):
            # print(task_heap)
            # print(wait_queue)
            if len(task_heap) > 1:
                task = pop()
                task_count[task] -= 1
                if task_count[task] > 0:
                    task_wait[task] = n
                    wait_queue.append(task)

            i = 0
            while i < len(wait_queue):
                task_wait[task] -= 1
                if task_wait[task] == 0:
                    wait_queue.pop(i)
                    add(task)
                else:
                    i += 1

            time += 1

        return time

    def mathSolution(self, tasks, n):
        task_counts = Counter(tasks)
        max_freq = max(task_counts.values())
        max_freq_count = 0
        for task in task_counts:
            if task_counts[task] == max_freq:
                max_freq_count += 1

        if (n+1) >= max_freq_count:
            row_length = n+1
        else:
            row_length = max_freq_count


        # Add the garunteed first elements of each row
        time = max_freq * max_freq_count
        
        remaining = len(tasks) - (max_freq*max_freq_count)
        if (max_freq - 1) * (row_length-max_freq_count) > remaining:
            time += (max_freq - 1) * (row_length-max_freq_count)
        else:
            time += remaining

        return time

    def leastInterval(self, tasks: list[str], n: int) -> int:
        return self.mathSolution(tasks, n)
        

test = Solution()
input = ["A","A","A","B","B","B"]
n = 2
result = test.leastInterval(input, n)
print(result)