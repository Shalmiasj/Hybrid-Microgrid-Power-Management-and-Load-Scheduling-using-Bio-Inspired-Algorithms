# Hybrid-Microgrid-Power-Management-and-Load-Scheduling-using-Bio-Inspired-Algorithms
 An efficient power management strategy is designed to effectively manage the electricity production from renewable energy resources connected to a micro-grid, thereby satisfying consumer demand. Minimized the operating costs using Bio Inspired Algorithms 

# Hybrid Microgrid Power Management and Load Scheduling using Bio-Inspired Algorithms
An efficient power management strategy is designed to effectively
manage the electricity production from renewable energy
resources connected to a micro-grid, thereby satisfying consumer
demand.Minimized the operating costs using Bio Inspired Algorithms such as Particle Swarm Optimization and Bat Algorithm.

## Overview
A microgrid plan that incorporates local wind or solar resources can provide important service redundancy while also reducing the main grid's vulnerability to localised calamity. In order to manage the distribution of energy resources from microgrids to loads, an efficient scheduling of power supply is required. To balance non-shiftable demand for power the operating cost during peak hours is minimised

## Motivation
Due to population growth, rapid industrialization and economic development there is huge demand for energy resources to satisfy the everyday requirements of electricity. The use of renewable energy resources such as solar panels and wind turbines help to preserve the existing conventional energy sources and also reduce the emission of greenhouse gases. Microgrids are used instead of main grids, and are often powered by generators or renewable wind and solar energy resources. A microgrid plan that incorporates local wind or solar resources can provide important service redundancy while also reducing the main grid's vulnerability to localised calamity


## Micro-grid Architecture

![Workflow](https://imgtr.ee/images/2023/06/17/YKZtM.png)


## Data from micro grid components collected every hour during the day
![data](https://imgtr.ee/images/2023/06/17/YKdO4.jpg)



## Files 
- `Pso.py` : Operating cost for the usage of energy resources for each day is computed using PSO
- `bat.py`: Operating cost for the usage of energy resources for each day is computed using bat algorithm
- `Cost_Calculation.ipnb` :The estimated operating cost, power load and the day profile costs per unit of distributed generators (PV and WT) without MT
- `PLOT_codes.ipnb`: Contains various plots for comparing the results in the presence or absence of certain energy resources
- `MG_Hourly_data.csv`: Data from micro grid components collected every hour during the day

## Algorithm Used
- Particle Swarm Optimization
- Bat Algorithm

## Packages Used
- Pandas 
- Numpy
- Matplotlib 
- Plotly 
- copy
- BatAlgorithm
- Random


## Simulation Results
When MT power is not used, the operating cost increases during peak hours and is low during other times of the day. 
As a next stage, the PSO algorithm is applied to calculate the necessary hourly set points for each distributed generator of the microgrid so that we can satisfy only the hourly non shiftable part of the load power.  It is then applied to calculate the rest hourly set points for each generator to satisfy the daily shiftable load power.  Figure 9 shows the distribution of the hourly optimal powers set points for each distributed generators by considering the non shiftable load powers only.

## Conclusion

In this article,  the minimal operation cost for the energy usage from a micro-grid which is connected to PV,WT and MT is obtained using the bio-inspired algorithm PSO and Bat Algorithm. The Optimal operating cost attained by using the reduced objective function in the PSO and Bat algorithm are calculated. The corresponding energy usage prices to the respective objective function, the optimal cost for each hour is achieved. By visualizing the cost unit prices in different scenarios, wind energy is more expensive than conventional energy resources. Future work can be carried out to examine the reduced operating cost by comparing other hybrid bio-inspired algorithms. 

## Documentation

[Documentation](https://drive.google.com/file/d/1GbUakik3ParXTl2R-kbDwB4_S1MaOaL8/view?usp=sharing)


