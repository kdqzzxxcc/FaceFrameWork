# coding=utf-8
__author__ = 'DELL'
from sklearn.decomposition import PCA
import numpy as np
import cv2
from sklearn.externals import joblib
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
import pandas as pd
from sklearn import cross_validation
from detect_face import process as detec_process
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing
PCA_MODEL = None
SVM_MODEL = None
GABOR_FILTER = None
image_size = 48

def init():
    global GABOR_FILTER, PCA_MODEL, SVM_MODEL
    GABOR_FILTER = build_filter(image_size)
    PCA_MODEL = joblib.load('./model/pca.pkl')
    SVM_MODEL = joblib.load('./model/svm.pkl')


# 5个尺度 8 个方向的 gabor filter
def build_filter(img_size):
    filters = []
    for lamd in np.arange(1, 16, 3):
        for thea in np.arange(0, np.pi, np.pi / 8):
            kern = cv2.getGaborKernel((img_size, img_size), sigma=4, theta=thea, lambd=lamd, gamma=10, psi=0.5, ktype=cv2.CV_32F)
            kern /= 1.5 * kern.sum()
            filters.append(kern)
    return filters


# 使用5 * 8 的gabor filter对图像进行处理
def process(img, filters):
    # results = np.zeros((1, 256* 256 * 40))
    # results[0,1] = 1
    result = np.zeros((1, img.shape[0] * img.shape[0] * 40))
    bound = 0
    spn = img.shape[0] * img.shape[0]

    for kern in filters:
        fimg = cv2.filter2D(img, cv2.CV_8UC3, kern)
        # cv2.imshow('test', fimg)
        # cv2.waitKey(1000)
        fimg = fimg.reshape(1,fimg.shape[0]*fimg.shape[1])
        result[0,bound:bound+spn] = fimg
        bound = bound + spn

    return preprocessing.normalize(result)

def get_classification(train_x, train_y):
    svc = SVC(C=100, cache_size=500, class_weight='auto', coef0=0.0, degree=3, gamma=1.0000000000000001e-04,
              kernel='linear',
              max_iter=-1, probability=False, random_state=None, shrinking=True, tol=0.001, verbose=False)
    model = OneVsRestClassifier(svc)
    model.fit(train_x, train_y)
    joblib.dump(model, './model/svm.pkl')
    # return model.predict(test)


def get_pca():
    f = open('./data/all_names.txt','r')
    filters = build_filter(image_size)
    count = 0
    results = np.zeros((213, image_size * image_size * 40))
    while True:
        line = f.readline()
        if len(line):
            line = line.strip('\n')
            g = cv2.imread('./JAFFE1/'+str(line)+'.jpg', 0)
            results[count, :] = process(img=g, filters=filters)
            count = count + 1
        else:
            break
    # results = 213 * (48 * 48 * 40)
    # results = preprocessing.normalize(results)
    # results = preprocessing.scale(results)
    Pca = PCA(n_components=213)
    Pca.fit(X=results)
    joblib.dump(Pca, './model/pca.pkl')
    # new_data = Pca.transform(results)
    # np.savetxt('train.csv', new_data, delimiter=',')

# 8-folds cross validation
def cross_validation_score(train, label):
    kfold = cross_validation.KFold(len(label), n_folds = 8, shuffle = True)
    model = joblib.load('./model/svm.pkl')
    scores = cross_validation.cross_val_score(estimator=model, cv=kfold, n_jobs=4, X=train, y=label)
    print scores
    print sum(scores) / len(scores)


def run_algorithm(file_path):
    file_path = detec_process(file_path)
    if file_path == None:
        return None
    g = cv2.imread(file_path, 0)
    test = process(g, GABOR_FILTER)
    test = PCA_MODEL.transform(X=test)
    return SVM_MODEL.predict(test)


def get_model():
    get_pca()
    train_x = pd.read_csv('./data/train.csv', header = 0)
    train_y = pd.read_csv('./data/label.csv', header = 0)
    get_classification(train_x.values, train_y.values)
    # cross_validation_score(train_x.values, train_y.values)

