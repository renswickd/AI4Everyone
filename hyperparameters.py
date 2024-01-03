import numpy as np


parameter_dict = {
    "KNN" : {
                'n_neighbors':[3,5,7,9,11],
                'metric':["euclidean","manhattan","chebyshev","minkowski"]
            },
    "SVM" : {
                'kernel':['linear', 'poly', 'rbf'],
                'C':[1,2,3,4,5],
                'gamma':['scale','auto']
            },
    "Decision Tree" : {
                'criterion': ['gini', 'entropy'],
                'max_depth': [None, 5, 10, 15, 20],
                'min_samples_split': [2, 5, 10],
                'min_samples_leaf': [1, 2, 4]
    },
    "Random forest" : {
                'n_estimators': [100, 200, 300],
                'max_depth': [None, 10, 20, 30],
                'min_samples_split': [2, 5, 10],
                'min_samples_leaf': [1, 2, 4]
    },
    "Naive Bayes" : {
                'var_smoothing': np.logspace(0,-9, num=10)[:4].tolist()
    }
}

# model_dict = {
#     'KNN' : 
# }

