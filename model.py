from flask import Flask, render_template
from threading import Thread
import tensorflow as tf
from tensorflow.keras import layers, models

app = Flask(__name__)

highest_accuracy = 0.0
epoch_with_highest_accuracy = 0

def train_model():
    global highest_accuracy
    global epoch_with_highest_accuracy

    # Load MNIST dataset
    mnist = tf.keras.datasets.mnist
    (train_images, train_labels), (_, _) = mnist.load_data()

    # Preprocess the data
    train_images = train_images.reshape((60000, 28, 28, 1)).astype('float32') / 255

    # Build the model
    model = models.Sequential()
    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Flatten())
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(10, activation='softmax'))

    # Compile the model
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # Train the model
    for epoch in range(1, 2):  # 5 epochs
        history = model.fit(train_images, train_labels, epochs=1)  # Train for 1 epoch

        # Update highest accuracy if the current accuracy is higher
        accuracy = history.history['accuracy'][0]
        if accuracy > highest_accuracy:
            highest_accuracy = accuracy
            epoch_with_highest_accuracy = epoch

        # Sleep for a short duration to simulate training progress
        # In a real scenario, this would be handled differently
        import time
        time.sleep(2)

@app.route('/')
def home():
    return render_template('index.html', highest_accuracy=highest_accuracy, epoch_with_highest_accuracy=epoch_with_highest_accuracy)

if __name__ == '__main__':
    training_thread = Thread(target=train_model)
    training_thread.start()
    app.run(debug=True)
