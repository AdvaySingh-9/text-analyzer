import tkinter as tk
from tkinter import scrolledtext
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
from collections import Counter

#Download required NLTK resources
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('vader_lexicon')

# Function to analyze text
def analyze_text():
    text = input_text.get("1.0", tk.END)

    if not text.strip():
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Please enter some text.")
        return
    
    sentences = sent_tokenize(text)
    words = word_tokenize(text)

    stop_words = set(stopwords.words("english"))
    filtered_words = [w.lower() for w in words if w.isalpha() and w.lower() not in stop_words]

    word_frequency = Counter(filtered_words)
    common_words = word_frequency.most_common(5)

    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)

    # Determine sentiment category
    if sentiment['compound'] >= 0.05:
        sentiment_category = "Positive"
    elif sentiment['compound'] <= 0.05:
        sentiment_category = "Negative"
    else:
        sentiment_category = "Neutral"

    # Display results
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, f"Total Sentences: {len(sentences)}\n")
    result_text.insert(tk.END, f"Total Words: {len(words)}\n")
    result_text.insert(tk.END, f"Top 5 common words & there frequencies\n")
    for word, freq in common_words:
        result_text.insert(tk.END, f"{word} -> {freq}\n")

    result_text.insert(tk.END, f"Sentiment: {sentiment_category}\n")
    result_text.insert(tk.END, f"Detailed Score: {sentiment}\n")

# GUI Window
root = tk.Tk()
root.title("Text Analyzer")
root.geometry("700x500")
root.configure(bg="#000086")

# Title
title = tk.Label(root, text="Text Analyzer", font=("Rockwell", 24, "bold"), bg="#f0f4f7")
title.pack(pady=10)

# Input box
input_label = tk.Label(root, text="Enter text:", font=("Arial", 14), bg="#f0f4f7")
input_label.pack()

input_text = scrolledtext.ScrolledText(root, height=8, width=50, font=("Arial", 12))
input_text.pack(pady=10)

# Button
analyze_btn = tk.Button(root, text="analyze", font=("Arial", 11, "bold"), bg="#00ff00", fg="white", padx=10, pady=5, command=analyze_text)
analyze_btn.pack(pady=10)

# Output Box

result_label = tk.Label(root, text="Result:", font=("Arial", 14), bg="#f0f4f7")
result_label.pack()

result_text = scrolledtext.ScrolledText(root, height=12, width=50, font=("Arial", 11))
result_text.pack(pady=10)

# Run the app
root.mainloop()