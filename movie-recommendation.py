import math
import re

# Movie dataset
movies = [
    {
        "title": "Inception",
        "genres": "science fiction thriller action",
        "description": "A skilled thief enters dreams to steal and plant ideas."
    },
    {
        "title": "Interstellar",
        "genres": "science fiction drama adventure",
        "description": "Astronauts travel through space to find a new home for humanity."
    },
    {
        "title": "The Matrix",
        "genres": "science fiction action thriller",
        "description": "A hacker discovers that reality is a simulated world."
    },
    {
        "title": "Avengers: Endgame",
        "genres": "action adventure science fiction superhero",
        "description": "Superheroes work together to defeat a powerful enemy."
    },
    {
        "title": "Iron Man",
        "genres": "action adventure science fiction superhero",
        "description": "A genius inventor creates a powerful armored suit and becomes a superhero."
    },
    {
        "title": "The Dark Knight",
        "genres": "action crime drama thriller superhero",
        "description": "A superhero faces a dangerous criminal who creates chaos in Gotham."
    },
    {
        "title": "Spider-Man",
        "genres": "action adventure superhero science fiction",
        "description": "A young student gains special powers and becomes a superhero."
    },
    {
        "title": "Titanic",
        "genres": "romance drama",
        "description": "Two people from different backgrounds fall in love during a famous voyage."
    },
    {
        "title": "The Notebook",
        "genres": "romance drama",
        "description": "A couple experiences love, separation and memories throughout their lives."
    },
    {
        "title": "La La Land",
        "genres": "romance drama musical",
        "description": "Two artists pursue their dreams while developing a romantic relationship."
    },
    {
        "title": "The Hangover",
        "genres": "comedy",
        "description": "Friends experience a chaotic night before a wedding."
    },
    {
        "title": "Home Alone",
        "genres": "comedy family",
        "description": "A young boy protects his home from two burglars."
    },
    {
        "title": "Toy Story",
        "genres": "animation comedy family adventure",
        "description": "Toys come to life and experience friendship and adventure."
    },
    {
        "title": "Finding Nemo",
        "genres": "animation adventure family",
        "description": "A father travels across the ocean to find his missing son."
    },
    {
        "title": "The Lion King",
        "genres": "animation adventure family drama",
        "description": "A young lion learns about responsibility and becomes a leader."
    },
    {
        "title": "The Conjuring",
        "genres": "horror thriller mystery",
        "description": "Investigators help a family experiencing frightening supernatural events."
    },
    {
        "title": "A Quiet Place",
        "genres": "horror science fiction thriller",
        "description": "A family tries to survive creatures that hunt by sound."
    },
    {
        "title": "John Wick",
        "genres": "action thriller crime",
        "description": "A retired assassin is forced back into action."
    },
    {
        "title": "Mission Impossible",
        "genres": "action thriller adventure",
        "description": "A skilled agent completes dangerous missions around the world."
    },
    {
        "title": "Top Gun Maverick",
        "genres": "action drama adventure",
        "description": "An experienced pilot trains a new generation of fighter pilots."
    }
]


def clean_text(text):
    """Convert text to lowercase and extract words."""
    return re.findall(r"[a-z]+", text.lower())


def create_vocabulary():
    """Create a vocabulary from all movie information."""
    vocabulary = set()

    for movie in movies:
        text = movie["genres"] + " " + movie["description"]
        vocabulary.update(clean_text(text))

    return sorted(vocabulary)


def term_frequency(words):
    """Calculate term frequency for a document."""
    total_words = len(words)

    if total_words == 0:
        return {}

    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    for word in frequency:
        frequency[word] = frequency[word] / total_words

    return frequency


def calculate_idf(vocabulary):
    """Calculate inverse document frequency."""
    total_documents = len(movies)
    idf = {}

    for word in vocabulary:
        documents_containing_word = 0

        for movie in movies:
            text = movie["genres"] + " " + movie["description"]
            words = set(clean_text(text))

            if word in words:
                documents_containing_word += 1

        idf[word] = math.log(
            (total_documents + 1) /
            (documents_containing_word + 1)
        ) + 1

    return idf


