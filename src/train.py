import tensorflow as tf
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer

# Load tokenizer & model
model_name = "saiful9379/Bangla_GPT2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = TFGPT2LMHeadModel.from_pretrained(model_name)

# Load dataset
with open("data/book.txt", "r", encoding="utf-8") as f:
    text = f.read()

inputs = tokenizer(text, return_tensors="tf", max_length=1024, truncation=True, padding="max_length")

# Convert inputs to TensorFlow dataset
dataset = tf.data.Dataset.from_tensor_slices((inputs["input_ids"], inputs["input_ids"])).batch(4)

# Compile model
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=5e-5),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
)

# Train model
model.fit(dataset, epochs=3)

# Save model
model.save_pretrained("model/fine_tuned")
tokenizer.save_pretrained("model/fine_tuned")

print("✅ Training complete! Model saved.")
