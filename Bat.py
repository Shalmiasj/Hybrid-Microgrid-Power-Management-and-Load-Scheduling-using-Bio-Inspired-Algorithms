# BAT ALGORITHM

import random
from BatAlgorithm import *
import numpy as np
import pandas as pd

class BatAlgorithm():
    def __init__(self, D, NP, N_Gen, A, r, Qmin, Qmax, Lower, Upper, function):
        self.D = D  
        self.NP = NP  
        self.N_Gen = N_Gen  
        self.A = A  
        self.r = r  
        self.Qmin = Qmin  
        self.Qmax = Qmax  
        self.Lower = Lower  
        self.Upper = Upper  
        self.f_min = 0.0  
        self.Lb = [0] * self.D 
        self.Ub = [0] * self.D  
        self.Q = [0] * self.NP  

        self.v = [[0 for i in range(self.D)] for j in range(self.NP)]  
        self.Sol = [[0 for i in range(self.D)] for j in range(self.NP)]  
        self.Fitness = [0] * self.NP 
        self.best = [0] * self.D  
        self.Fun = function


    def best_bat(self):
        i = 0
        j = 0
        for i in range(self.NP):
            if self.Fitness[i] < self.Fitness[j]:
                j = i
        for i in range(self.D):
            self.best[i] = self.Sol[j][i]
        self.f_min = self.Fitness[j]

    def init_bat(self):
        for i in range(self.D):
            self.Lb[i] = self.Lower
            self.Ub[i] = self.Upper

        for i in range(self.NP):
            self.Q[i] = 0
            for j in range(self.D):
                rnd = np.random.uniform(0, 1)
                self.v[i][j] = 0.0
                self.Sol[i][j] = self.Lb[j] + (self.Ub[j] - self.Lb[j]) * rnd
            self.Fitness[i] = self.Fun(self.D, self.Sol[i])
        self.best_bat()

    def simplebounds(self, val, lower, upper):
        if val < lower:
            val = lower
        if val > upper:
            val = upper
        return val

    def move_bat(self):
        S = [[0.0 for i in range(self.D)] for j in range(self.NP)]

        self.init_bat()

        for t in range(self.N_Gen):
            for i in range(self.NP):
                rnd = np.random.uniform(0, 1)
                self.Q[i] = self.Qmin + (self.Qmax - self.Qmin) * rnd
                for j in range(self.D):
                    self.v[i][j] = self.v[i][j] + (self.Sol[i][j] -
                                                   self.best[j]) * self.Q[i]
                    S[i][j] = self.Sol[i][j] + self.v[i][j]

                    S[i][j] = self.simplebounds(S[i][j], self.Lb[j],
                                                self.Ub[j])

                rnd = np.random.random_sample()

                if rnd > self.r:
                    for j in range(self.D):
                        S[i][j] = self.best[j] + 0.001 * random.gauss(0, 1)
                        S[i][j] = self.simplebounds(S[i][j], self.Lb[j],
                                                self.Ub[j])
                        
                Fnew = self.Fun(self.D, S[i])

                rnd = np.random.random_sample()

                if (Fnew <= self.Fitness[i]) and (rnd < self.A):
                    for j in range(self.D):
                        self.Sol[i][j] = S[i][j]
                    self.Fitness[i] = Fnew

                if Fnew <= self.f_min:
                    for j in range(self.D):
                        self.best[j] = S[i][j]
                    self.f_min = Fnew

        print(round(self.f_min,5))

def Obj_Func(D, sol):
    dataset = pd.read_csv('MG_Hourly_data.csv',encoding='latin1')
    MT_Pmax = 30
    nsum=0
    sum=0
    Ui = 1
    l=[]

    peak = ["08H00","09H00","10H00","11H00","12H00","13H00","14H00","15H00","16H00","17H00"]
    for j in range(D):
        if dataset['Hour'][j] in peak:
            Ui = 1
            sum1 = (Ui * dataset['PV_Pmax'][j] * dataset['PV_cost'][j]) 
            sum2 = 0
            sum3 = (Ui * dataset['MT_cost'][j] *  MT_Pmax) 
        else:
            sum1 = 0
            sum2 = (Ui * dataset['WT_Pmax'][j] * dataset['WT_cost'][j]) 
            sum3 = (Ui * dataset['MT_cost'][j] *  MT_Pmax) 
        sum = sum1 + sum2 + sum3
    nsum +=  sum #operating cost
    return nsum


print("\nBegin Bat algorithm on Objective function\n")

D=24
num_bats = 40
max_iter = 100

print("Goal is to minimize Objective function ")

print("Setting num_bats = " + str(num_bats))
print("Setting max_iter    = " + str(max_iter))


print("\nBAT completed\n")

print("\nBest solution found:")

Algorithm = BatAlgorithm(24, 40, 100, 0.5, 0.5, 0.0, 2.0, -10.0, 10.0, Obj_Func)
Algorithm.move_bat()

print("\nEnd Bat algorithm for Objective function\n")