# Bangla Chatbot using GPT-2

This repository contains a fine-tuned GPT-2 model for generating responses in Bangla. The chatbot is designed to handle conversations and provide meaningful replies in Bangla.

## Features
- Fine-tuned Bangla GPT-2 model
- Interactive chatbot interface
- Supports text-based queries
- Easily customizable and extendable

## Installation
To get started, clone this repository and install the required dependencies:

```bash
git clone https://github.com/mdzubayerhossain/Bangla-Chatbot-using-GPT-2.git
cd Bangla-Chatbot-using-GPT-2
pip install -r requirements.txt
```

## Training the Model
To train the chatbot model, run the following command:

```bash
python src/train.py
```

This will fine-tune the GPT-2 model on the provided dataset.

## Running the Chatbot
Once the model is trained, you can start the chatbot using:

```bash
python src/chatbot.py
```

After running the command, the chatbot will prompt you to enter text. You can chat with the bot by typing messages in Bangla.

## Example Usage
```bash
🤖 Bangla Chatbot (type 'exit' to stop)

You: হাই
Bot: হাই! কেমন আছেন?

You: খাবার বড়ি কিভাবে খাব
Bot: খাবার বড়ি সঠিকভাবে গ্রহণের জন্য প্রথমে ... (appropriate response)
```

## Troubleshooting
- If you encounter any issues related to TensorFlow, ensure that your environment is properly configured.
- If you see warnings about `do_sample` or `attention_mask`, check the chatbot script and modify the generation settings accordingly.
- If the bot's responses seem irrelevant, consider retraining the model with a better dataset.

## Contributing
Feel free to contribute to this project by improving the model, fixing bugs, or enhancing the chatbot's functionality. Fork the repository, make your changes, and submit a pull request.

## License
This project is licensed under the MIT License.

## Acknowledgements
- The GPT-2 model used in this project was fine-tuned on Bangla data.
- Inspired by various NLP projects using Hugging Face Transformers.

Happy coding! 🚀

