import random
import math
import copy
import numpy as np


maxweight = 50

def nimotu_init():
    nimotu_list = np.array([(2,21),(10,22),(7,28),(2,21),(4,12),(9,24),(10,15),(7,2),(8,25),(5,28),(3,4),(10,22),
                           (9,36),(8,2),(8,7),(5,40),(7,14),(3,40),(9,33),(7,21),(2,28),(10,22),(7,14),(9,36),(7,28),
                           (2,21),(10,18),(4,12),(9,24),(10,15)])
    omosa = nimotu_list[:,0]
    nedan = nimotu_list[:,1]
    return [omosa, nedan]

#評価関数
def eval_func(gean):
    omosa,nedan = nimotu_init()
    vallue = sum(nedan * gean)
    weight = sum(omosa * gean)
    if weight < maxweight:
        return vallue
    else:
        return 0

def genetioptimize(maxiter = 30000,maximize = True,popsize = 15,popnum = 30,elite = 0.2,mutprob =0.2):
    """
    maxiter = 1, 繰り返し数
    maximize = True,    スコアを最大化
    popsize = 50,   個体数
    popnum = 10,    遺伝子数（長さ）
    elite = 0.2,    生き残る遺伝子の割合
    mutprob =0.2    突然変異のおこる確立
    """
