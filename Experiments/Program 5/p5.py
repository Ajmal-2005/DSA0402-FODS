import numpy as np

fuel_efficiency = np.array([18, 22, 25, 30, 28])

average_efficiency = np.mean(fuel_efficiency)

old_model = fuel_efficiency[0]   
new_model = fuel_efficiency[3]   

percentage_improvement = ((new_model - old_model) / old_model) * 100

print("Average Fuel Efficiency:", average_efficiency, "MPG")
print("Percentage Improvement:", percentage_improvement, "%")