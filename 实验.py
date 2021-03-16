import random
import character as c
"""
p1 = c.Character("一号")
p2 = c.Character("二号")
a_list = [p1,p2]
print(a_list.pop(0).name) 
pop可以返回对象
"""

b_list = [1,2,3,4,5]
for i in range(5):
    print(random.choice(b_list)