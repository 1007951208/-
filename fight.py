
'''模拟一次简单的战斗'''

import time 

def role(name,healthy=1000,attack=100,describe=""):
    p = {"name":name,"healthy":healthy,"attack":attack,"describe":describe}
    return p

def once_attack(attacker,attacked):
    attacked.healthy -= attacker.attack
    if attacked.healthy <0:
        attacker.attack = 0
    print("\r                                                                      ",end="")
    print("\r{}攻击了{},造成了{}点伤害,{}剩余血量为{}".format(attacker.name,attacked.name,attacker.attack,attacked.name,attacked.healthy),end="    ")
    time.sleep(1)    
    return attacked.healthy


def attack(A,B):
    i = 1
    while True:
        B.healthy=once_attack(A,B)
        if B.healthy<=0:
            print("\n{}胜利了".format(A.name))
            break
        A.healthy=once_attack(B,A)
        if A.healthy<=0:
            print("\n{}胜利了".format(B.name))
            break

        i=i+1
        if i >10:
            break



'''p1 = role("Ken")
p2 = role("李白",1100)
attack(p1,p2)'''
