# Write By Sunwl
# 2017/10/26
#
# 学生管理系统
# 
# python 3.6.2

class Student:
    __slots__ = ["name", "age", "score"]

    def __init__(self, n, a, s):
        self.name = n
        self.age = a
        self.score = s

    def setScore(self, s):
        if s > 100 or s < 0:
            return
        self.score = s

    def infos(self):
        s = str(self)        
        print(s)

    def __str__(self):
        return ("|" + self.name.center(13) +
             "|" + str(self.age).center(13) +
             "|" + str(self.score).center(13) + "|"
             )
