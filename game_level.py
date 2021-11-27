"""
单个游戏关卡的模拟，通过创建场景Scene"""

import random
import time

import character as c
import fight
import item

# Scene类，代表一个游戏场景/关卡


class Scene():

    def __init__(self, scene_name):  # 初始化场景，构建敌人、玩家、宝藏
        self.scene_name = scene_name
        self.enemy_sum = {1}
        self.enemy = []
        self.create_scene_enemy("默认敌人", 200, 10, "敌人出现了")
        self.describe = ""
        self.treasure = {"name": "铜钱"}
        # {"name":"你","healthy":1000,"attack":180}
        self.player = c.Character("你")

        self.describe = "这里一片漆黑"

    def scene_describe(self, describe):  # 描述场景 ###
        self.describe = describe

    def create_scene_item(self, name):
        self.item = item.Item(name)

    def scene_enter(self):  # 进入场景
        print("你走进了了" + self.scene_name)
        print(self.describe)
        time.sleep(1)

    def set_player(self, player_name, player_healthy, player_attack):  # 设置玩家信息
        self.player = {{"name": player_name,
                        "healthy": player_healthy, "attack": player_attack}}

    def create_scene_enemy(self, enemy_name, enemy_healthy=1000, enemy_attacked=100, enemy_describe=""):  # 创建场景内的敌人
        self.enemy.append(c.Character(
            enemy_name, enemy_healthy, enemy_attacked, enemy_describe))
        self.enemy_sum.add(len(self.enemy))

    def make_treasure(self, treasure_name, treasure_attack, treasure_healthy):  # 创建宝藏
        self.treasure = {"name": treasure_name,
                         "attack": treasure_attack, "healthy": treasure_healthy}

    def set_event_common(self):
        self.event_common = {""}

    def select_enemy(self):
        while True:
            select = random.randint(1, len(self.enemy))
            if select in self.enemy_sum:
                self.enemy_sum.discard(select)
                return select-1

    def enemy_encounter(self):  # 遭遇敌人
        if not self.enemy_sum.issubset(set()):  # 如果仍有未遭遇的敌人：
            select = self.select_enemy()
            print(self.enemy[select].describe)
            time.sleep(0.3)
            choice = input("你的选择是\n1.逃走　2.迎战    ")
            if eval(choice) == 1:
                print("你闪躲开来，转眼间就到了远处")
            else:
                print("战斗开始")
                fight.attack(self.player, self.enemy[select])

    def get_treasure(self):  # 找到宝藏
        print("你找到了{}".format(self.treasure["name"]))

    def walking(self):
        time.sleep(0.3)
        print("你在{}中散步".format(self.scene_name))
        time.sleep(0.8)

    def event_item_work(self):
        self.player.observe(self.item)

    def random_event(self):  # 随机事件，遭遇敌人或找到宝藏
        ran = random.randint(1, 2)
        if ran in {1}:
            self.get_treasure()
        if ran in {2}:
            self.enemy_encounter()

    def game(self):  # 进入场景，并经历数个随机事件
        event_num = random.randint(2, 5)
        self.scene_enter()
        for i in range(event_num):
            self.walking()
            self.random_event()


game1 = Scene("铜人巷")
game1.create_scene_item("梅花")
game1.event_item_work()
game1.create_scene_enemy("剑丙", 500, 100, "一人持剑从黑暗处突出")
game1.scene_describe("远处立着数个铜人，兵甲锋利，但一动不动，似是死物")
game1.game()
