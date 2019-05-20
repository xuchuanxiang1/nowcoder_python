'''请实现一个函数，将一个字符串中的
每个空格替换成“%20”。例如，当字符
串为We Are Happy.则经过替换之后的字
符串为We%20Are%20Happy。'''
class Solution:
    def replaceSpace(self, s):
        return s.replace(' ','%20')

if __name__ == '__main__':
    s = input('请输入一个字符串：')
    solution = Solution()
    s = solution.replaceSpace(s)
    print(s)