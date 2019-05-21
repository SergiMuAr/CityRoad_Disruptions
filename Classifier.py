from sklearn import svm


class SVMmodel:
    def __init__(self, train_matrix, target):
        self.clf = svm.SVC(tol=0.001, shrinking=True, kernel= 'linear', gamma= 'scale', degree= 2, C= 10).fit(train_matrix, target)

    
    def predictText(self,text):
        return bool(self.clf.predict(text)[0])