# 随机森林分类器
def train_random_forest():
    train_x = pd.read_csv('./data/train.csv', header = 0)
    train_y = pd.read_csv('./data/label.csv', header = 0)
    forest = RandomForestClassifier(n_estimators=100)
    forest.fit(train_x.values, train_y.values)
    kfold = cross_validation.KFold(len(train_y.values), n_folds = 8, shuffle = True)
    scores = cross_validation.cross_val_score(estimator=forest, cv=kfold, n_jobs=4, X=train_x.values, y=train_y.values)
    print scores , sum(scores) / len(scores)

# k近邻分类器
def train_knn():
    train_x = pd.read_csv('./data/train.csv', header = 0)
    train_y = pd.read_csv('./data/label.csv', header = 0)
    knn = KNeighborsClassifier(algorithm='auto', n_neighbors=5, weights='distance')
    knn.fit(train_x.values, train_y.values)
    kfold = cross_validation.KFold(len(train_y.values), n_folds = 8, shuffle = True)
    scores = cross_validation.cross_val_score(estimator=knn, cv=kfold, n_jobs=4, X=train_x.values, y=train_y.values)
    print scores , sum(scores) / len(scores)

# 测试不同kernel的svm的交叉验证率，并没有本质上的差距
def train_different_svm():
    train_x = pd.read_csv('./data/train.csv', header = 0)
    train_y = pd.read_csv('./data/label.csv', header = 0)
    kfold = cross_validation.KFold(len(train_y), n_folds = 8, shuffle = True)

    svc = SVC(C=100, cache_size=500, class_weight='auto', coef0=0.0, degree=3, gamma=1.0000000000000001e-04,
              kernel='rbf',
              max_iter=-1, probability=False, random_state=None, shrinking=True, tol=0.001, verbose=False)
    model = OneVsRestClassifier(svc)
    model.fit(train_x, train_y)
    scores = cross_validation.cross_val_score(estimator=model, cv=kfold, n_jobs=4, X=train_x, y=train_y)
    print "rbf kernel",sum(scores) / len(scores), model.score(train_x, train_y)

    svc = SVC(C=100, cache_size=500, class_weight='auto', coef0=0.0, degree=3, gamma=1.0000000000000001e-04,
              kernel='linear',
              max_iter=-1, probability=False, random_state=None, shrinking=True, tol=0.001, verbose=False)
    model = OneVsRestClassifier(svc)
    model.fit(train_x, train_y)
    scores = cross_validation.cross_val_score(estimator=model, cv=kfold, n_jobs=4, X=train_x, y=train_y)
    print "linear kernel",sum(scores) / len(scores), model.score(train_x, train_y)

    svc = SVC(C=100, cache_size=500, class_weight='auto', coef0=0.0, degree=3, gamma=1.0000000000000001e-04,
              kernel='poly',
              max_iter=-1, probability=False, random_state=None, shrinking=True, tol=0.001, verbose=False)
    model = OneVsRestClassifier(svc)
    model.fit(train_x, train_y)
    scores = cross_validation.cross_val_score(estimator=model, cv=kfold, n_jobs=4, X=train_x, y=train_y)
    print "poly kernel",sum(scores) / len(scores), model.score(train_x, train_y)

    svc = SVC(C=100, cache_size=500, class_weight='auto', coef0=0.0, degree=3, gamma=1.0000000000000001e-04,
              kernel='sigmoid',
              max_iter=-1, probability=False, random_state=None, shrinking=True, tol=0.001, verbose=False)
    model = OneVsRestClassifier(svc)
    model.fit(train_x, train_y)
    scores = cross_validation.cross_val_score(estimator=model, cv=kfold, n_jobs=4, X=train_x, y=train_y)
    print "sigmoid kernel",sum(scores) / len(scores), model.score(train_x, train_y)

if __name__ == '__main__':
    # for i in range(1,5):
    #     train_different_svm()
    # train_knn()
    # train_random_forest()
    get_model()
    # a = np.array([[1,2,3]],dtype=np.float)
    # a = preprocessing.normalize(a)
    # print a
