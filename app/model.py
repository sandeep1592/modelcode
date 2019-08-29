import os
import warnings
import sys
import pickle
import pandas as pd
import numpy as np
import glob
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet

def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    np.random.seed(40)
	
    # Read the wine-quality csv file (make sure you're running this from the root of MLflow!)
    #wine_path = os.path.join(os.path.dirname(os.path.abspath("/home/ec2-user/mlscale/data/winequality.csv")), "winequality.csv")
    data = pd.concat(map(pd.read_csv, glob.glob(os.path.join('/home/ec2-user/mlscale/data', "winequality*.csv"))))
    #data = pd.read_csv(wine_path)
	
    # Split the data into training and test sets. (0.75, 0.25) split.
    train, test = train_test_split(data)
	
    # The predicted column is "quality" which is a scalar from [3, 9]
    train_x = train.drop(["quality"], axis=1)
    test_x = test.drop(["quality"], axis=1)
    train_y = train[["quality"]]
    test_y = test[["quality"]]
    alpha = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
    l1_ratio = float(sys.argv[2]) if len(sys.argv) > 2 else 0.5

lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)
lr.fit(train_x, train_y)
predicted_qualities = lr.predict(test_x)
(rmse, mae, r2) = eval_metrics(test_y, predicted_qualities)
print("Elasticnet model (alpha=%f, l1_ratio=%f):" % (alpha, l1_ratio))
print("  RMSE: %s" % rmse)
print("  MAE: %s" % mae)
print("  R2: %s" % r2)
pickle.dump(lr, open("/model_repo/pickle_model.pkl", 'wb'))





