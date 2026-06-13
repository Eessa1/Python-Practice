import numpy as np
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
x2 = [1,2,3,4,5]
y2 = [1,8,27,64,125]
plt.plot(x,y)
plt.plot(x2,y2)
plt.title("Y = X squared and x cubed")
plt.legend(["X squared","X cubed"], loc = "lower right")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()