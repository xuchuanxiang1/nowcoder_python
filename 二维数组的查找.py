'''
在一个二维数组中（每个一维数组的长度相同），
每一行都按照从左到右递增的顺序排序，每一列都按照
从上到下递增的顺序排序。请完成一个函数，输入这样
的一个二维数组和一个整数，判断数组中是否含有该整
数。
'''
class Solution:
    def Find(self, target, array):
        cols = len(array[0]) - 1
        rows = len(array)
        while cols >= 0 and rows > 0:
            if array[len(array) - rows][cols] == target:
                return True
            if array[len(array) - rows][cols] > target:
                cols -= 1
            else:
                rows -= 1
        return False
if __name__ == '__main__':
    solution = Solution()
    array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    a = solution.Find(16,array)
    print(a)


