from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
boston = load_boston()  #获取数据
X = boston.data
y = boston.target
#线性回归模型
hypothesis = LinearRegression(normalize=True)  #生成评估器，评估器依据观测值来预测结果
hypothesis.fit(X,y)  #利用fit方法得到参数
#在 scikit-learn 里面，所有的评估器都带有 fit() 和 predict() 方法。 
#fit() 用来分析模型参数，predict() 是通过 fit() 算出的模型参数构成的模型，对解释变量进行预测获得的值。
print(hypothesis.coef_)
