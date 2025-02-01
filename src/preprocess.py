import re

def prepare_data(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    formatted_text = ""
    for line in lines:
        line = line.strip()
        if line:
            formatted_text += f"{line} </s> "

    return formatted_text

# Save processed data
with open("data/processed_chat_data.txt", "w", encoding="utf-8") as f:
    f.write(prepare_data("data/chat_data.txt"))
