""" 
Scene类：载入物品、任务，并进行事件
"""
import random
import time

import character as c
import fight
import item 

class Scene():  
    def __init__(self,scene_name,player):  #初始化场景，构建敌人、玩家、宝藏
        self.scene_name = scene_name 
        self.player = player  # 载入玩家
        self.people_list = [] 
        self.item_list = []     #场景物品列表
        self.describe = ""
        self.event_list = ["离开","与人交谈"]
    
    # 场景属性
    def set_describe(self,describe):
        self.describe = describe

    #载入
    def add_item(self,item):
        self.item_list.append(item)
    
    def add_people(self, people):
        self.people_list.append(people)

    #事件: player操作->事件响应
    def enter_scene(self):
        print("你进入了" + self.scene_name)
        print(self.describe)
        time.sleep(1)

    def meet(self):
        print("你要找的人是{}".format(self.people_list))

    def event_observe(self):
        pass
    
    
    def event_player_operate(self):
        print("你要做的是")

    def scene_event(self):
        self.enter_scene()
        while True:
            pass
        #TODO 响应事件
            
            
            

            

if __name__ == "__main__":
    player = c.Character("wo")
    
    xiaoer = c.Character("小二")
    zhanggui = c.Character("王掌柜")

    tea = Scene("茶馆", player)
    tea.add_people(xiaoer)
    tea.add_people(zhanggui)
    tea.set_describe("茶馆里没有什么客人")
    
    tea.scene_event()
    tea.meet()    
