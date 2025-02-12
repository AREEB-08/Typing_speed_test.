🎯 Typing Speed Test 🎯

A simple Python script to measure your typing speed in Words Per Minute (WPM). It calculates the time taken to type a given passage and counts the number of errors made.

✨ Features

✅ Randomly selects a test passage from typing_speed_data.py✅ Measures Typing Speed (WPM)✅ Tracks Errors made while typing✅ Provides detailed feedback on mistakes

🛠️ Requirements

This script requires Python 3 and the following libraries:

📌 Required Libraries

🕒 time (Built-in)

🎲 random (Built-in)

📄 typing_speed_data (Custom module containing test text)

⚙️ Installation & Setup

🔹 1. Install Python (if not installed)

📥 Download and install Python from the official website:🔗 Python Downloads

🔹 2. Clone the Repository

git clone https://github.com/AREEB-08/Typing_speed_test.git
cd Typing_speed_test

🔹 3. Ensure typing_speed_data.py Exists

The script fetches text from typing_speed_data.py, so ensure this file exists and contains sample text.

📜 Example content for typing_speed_data.py:

test = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a popular programming language for data science.",
    "Practice makes perfect, so keep improving your typing speed."
]

🔹 4. Run the Script

🚀 Execute the script using:

python typing_speed.py

🎮 Usage

1️⃣ Run the script.2️⃣ A random passage from typing_speed_data.py will appear.3️⃣ Type the passage exactly as shown and press Enter.4️⃣ The script will display:

🏎 Typing Speed (WPM)

⏳ Time Taken

❌ Errors Count & Details

🖥️ Recommended IDEs & Tools

You can run this script in:

🔥 PyCharm (Recommended)

💻 VS Code

📓 Jupyter Notebook

🖥 Any terminal with Python installed

📊 Example Output

*** Typing Speed Test ***
Python is a popular programming language for data science.

ENTER the text above: Python is a poplar programming langauge for data science.

Results:
🏎 Speed: 40 WPM
⏳ Time taken: 12.34 seconds
❌ Errors: 2

Here are the mistakes you made:
✅ Correct: 'popular' | ❌ You typed: 'poplar'
✅ Correct: 'language' | ❌ You typed: 'langauge'

The correct text was:
Python is a popular programming language for data science.

🤝 Contributing

Feel free to contribute by adding more test passages to typing_speed_data.py or improving the script.

👨‍💻 Author

Developed by Mohammad Areeb Uddin.🛠 GitHub: AREEB-08

📜 License

This project is open-source and available under the MIT License.📄 Feel free to use and modify it!

