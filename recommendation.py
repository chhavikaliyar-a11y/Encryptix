import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Sample data: User-Item interactions
data = {
    'user_id': [1, 1, 1, 2, 2, 3, 3, 3, 4, 4],
    'item_id': [1, 2, 3, 2, 4, 1, 3, 4, 1, 2],
    'rating': [5, 4, 3, 4, 5, 2, 5, 4, 5, 4]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a user-item matrix
pivot_table = df.pivot_table(index='user_id', columns='item_id', values='rating').fillna(0)

# Calculate cosine similarity
similarity_matrix = cosine_similarity(pivot_table)
similarity_df = pd.DataFrame(similarity_matrix, index=pivot_table.index, columns=pivot_table.index)

# Function to get recommendations
def get_recommendations(user_id, num_recommendations=2):
    # Get similarity scores and drop the target user
    similar_users = similarity_df[user_id].drop(index=user_id).sort_values(ascending=False)

    # Get user's rated items
    user_rated_items = pivot_table.loc[user_id]
    items_already_rated = user_rated_items[user_rated_items > 0].index

    # Calculate weighted scores
    scores = pd.Series(dtype=float)
    for other_user_id, similarity_score in similar_users.items():
        other_user_ratings = pivot_table.loc[other_user_id]
        for item in pivot_table.columns:
            if item not in items_already_rated and other_user_ratings[item] > 0:
                if item not in scores:
                    scores[item] = 0
                scores[item] += similarity_score * other_user_ratings[item]

    return scores.sort_values(ascending=False).head(num_recommendations)

# Example usage
user_id = 1
recommendations = get_recommendations(user_id)
print(f"Recommendations for User {user_id}:\n{recommendations}")
