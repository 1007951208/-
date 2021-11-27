"""角色模块"""

import time
import random

class Character():
    
    def __init__(self,name,healthy=1000,attack = 100,describe = ""):
        self.name = name
        self.healthy = healthy
        self.attack = attack
        self.describe = describe
        self.equipment = {"weapon":0,"armor":0}
        if describe.isspace() :
            self.describe = "你遭遇了" + name

    """ 攻击模块 """
    def fight(self,attacked:"被攻击的character对象"):
        attacked.healthy -= self.attack
        if attacked.healthy <0:
            self.attack = 0
        print("\r                                                                      ",end="")
        print("\r{}攻击了{},造成了{}点伤害,{}剩余血量为{}".format(self.name,attacked.name,self.attack,attacked.name,attacked.healthy),end="    ")
        time.sleep(1)    
        return attacked.healthy
    
    """ TODO 与物品的交互 """
    def observe(self,item):
        print("你观察了"+ item.name)
        ran = random.randint(1,10)
        if ran in {1,2,3,4,5,6,7,8}:
            item.item_work()   #触发item事件
        if ran in {9,10}:
            print("无事发生")
    """ TODO 查找物品 """
    def see(self,scene):
        pass
    
    """ TODO 装备 """
    def get_equipment(self, equipment):
        """ 安装装备 """
        self.equipment[equipment.type] = equipment

    
        
    
    
        
        
