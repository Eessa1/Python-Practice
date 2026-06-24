import numpy as np
import matplotlib.pyplot as plt

#  house data
sizes =  np.array([50, 60, 70, 80, 90, 100])
prices = np.array([140, 195, 200, 260, 280, 310])

# plot 
plt.scatter(sizes, prices)
plt.xlabel("Size (sqm)")
plt.ylabel("Price (£k)")
plt.title("House prices")
plt.show()
m = 3.1
c = 5
predicted = m* sizes + c
errors = predicted - prices
rmse = np.sqrt(np.mean(errors**2))
print ("RMSE:", rmse)
plt.scatter(sizes,prices, label = "real")
plt.plot(sizes, predicted, color = 'red', label="prediction")
plt.legend()
plt.show()

