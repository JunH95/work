# iris dataset 150 row 3가지 종류 4개 특성
import pandas as pd
import matplotlib.pyplot as plt

iris_data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/iris.csv")

# 산점도
# plt.scatter(iris_data["Sepal.Length"], iris_data["Petal.Length"])
# plt.xlabel("Sepal.Length")
# plt.xlabel("Petal.Length")
# plt.title("iris data")
# plt.show()

print(iris_data["Species"].unique())
cols = []
for s in iris_data["Species"]:
    if s == "setosa": choice=1
    elif s == "versicolor": choice=2
    elif s == "virginica": choice=3
    cols.append(choice)

plt.scatter(iris_data["Sepal.Length"], iris_data["Petal.Length"])
plt.xlabel("Sepal.Length")
plt.xlabel("Petal.Length")
plt.title("iris data")
plt.show()