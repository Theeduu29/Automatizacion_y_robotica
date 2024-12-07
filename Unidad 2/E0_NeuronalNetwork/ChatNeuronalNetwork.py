import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from keras.callbacks import EarlyStopping
from keras import regularizers
from keras.layers import Dropout

# Leer los datos
df = pd.read_csv("iris.data")
print(df.head())  # Muestra las primeras 5 filas del dataset

#################################
## Dividir datos en entradas (X) y salidas (y)
X = df.iloc[:, 0:4].values  # Inputs
y = df.iloc[:, 4].values    # Outputs

#################################
## Convertir la variable de salida en etiquetas numéricas
encoder = LabelEncoder()
y1 = encoder.fit_transform(y)

# Convertir las etiquetas en one-hot encoding
Y = pd.get_dummies(y1).values

#################################
### Normalización de los datos
scaler = StandardScaler()
X = scaler.fit_transform(X)

### Dividir en datos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

#################################
# Construir el modelo con capas más profundas, regularización L2 y dropout
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', kernel_regularizer=regularizers.l2(0.01)),
    Dropout(0.5),
    tf.keras.layers.Dense(32, activation='relu', kernel_regularizer=regularizers.l2(0.01)),
    Dropout(0.5),
    tf.keras.layers.Dense(16, activation='relu', kernel_regularizer=regularizers.l2(0.01)),
    tf.keras.layers.Dense(3, activation='softmax')
])

print("Modelo construido:")
print(model.summary())  # Muestra la arquitectura del modelo

#################################
# Compilar el modelo usando Adam como optimizador
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Implementar EarlyStopping para detener el entrenamiento si no mejora
early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

# Entrenar el modelo con batch_size de 64 y early stopping
model.fit(X_train, y_train, batch_size=64, epochs=1000,
          validation_data=(X_test, y_test), callbacks=[early_stopping])

#################################
# Evaluar el modelo
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f'Test loss: {loss}')
print(f'Test accuracy: {accuracy}')

#################################
# Hacer predicciones
y_pred = model.predict(X_test)

# Convertir predicciones y valores reales de one-hot encoding a etiquetas
y_pred_classes = np.argmax(y_pred, axis=1)
y_true = np.argmax(y_test, axis=1)

# Mostrar reporte de clasificación
print("\nReporte de clasificación:")
print(classification_report(y_true, y_pred_classes))
