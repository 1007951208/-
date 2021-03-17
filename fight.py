'''
module fight
用于模拟战斗的过程
'''

import time
import character as c

def role(name,healthy=1000,attack=100,describe=""):
    p = {"name":name,"healthy":healthy,"attack":attack,"describe":describe}
    return p


def attack(A,B):
    i = 1
    while True:
        A.fight(B)
        if B.healthy<=0:
            print("\n{}胜利了".format(A.name))
            break
        B.fight(A)
        if A.healthy<=0:
            print("\n{}胜利了".format(B.name))
            break

        i=i+1
        if i >10:
            break


if __name__ == "__main__":
    pass
