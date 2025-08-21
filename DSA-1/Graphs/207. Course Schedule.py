class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visit = set()
        # completed = set() # if we do not want to modify preMap, we can use this to track completed courses
        def dfs(crs):
            if crs in visit:
                return False
            if preMap[crs] == []: # if crs in completed: return True
                return True
            
            visit.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            preMap[crs] = [] # completed.add(crs) # mark as completed
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True