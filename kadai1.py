
import random #ランダムモジュール
import math
import copy
import numpy as np

def nimotu_init():
    nimotu_list = np.array([(2,21),(10,22),(7,28),(2,21),(4,12),(9,24),(10,15),(7,2),(8,25),(5,28),(3,4),(10,22),
                            (9,36),(8,2),(8,7),(5,40),(7,14),(3,40),(9,33),(7,21),(2,28),(10,22),(7,14),(9,36),(7,28),
                            (2,21),(10,18),(4,12),(9,24),(10,15)])
    omosa = nimotu_list[:,0]
    nedan = nimotu_list[:,1]
    return [omosa,nedan]

##評価関数
def eval_func(gean):
    omosa,nedan = nimotu_init()
##    gean = [0,0,1,0,1,1,1,0,1,1]
    vallue = sum(nedan * gean)
    weight = sum(omosa * gean)
    weightmax = 60
    if weight< weightmax:
        return vallue
    else:
        vallue = 0
        return vallue

def geneticoptimize(maxiter = 300,maximize = True,popsize = 50,popnum = 30,elite = 0.2,mutprob =0.3):
    """
    maxiter = 1, 繰り返し数
    maximize = True,    スコアを最大化
    popsize = 50,   個体数
    popnum = 10,    遺伝子数（長さ）
    elite = 0.2,    生き残る遺伝子の割合
    mutprob =0.2    突然変異のおこる確立
    """
    # 突然変異
    def mutate(vec):
        i = random.SystemRandom().randint(0,popnum-1)
        if vec[i] == 0:
            return vec[:i] + [1]+vec[i+1:]
        else:
            return vec[:i] + [0]+vec[i+1:]
     # 1点交叉 非推奨
    def one_point_crossover(r1,r2):
        i = random.SystemRandom().randint(1,popnum-2)

        return random.SystemRandom().choice((r1[0:i] + r2[i:], r2[0:i] + r1[i:]))

    # 2点交叉
    def two_point_crossover(r1,r2):
        i, j = sorted(random.SystemRandom().sample(range(popnum),2))
        return random.SystemRandom().choice((r1[0:i] + r2[i:j] + r1[j:] , r2[0:i] + r1[i:j] + r2[j:]))

    # 一様交叉
    def uniform_crossover(r1, r2):
        q1 = copy.copy(r1)
        q2 = copy.copy(r2)
        for i in range(len(r1)):
            if random.SystemRandom().random() < 0.5:
                q1[i], q2[i] = q2[i], q1[i]

        return random.SystemRandom().choice([q1,q2])
    #遺伝子の初期化
    pop = []
    for i in range(popsize):
        vec = [random.SystemRandom().randint(0,1) for i in range(popnum)]
        print (vec)
        pop.append(vec)
    #遺伝子の初期化

    # 交叉アルゴリズムの選択
    #crossover = two_point_crossover
    crossover = uniform_crossover

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
            if random.SystemRandom().random() < mutprob:
                # 突然変異
                c = random.SystemRandom().randint(0,topelite)
                pop.append(mutate(ranked[c]))

            else:
                # 交叉
                c1 = random.SystemRandom().randint(0,topelite)
                c2 = random.SystemRandom().randint(0,topelite)
                pop.append(crossover(ranked[c1],ranked[c2]))
##        # 暫定の値を出力
        #print(scores[0][0])
        print(scores[0])
    return scores[0]


def main():
    omosa,nedan = nimotu_init()
    ans = geneticoptimize()
    print("Ans:",ans)

if __name__ == '__main__':
    main()
