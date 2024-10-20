import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

house_df = pd.read_csv('melb_data.csv')

print(house_df.columns)

y = house_df.Price

features = ["Rooms", "Bathroom", "Landsize", "Lattitude", "Longtitude"]

x = house_df[features]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
x_train_scaler = scaler.fit_transform(x_train)
x_test_scaler = scaler.fit_transform(x_test)

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(x_train_scaler.shape[1],)),
    tf.keras.layers.Dense(units=64, activation='relu'),
    tf.keras.layers.Dense(units=1)
])

model.compile(optimizer='sgd', loss='mean_squared_error')

model.fit(x_train_scaler, y_train, epochs=500, validation_data=(x_test_scaler, y_test))

new_data = np.array([[3, 2, 500, -37.8, 145.0]])
new_data_scaled = scaler.transform(new_data)
print(model.predict(new_data_scaled))
