# Write here the code challenge solution
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
    def sortedArrayToBST(self, nums):
        def helper(l,r):
            if l > r:
                return None
            
            m = (l+r)//2
            root = TreeNode(nums[m])
            root.left = helper(l,m-1)
            root.right = helper(m+1,r)
            return root.val
        
        return helper(0,len(nums)-1)
    
    
test = TreeNode()
print(test.sortedArrayToBST([-10,-3,0,5,9]))
print(test.sortedArrayToBST( [3,1]))