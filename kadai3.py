import random #ランダムモジュール
import math
import copy
import numpy as np
import copy


city = [[1150.0, 1760.0], [630.0, 1660.0], [40.0, 2090.0], [750.0, 1100.0],
        [750.0, 2030.0], [1030.0, 2070.0], [1650.0, 650.0], [1490.0, 1630.0],
        [790.0, 2260.0], [710.0, 1310.0], [840.0, 550.0], [1170.0, 2300.0],
        [970.0, 1340.0], [510.0, 700.0], [750.0, 900.0], [1280.0, 1200.0],
        [230.0, 590.0], [460.0, 860.0], [1040.0, 950.0], [590.0, 1390.0],
        [830.0, 1770.0], [490.0, 500.0], [1840.0, 1240.0], [1260.0, 1500.0],
        [1280.0, 790.0], [490.0, 2130.0], [1460.0, 1420.0], [1260.0, 1910.0],
        [360.0, 1980.0]]

def individual_init():
    x = list(range(29))
    random.shuffle(x)
    return x

##評価関数
def eval_func(gean):
    vallue = 0
    for i in range(len(city)):
        city1 = city[gean[i]]
        city2 = city[gean[i+1]]
        distance = math.sqrt((city1[0]-city2[0])**2 + (city1[1]-city2[1])**2)
        vallue = vallue + distance
        if i==(len(city)-1):
            city1 = city[i]
            city2 = city[0]
            distance = math.sqrt((city1[0]-city2[0])**2 + (city1[1]-city2[1])**2)
            vallue = vallue + distance
        return vallue



# 突然変異
def mutate(gean):
    index1 = random.randint(0, len(city)-1)
    index2 = random.randint(0, len(city)-1)
    gean1 = gean[index1]
    gean2 = gean[index2]
    gean[index1] = gean2
    gean[index2] = gean1

    return gean

def my_index_multi(l, x):
    return [i for i, _x in enumerate(l) if _x == x]

def PMX(r1, r2):
    child1 = copy.copy(r1)
    child2 = copy.copy(r2)
    box1 = [0] * len(city)
    box2 = [0] * len(city)
    digit1 = random.randint(0, len(city)-2)
    digit2 = random.randint(digit1, len(city)-1)
    child1[digit1:digit2] = r2[digit1:digit2]
    child2[digit1:digit2] = r1[digit1:digit2]
    for i in child1[digit1:digit2]:
        box1[i] = 1
    for i in child1:
        if box1[i] == 0:
            box1[i] = 1
    print(box1)
    for i in range(len(child1[:digit1])):
        if box1[child1[i]] == 1:
            index = random.choice(my_index_multi(box1, 0))
            child1[i] = index
            box1[index] = 1
    for i in range(len(child1[digit2+1:])):
        if box1[child1[digit2+1+i]] == 1:
            index = random.choice(my_index_multi(box1, 0))
            child1[digit2+1+i] = index
            box1[index] = 1

    # for i in range(len(child1)):
    #     if box1[child1[i]] == :
    #         index = random.choice(my_index_multi(box1, 0))
    #         child1[i] = index
    #         box1[index] = 1

    # print(box1)

    return child1





def geneticoptimize(maxiter = 1000,maximize = False,popsize = 50,elite = 0.7,mutprob =0.2,crosprob=0.7):
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

    crossover = PMX

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
