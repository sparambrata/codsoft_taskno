import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Define a simple movie dataset
movies = pd.DataFrame({
    'title': [
        'The Matrix', 'The Godfather', 'The Dark Knight', 'Pulp Fiction', 
        'Inception', 'Fight Club', 'Forrest Gump', 'The Shawshank Redemption', 
        'The Avengers', 'The Lord of the Rings'
    ],
    'genres': [
        'Action|Sci-Fi', 'Crime|Drama', 'Action|Crime|Drama', 'Crime|Drama', 
        'Action|Adventure|Sci-Fi', 'Drama', 'Drama|Romance', 'Drama', 
        'Action|Adventure|Sci-Fi', 'Action|Adventure|Fantasy'
    ]
})

def recommend_movies(user_preferences, movies):
    # Convert '|' separated genres into a single space-separated string
    movies['genres'] = movies['genres'].apply(lambda x: ' '.join(x.split('|')))
    
    # Vectorize the genres
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(movies['genres'])
    
    # Create a vector for the user's preferences
    user_vector = vectorizer.transform([user_preferences])
    
    # Compute similarity scores
    cosine_sim = cosine_similarity(user_vector, tfidf_matrix)
    
    # Get the indices of the top recommended movies
    movie_indices = cosine_sim[0].argsort()[::-1]
    
    # Get top 3 movie recommendations
    top_movies = movies.iloc[movie_indices][:3]
    return top_movies

def main():
    print("Welcome to the Simple Movie Recommendation System!")
    
    # Get user preferences
    user_preferences = input("Enter your preferred genres (separated by '|', e.g., 'Action|Sci-Fi'): ")
    
    # Recommend movies
    recommendations = recommend_movies(user_preferences, movies)
    
    # Display recommendations
    print("\nRecommended movies based on your preferences:")
    for idx, row in recommendations.iterrows():
        print(f"- {row['title']}")

if __name__ == "__main__":
    main()
