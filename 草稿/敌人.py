class Enemy_hero():
    def __init__(self,name):
        self.name = name 
        self.quality = [3000,100,100,100,100]
        self.level = 1
        self.exp = 0
    
    def level_up(self):
        self.exp_max = 100+ (self.level-1)*20
        if self.exp >= self.exp_max:
            self.level += 1
    
    def quality_up(self):
        self.quality +=10

    def describe_hero(self):
        print("英雄名称为"+self.name)
        print("血量为"+str(self.quality[0]))
        print("物理攻击为"+str(self.quality[1]))

guan = Enemy_hero("关羽")
guan.describe_hero()

diao = Enemy_hero("貂蝉")
diao.describe_hero()