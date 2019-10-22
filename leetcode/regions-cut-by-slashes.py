'''
problem_url -: https://leetcode.com/problems/regions-cut-by-slashes
editorial1 - https://leetcode.com/articles/regions-cut-by-slashes/#
editorial2- https://leetcode.com/problems/regions-cut-by-slashes/discuss/205680/JavaC%2B%2BPython-Split-4-parts-and-Union-Find
'''
class Solution(object):
    
    def dsu(self, n):
        self.parent = [i for i in range(n)]
    
    def find(self, x):
        while x!= self.parent[x]:
            x = self.parent[x]
        return x
    
    def union(self, x, y):
       self.parent[self.find(x)] = self.find(y)
    
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        N = len(grid)
        
        # divide each cell into 4 triangles
        self.dsu(4*N*N)
        
        for i in range(N):
            for j in range(N):
                root = 4*(i*N + j)
                
                char = grid[i][j]
                if not char == "\\": #join the parts of one cell
                    self.union(root, root+3)
                    self.union(root+1, root+2)
                if not char == "/": # join the parts of one cell
                    self.union(root, root+1)
                    self.union(root+2, root+3)
                    
                # Join the different cells
                if i > 0: #up 
                    self.union(root, root - 4*N + 2)
                if i < N-1: # down
                    self.union(root+2, root + 4*N)
                if j > 0: # left
                    self.union(root+3, root - 4 + 1)
                if j < N-1: # right
                    self.union(root+1, root + 4 + 3)
        ans = 0
        for i in range(4*N*N):
            if self.find(i)==i:
                ans += 1
        return ans