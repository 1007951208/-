"""简单的关卡模拟，已整合至game_level"""
import fight
import random

def scene_enter(scene_name):
    print("你已进入了" + scene_name)
    print("这里一片漆黑") ##描述

def enemy_encounter(me,enemy):
    print("你遇到了{}".format(enemy["name"]))
    choice=input("你的选择是\n1.逃走　2.迎战\n")
    if eval(choice) ==1 :
        print("你退出了关卡")
    else :
        print("战斗开始")
        fight.attack(me,enemy)

def get_treasure(me,treasure):
    print("你找到了{}".format(treasure["name"]))

def random_event(a,b,c):
    ran = random.randint(1,2)
    if ran in {1}:
        get_treasure(a,c)
    if ran in {2}:
        enemy_encounter(a,b)

def game(game_scene,player,enemy,treasure):
    event_num = random.randint(2,5)
    scene_enter(game_scene)
    for i in range(event_num):
        random_event(player,enemy,treasure)

treasure = {"name":"宝剑","attack_up":10}
me = fight.role("你")
ann=fight.role("铜人甲")
game("金牛街",me,ann,treasure)

'''
ken=fight.role("你")

enemy_encounter(ken,ann)
'''