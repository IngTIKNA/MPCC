import json
import matplotlib.pyplot as plt


f = open('../Params/track.json')
data = json.load(f)


#Plot the road boundaries with the centerline 

plt.plot(data["X"],data["Y"])
plt.plot(data["X_i"],data["Y_i"])
plt.plot(data["X_o"],data["Y_o"])
plt.show()



plt.scatter(data["X"],data["Y"])
plt.scatter(data["X_i"],data["Y_i"])
plt.scatter(data["X_o"],data["Y_o"])
plt.show()









