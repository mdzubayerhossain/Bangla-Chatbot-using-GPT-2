#!/bin/bash

echo "Preprocessing data..."
python src/preprocess.py

echo "Training model..."
python src/train.py

echo "Starting chatbot server..."
python src/chatbot.py
