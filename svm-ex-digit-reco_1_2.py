import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm

digits = datasets.load_digits()

#print(digits.data)

#print(digits.target)

#print(digits.images[7])

clf = svm.SVC(gamma=0.001, C=100)

X,y = digits.data[:-10], digits.target[:-10]

clf.fit(X,y)

print('Prediction:',clf.predict(digits.data[-5])) #any from -10 to -1

#to visualize the preiction-
plt.imshow(digits.images[-5], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()