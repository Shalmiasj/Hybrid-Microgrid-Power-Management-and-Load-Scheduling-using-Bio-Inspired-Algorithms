# PARTICLE SWARM OPTIMIZATION ALGORITHM
 
import random
import copy   
import sys     
import pandas as pd 
 
def Obj_func(position):
    dataset = pd.read_csv('MG_Hourly_data.csv',encoding='latin1')
    MT_Pmax = 30
    fitnessVal = 0.0
    sum=0.0
    Ui = 1
    l=[]
    for j in range(len(position)):
        peak = ["08H00","09H00","10H00","11H00","12H00","13H00","14H00","15H00","16H00","17H00"]
        for i in range(1):
            if dataset['Hour'][j] in peak:
                Ui = 1
                sum1 = (Ui * dataset['PV_Pmax'][j] * dataset['PV_cost'][j]) 
                sum2 = 0 
                sum3 = (Ui * dataset['MT_cost'][j] *  MT_Pmax)
            else:
                sum1 = 0
                sum2 = (Ui * dataset['WT_Pmax'][j] * dataset['WT_cost'][j]) 
                sum3 = (Ui * dataset['MT_cost'][j] *  MT_Pmax) 
            sum = (sum1 + sum2 + sum3);
    fitnessVal +=  sum #operating cost
    return (fitnessVal);

class Particle:
  def __init__(self, fitness, dim, minx, maxx, seed):
    self.rnd = random.Random(seed)
    self.position = [0.0 for i in range(dim)]
    self.velocity = [0.0 for i in range(dim)]
    self.best_part_pos = [0.0 for i in range(dim)]
    for i in range(dim):
      self.position[i] = ((maxx - minx) *
        self.rnd.random() + minx)
      self.velocity[i] = ((maxx - minx) *
        self.rnd.random() + minx)

    self.fitness = fitness(self.position) 

    self.best_part_pos = copy.copy(self.position)
    self.best_part_fitnessVal = self.fitness 

def pso(fitness, max_iter, n, dim, minx, maxx):
  w = 0.729   
  c1 = 1.49445 
  c2 = 1.49445 
 
  rnd = random.Random(0)

  swarm = [Particle(fitness, dim, minx, maxx, i) for i in range(n)]

  best_swarm_pos = [0.0 for i in range(dim)]
  best_swarm_fitnessVal = sys.float_info.max 

  for i in range(n): 
    if swarm[i].fitness < best_swarm_fitnessVal:
      best_swarm_fitnessVal = swarm[i].fitness
      best_swarm_pos = copy.copy(swarm[i].position)
 
  #Main loop of pso
  Iter = 0
  while Iter < max_iter:
 
    for i in range(n): 
      for k in range(dim):
        r1 = rnd.random()    
        r2 = rnd.random()
        swarm[i].velocity[k] = (
                                 (w * swarm[i].velocity[k]) +
                                 (c1 * r1 * (swarm[i].best_part_pos[k] - swarm[i].position[k])) + 
                                 (c2 * r2 * (best_swarm_pos[k] -swarm[i].position[k]))
                               ) 
        if swarm[i].velocity[k] < minx:
          swarm[i].velocity[k] = minx
        elif swarm[i].velocity[k] > maxx:
          swarm[i].velocity[k] = maxx
 
      for k in range(dim):
        swarm[i].position[k] += swarm[i].velocity[k]
   
      swarm[i].fitness = fitness(swarm[i].position)

      if swarm[i].fitness < swarm[i].best_part_fitnessVal:
        swarm[i].best_part_fitnessVal = swarm[i].fitness
        swarm[i].best_part_pos = copy.copy(swarm[i].position)

      if swarm[i].fitness < best_swarm_fitnessVal:
        best_swarm_fitnessVal = swarm[i].fitness
        best_swarm_pos = copy.copy(swarm[i].position)

    Iter += 1
  return best_swarm_pos

# Driver code for Objective function
print("\nBegin particle swarm optimization on Objective function\n")
dim = 10
fitness = Obj_func
 
 
print("Goal is to minimize Objective function")

num_particles = 50
max_iter = 100
 
print("Setting num_particles = " + str(num_particles))
print("Setting max_iter    = " + str(max_iter)) 

best_position = pso(fitness, max_iter, num_particles, dim, -10,10)
 
print("\nPSO completed\n")
print("\nBest solution found:")
fitnessVal = fitness(best_position)
print("Fitness of best solution: ",round(fitnessVal,4))
 
print("\nEnd particle swarm for Objective function\n")