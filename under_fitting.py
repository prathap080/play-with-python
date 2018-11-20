from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import pandas as pd

melbourne_data = pd.read_csv(r'.\melb_data.csv')

filtered_melbourne_data= melbourne_data.dropna(axis=0)

y= filtered_melbourne_data.Price

features= ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']

X = filtered_melbourne_data[features]

melbourne_model = DecisionTreeRegressor(random_state=1, max_leaf_nodes= 5000)

train_X, val_X, train_y, val_y = train_test_split(X,y,random_state=0)

melbourne_model.fit(train_X, train_y)

val_predictions= melbourne_model.predict(val_X)

print(mean_absolute_error(val_y,val_predictions))
