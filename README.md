🎬 Movie Recommendation System

A content-based movie recommendation system built using Python for the CodSoft Internship Task 3.

The system recommends movies based on the similarity between their genres and descriptions. It uses TF-IDF to represent movie content numerically and cosine similarity to identify similar movies.

---

🚀 Features

- 🎬 Movie recommendations
- 🧠 Content-based filtering
- 📊 TF-IDF text representation
- 📐 Cosine similarity
- 🔎 Movie search
- 📋 Available movie list
- ⚠️ Invalid movie handling
- 💻 Command-line interface
- 📦 No external Python packages required

---

🛠️ Technologies Used

- Python 3
- TF-IDF
- Cosine Similarity
- "math" standard library
- "re" standard library

---

📂 Project Structure

Movie-Recommendation-System/
│
├── recommendation_system.py
├── README.md
├── requirements.txt
├── LICENSE
├── CODSOFT_SUBMISSION.md
│
└── screenshots/
    ├── system_start.png
    ├── movie_input.png
    ├── recommendations.png
    └── system_exit.png

---

▶️ How to Run

Make sure Python 3 is installed.

Open Command Prompt or Terminal in the project folder and run:

python recommendation_system.py

---

🎬 Available Movies

The current dataset contains:

- Inception
- Interstellar
- The Matrix
- Avengers: Endgame
- Iron Man
- The Dark Knight
- Spider-Man
- Titanic
- The Notebook
- La La Land
- The Hangover
- Home Alone
- Toy Story
- Finding Nemo
- The Lion King
- The Conjuring
- A Quiet Place
- John Wick
- Mission Impossible
- Top Gun Maverick

---

🧠 How It Works

The system uses content-based filtering.

Movie Dataset
      ↓
Combine Genres + Description
      ↓
Clean and Tokenize Text
      ↓
Calculate TF-IDF
      ↓
Create Movie Vectors
      ↓
Calculate Cosine Similarity
      ↓
Rank Similar Movies
      ↓
Recommend Top Movies

TF-IDF

TF-IDF stands for Term Frequency-Inverse Document Frequency.

It converts important words from movie descriptions and genres into numerical values.

Cosine Similarity

Cosine similarity measures how similar two movie vectors are.

A higher similarity score means the movies have more similar content.

---

💬 Example

==================================================
       MOVIE RECOMMENDATION SYSTEM
==================================================
Content-Based Filtering using TF-IDF

Type 'movies' to see available movies.
Type 'help' for instructions.
Type 'exit' to quit.

Enter a movie you like: Inception

Recommended Movies:
----------------------------------------
1. The Matrix
2. Interstellar
3. A Quiet Place
...

The exact ranking depends on the calculated similarity values.

---

🎯 Recommendation Technique

This project uses content-based filtering rather than collaborative filtering.

The recommendations are based on the characteristics of the selected movie, including:

- Genres
- Description
- Keywords

This means the system does not require information about other users.

---

📚 Concepts Learned

This project helped me practice:

- Python programming
- Text processing
- TF-IDF
- Cosine similarity
- Content-based recommendation
- Lists and dictionaries
- Functions
- Loops
- Conditional statements
- Mathematical calculations
- User input handling
- GitHub project management

---

🔮 Future Improvements

Possible improvements include:

- Larger movie datasets
- Movie ratings
- User profiles
- Collaborative filtering
- Hybrid recommendation
- GUI interface
- Web-based application
- Movie posters and additional information
- Integration with a movie database API

---

🎓 CodSoft Internship

Internship: CodSoft Internship
Task: Task 3 - Recommendation System
Project: Movie Recommendation System
Programming Language: Python
Technique: Content-Based Filtering

---

👨‍💻 Author

Nishesh Raj Singh

BTech CSE (AI/ML) Student
1st Year
GitHub:
https://github.com/yashsingh-07
LinkedIn:
https://www.linkedin.com/in/nishesh-raj-singh-5b5246372/


📄 License

This project is licensed under the MIT License.
