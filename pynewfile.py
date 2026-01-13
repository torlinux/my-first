import numpy as np
import matplotlib.pyplot as pyplot
plt.plot(temp,pressure)
plt.xlabel('temprature in centgrate')
plt.ylabel('pressure in atm')


plt.title('temp vs pre')
plt.xticks(np.arange(0,6,step=0.5))
plt.show