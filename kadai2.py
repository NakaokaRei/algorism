import random #ランダムモジュール
import math
import copy
import numpy as np

def individual_init():
    x_1 = random.uniform(-1.5,4)
    x_2 = random.uniform(-3,4)

    print([x_1, x_2])
    return [x_1, x_2]

##評価関数
def eval_func(gean):
    vallue = math.sin(gean[0] + gean[1]) + (gean[0] - gean[1])**2 - 1.5 * gean[0] + 2.5 * gean[1] + 1
    return vallue

# 突然変異
def mutate(gean):
    index = random.randint(0, 1)
    if index == 0:
        gean[index] = random.uniform(-1.5,4)
    elif index == 1:
        gean[index] = random.uniform(-3,4)

    return gean

def BLX_alpha(r1, r2):
    a = 0.3
    x1 = r1[0]
    y1 = r1[1]
    x2 = r2[0]
    y2 = r2[1]
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    min_x = min(x1, x2)
    min_y = min(y1, y2)
    max_x = max(x1, x2)
    max_y = max(y1, y2)
    min_cx = min_x - a * dx
    max_cx = max_x + a * dx
    min_cy = min_y - a * dy
    max_cy = max_y + a * dy
    x_1_new = random.uniform(min_cx,max_cx)
    x_2_new = random.uniform(min_cy,max_cy)

    return [x_1_new, x_2_new]


def geneticoptimize(maxiter = 30000,maximize = False,popsize = 50,elite = 0.5,mutprob =0.2,crosprob=0.8):
    """
    maxiter = 1, 繰り返し数
    maximize = True,    スコアを最大化
    popsize = 50,   個体数
    elite = 0.2,    生き残る遺伝子の割合
    mutprob = 0.3    突然変異のおこる確立
    crosprob = 0.8  交叉率
    """

    #遺伝子の初期化
    pop = []
    for i in range(popsize):
        pop.append(individual_init())

    crossover = BLX_alpha

    #メインループ
    topelite = int(elite * popsize)
    for i in range(maxiter):
        scores=[(eval_func(v),v) for v in pop]
        scores.sort()
        if maximize:
            scores.reverse()
        ranked = [v for (s,v) in scores]
        # 弱い遺伝子は淘汰される
        pop = ranked[0:topelite]
        # 生き残った遺伝子同士で交叉したり突然変異したり
        while len(pop) < popsize:
            if random.random() < mutprob:
                # 突然変異
                c = random.randint(0,topelite)
                pop.append(mutate(ranked[c]))
            elif random.random() < crosprob:
                # 交叉
                c1 = random.randint(0,topelite)
                c2 = random.randint(0,topelite)
                pop.append(crossover(ranked[c1],ranked[c2]))

        print(scores[0])
    return scores[0]


def main():
    ans = geneticoptimize()
    print("Ans:",ans)

if __name__ == '__main__':
    main()
