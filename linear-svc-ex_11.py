import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn import svm

x = [1, 5, 1.5, 8, 1, 9]
y = [2, 8, 1.8, 8, 0.6, 11]

# above both are features

#graphing the data:
plt.scatter(x,y)
plt.show()
#the overall feature list -
X = np.array([[1,2],
             [5,8],
             [1.5,1.8],
             [8,8],
             [1,0.6],
             [9,11]])
#labels-
y = [0,1,0,1,0,1]

#defining the classifier -
clf = svm.SVC(kernel='linear', C = 1.0)

clf.fit(X,y)

#to predict and test-
print(clf.predict([10.58,10.76]))

#visualize -
w = clf.coef_[0]
print(w)

a = -w[0] / w[1] #learning rate

xx = np.linspace(0,12)
yy = a * xx - clf.intercept_[0] / w[1]

h0 = plt.plot(xx, yy, 'k-', label="non weighted div")

plt.scatter(X[:, 0], X[:, 1], c = y)
plt.legend()
plt.show()