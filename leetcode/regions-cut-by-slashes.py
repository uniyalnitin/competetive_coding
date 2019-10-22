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

 '''
 Solution 2- using DFS
 editorial - https://leetcode.com/problems/regions-cut-by-slashes/discuss/367154/Python-readable-DFS-on-upscaled-grid
 '''

 class Solution(object):
    
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        N = len(grid)*3

        big_grid = [[True]*N for i in range(N)]

        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == "/":
                    big_grid[3*i][3*j+2] = False
                    big_grid[3*i+1][3*j+1] = False
                    big_grid[3*i+2][3*j] = False
                elif grid[i][j] == "\\":
                    big_grid[3*i][3*j] = False
                    big_grid[3*i+1][3*j+1] = False
                    big_grid[3*i+2][3*j+2] = False
        seen = set()
        regions_count = 0
        n = N
        for i, row in enumerate(big_grid):
			for j, is_char in enumerate(row):
				if is_char and (i, j) not in seen:
					regions_count += 1
					stack = [(i, j)]
					while stack:
						a, b = stack.pop()
						seen.add((a, b))
						if a > 0 and big_grid[a - 1][b] and (a - 1, b) not in seen:
							stack.append((a - 1, b))
						if a < n - 1 and big_grid[a + 1][b] and (a + 1, b) not in seen:
							stack.append((a + 1, b))
						if b > 0 and big_grid[a][b - 1] and (a, b - 1) not in seen:
							stack.append((a, b - 1))
						if b < n - 1 and big_grid[a][b + 1] and (a, b + 1) not in seen:
							stack.append((a, b + 1))
        return regions_count