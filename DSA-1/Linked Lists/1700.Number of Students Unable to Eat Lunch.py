# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = deque()
        s = []
        length = len(students)

        for i in range(length):
            q.append(students[i])
            s.append(sandwiches[length - i - 1])
        
        waiting = 0
        while len(q) and waiting < len(q):
            if s[-1] == q[0]:
                s.pop()
                q.popleft()
                waiting = 0
            else:
                q.append(q.popleft())
                waiting += 1

        return len(q)
