# ...existing code...
import matplotlib.pyplot as plt

# ...existing code...

history = model.fit(
    x_train, y_train,
    epochs=10,
    validation_data=(x_val, y_val)
)

# Access the history
loss_history = history.history['loss']
val_loss_history = history.history['val_loss']

# Print the loss at each epoch
for epoch, loss in enumerate(loss_history):
    print(f"Epoch {epoch + 1}: Loss = {loss}")

# Plot the loss
plt.plot(loss_history, label='Training Loss')
plt.plot(val_loss_history, label='Validation Loss')
plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.show()

# ...existing code...