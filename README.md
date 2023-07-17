# DTization: A new method for feature scaling
This method enables feature scaling based on feature importance.

 How to use: 
- Before using please make sure you have the following libraries installed
    - Numpy
    - Pandas
    - Sklearn
- Clone the github repository using the code below
```  
! git clone git@github.com:NifulIslam/DTization.git
```
- Import DTization
``` python
from DTization import DTization
```
- Create the DTization object. Pass classifier = False if the dataset is for regression. The default is True.
``` python
dtization= new DTization(classifier=True)
```
  
- Now use the object as regular sklearn scalers with fit, transform, fit_transform functions. Just pass and extra dependent variable with it. [Note that once the dependent variable is passed to fit function, no need to pass it again for transform function]

```python
dtization.fit_transform(X_train,y_train)
dtization.transform(X_test)
```
