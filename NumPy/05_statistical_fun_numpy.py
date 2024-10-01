#statistical function
# mean ,median, mode, variance, std deviation
import numpy as np
temperature = np.array([190,87,75,45,50,66,72,75,87,75])
# To calculate mean - mean()
mean_temperature = np.mean(temperature)
print("Mean temperature :",mean_temperature)

# median - median()
median_temperature = np.median(temperature)
print("Median temperature :",median_temperature)

# variance
variance_tem = np.var(temperature)
print("Variance temperature :",variance_tem)

# min, max - to get min and max value from dataset
min_tem = np.min(temperature)
print("Minmum temperature :",min_tem)

max_tem = np.max(temperature)
print("Maxmum temperature :",max_tem)

# percentile
marks = np.array([45,65,78,87,54,34,54,12,90,54,67,87,89,100,50,60,70,80,90,95,85,55,45,63])
# percentile -percentile()
median_marks = np.median(marks)
print("Median marks :",median_marks)

percentile_marks =np.percentile(marks,50)
print("50th percentile :",percentile_marks)

# Quartile - Q1 -25% , Q2- 50% ,Q3 -75% ,Q4 -100%
lower_percentile =np.percentile(marks,25)
print(lower_percentile)

highest_percentile =np.percentile(marks,100)
print(highest_percentile)

marks = np.array([45,65,78,87,54,34,54,12,90,54,67,87,89,100,50,60,70,80,90,95,85,55,45,63,20,25,65,40,58,20])
np.save('05_statistical_fun_numpy.npy',marks)