def create_tfidf_vectors():
    """Create TF-IDF vectors for all movies."""
    vocabulary = create_vocabulary()
    idf = calculate_idf(vocabulary)

    vectors = []

    for movie in movies:
        text = movie["genres"] + " " + movie["description"]
        words = clean_text(text)

        tf = term_frequency(words)

        vector = []

        for word in vocabulary:
            value = tf.get(word, 0) * idf[word]
            vector.append(value)

        vectors.append(vector)

    return vocabulary, vectors, idf


def cosine_similarity(vector_a, vector_b):
    """Calculate cosine similarity between two vectors."""
    dot_product = 0
    magnitude_a = 0
    magnitude_b = 0

    for i in range(len(vector_a)):
        dot_product += vector_a[i] * vector_b[i]
        magnitude_a += vector_a[i] ** 2
        magnitude_b += vector_b[i] ** 2

    magnitude_a = math.sqrt(magnitude_a)
    magnitude_b = math.sqrt(magnitude_b)

    if magnitude_a == 0 or magnitude_b == 0:
        return 0

    return dot_product / (magnitude_a * magnitude_b)


def find_movie(movie_name):
    """Find a movie using a case-insensitive search."""
    movie_name = movie_name.lower().strip()

    for i, movie in enumerate(movies):
        if movie["title"].lower() == movie_name:
            return i

    # Also allow partial title matching
    for i, movie in enumerate(movies):
        if movie_name in movie["title"].lower():
            return i

    return None


def recommend_movies(movie_name, number_of_recommendations=5):
    """Recommend similar movies."""
    movie_index = find_movie(movie_name)

    if movie_index is None:
        return None

    _, vectors, _ = create_tfidf_vectors()

    selected_vector = vectors[movie_index]

    similarities = []

    for i, vector in enumerate(vectors):
        if i != movie_index:
            similarity = cosine_similarity(selected_vector, vector)
            similarities.append((similarity, i))

    similarities.sort(reverse=True)

    recommendations = []

    for similarity, index in similarities[:number_of_recommendations]:
        recommendations.append(
            (movies[index]["title"], similarity)
        )

    return recommendations


def show_movies():
    """Display available movies."""
    print("\nAvailable Movies:")
    print("-" * 30)

    for movie in movies:
        print("-", movie["title"])


def show_welcome():
    print("\n" + "=" * 50)
    print("       MOVIE RECOMMENDATION SYSTEM")
    print("=" * 50)
    print("Content-Based Filtering using TF-IDF")
    print("\nType 'movies' to see available movies.")
    print("Type 'help' for instructions.")
    print("Type 'exit' to quit.")


def main():
    show_welcome()

    while True:
        user_input = input(
            "\nEnter a movie you like: "
        ).strip()

        if not user_input:
            print("Please enter a movie name.")
            continue

        command = user_input.lower()

        if command == "exit" or command == "quit":
            print("\nThank you for using the Movie Recommendation System!")
            print("Goodbye!")
            break

        if command == "help":
            print("\nHow to use:")
            print("1. Enter the name of a movie you like.")
            print("2. The system analyzes its content.")
            print("3. Similar movies are recommended.")
            print("\nExample: Inception")
            continue

        if command == "movies":
            show_movies()
            continue

        recommendations = recommend_movies(user_input)

        if recommendations is None:
            print("\nMovie not found.")
            print("Please choose a movie from the available list.")
            continue

        print("\nRecommended Movies:")
        print("-" * 40)

        for rank, (title, similarity) in enumerate(
            recommendations, start=1
        ):
            percentage = similarity * 100
            print(
                f"{rank}. {title} "
                f"(Similarity: {percentage:.2f}%)"
            )

        print("-" * 40)


if __name__ == "__main__":
    main()