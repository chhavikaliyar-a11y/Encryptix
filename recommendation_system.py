# Install the required library
# pip install scikit-surprise

from surprise import Dataset, Reader, KNNBasic
from surprise.model_selection import train_test_split
from surprise import accuracy

# Load built-in MovieLens dataset
data = Dataset.load_builtin('ml-100k')

# Split into training and testing sets
trainset, testset = train_test_split(data, test_size=0.2)

# Define similarity options
sim_options = {
    'name': 'cosine',
    'user_based': True  # Change to False for item-based filtering
}

# Create collaborative filtering model
algo = KNNBasic(sim_options=sim_options)

# Train model
algo.fit(trainset)

# Predict on test data
predictions = algo.test(testset)

# Evaluate model
print("RMSE:", accuracy.rmse(predictions))

# Predict rating for specific user and movie
user_id = '196'
movie_id = '302'
pred = algo.predict(user_id, movie_id)
print(f"Predicted rating for user {user_id} on movie {movie_id}: {pred.est:.2f}")
