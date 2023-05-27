import numpy as np 
import pandas as pd 
from sklearn.tree import DecisionTreeClassifier
class DTization:
    def __init__(self):
        pass
    def get_column_names_by_tree_levels(self, tree, feature_names):
        column_names = []
        max_depth = max(tree.feature)
        for level in range(max_depth + 1):
            level_column_names = []
            queue = [(0, 0)]  

            while queue:
                node, depth = queue.pop(0)

                if depth == level and tree.feature[node] != -2:
                    level_column_names.append(feature_names[tree.feature[node]])

                if depth < level:
                    if tree.children_left[node] != -1:
                        queue.append((tree.children_left[node], depth + 1))
                    if tree.children_right[node] != -1:
                        queue.append((tree.children_right[node], depth + 1))

            column_names.append(level_column_names)

        return column_names
    def fit(self,X,y):
        dt = DecisionTreeClassifier()
        dt.fit(X, y)
        priority= get_column_names_by_tree_levels(dt.tree_,X.columns)
        d=len(X.columns)
        self.x = np.log(2)/d #ln(2)/d
        self.scale={}
        for i, features in enumerate(priority):
            if(len(features)==0):
                continue
            
            for feature in features:
                if(feature in self.scale.keys()):
                    continue
                d_prime = d-i
                self.scale[feature]= np.exp(self.x*d_prime) -1
                
    def transform(self,X,y):
        for column in X.columns:
            x2=X[column].max()
            x1=X[column].min()
            y2= 1
            if(column in self.scale.keys()):
                y2= self.scale[column]
            y1=0
            X[column]=X[column].apply( lambda x : y1+ ((x-x1)*(y1-y2)/(x1-x2)) )
            
    def fit_transform(self, X, y):
        self.fit(X,y)
        self.transform(X,y)
        
