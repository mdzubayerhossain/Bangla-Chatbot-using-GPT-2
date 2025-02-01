from transformers import TFGPT2LMHeadModel, GPT2Tokenizer
import tensorflow as tf

# Load fine-tuned model & tokenizer
model_path = "model/fine_tuned"
tokenizer = GPT2Tokenizer.from_pretrained(model_path)
model = TFGPT2LMHeadModel.from_pretrained(model_path)

# Set pad token
tokenizer.pad_token = tokenizer.eos_token

def chat():
    print("🤖 Bangla Chatbot (type 'exit' to stop)\n")

    while True:
        text = input("You: ")
        if text.lower() == "exit":
            print("Bot: Bye! 👋")
            break

        # Encode input text
        input_ids = tokenizer.encode(text, return_tensors="tf")
        attention_mask = tf.ones_like(input_ids)  # Fix attention mask issue

        # Generate response
        output = model.generate(
            input_ids,
            attention_mask=attention_mask,  # Fix missing attention mask warning
            max_length=100,
            num_return_sequences=1,  # Generate a single response
            num_beams=5,  # Beam search for better quality
            temperature=0.7,
            top_k=50,  # Restrict vocabulary size
            top_p=0.95,  # Nucleus sampling for diversity
            do_sample=True,  # Enable sampling
            pad_token_id=tokenizer.eos_token_id  # Fix pad token warning
        )

        response = tokenizer.decode(output[0], skip_special_tokens=True)
        print(f"Bot: {response}")

# Start chat
if __name__ == "__main__":
    chat()
