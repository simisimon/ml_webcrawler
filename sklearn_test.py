from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC


logistic_reg = LogisticRegression(multi_class="multinomial", solver="lbfgs", C=5)

rnd_forest = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)

ada = AdaBoostClassifier(n_estimators=100)

gNB = GaussianNB()

svm = SVC(gamma='scale', decision_function_shape='ovo')