# Required Libraries
import pandas as pd
from tkinter import *
from tkinter import messagebox
from sklearn.metrics.pairwise import cosine_similarity

# Sample data
user_item_interactions = pd.DataFrame({
    'user_id': [1, 1, 2, 2, 3, 3, 4, 4],
    'item_id': [1, 2, 2, 3, 3, 4, 4, 1]
})

# Function to recommend items for a given user
def recommend_items():
    try:
        # Pivot table to create user-item matrix
        user_item_matrix = pd.pivot_table(user_item_interactions,
                                           index='user_id',
                                           columns='item_id',
                                           aggfunc=len,
                                           fill_value=0)
        
        # Cosine similarity between users
        similarity_matrix = cosine_similarity(user_item_matrix)
        
        # Convert to DataFrame for better readability
        similarity_df = pd.DataFrame(similarity_matrix,
                                     index=user_item_matrix.index,
                                     columns=user_item_matrix.index)

        # Show recommendations for user 1 (example)
        target_user = 1
        recommendations = similarity_df[target_user].sort_values(ascending=False).index.tolist()
        recommendations.remove(target_user)  # Remove the same user
        
        # Prepare output text
        output_text = f"Recommendations for User {target_user}: {recommendations}"
        
        # Terminal print
        print("=== User Similarity Matrix ===")
        print(similarity_df)
        print(output_text)

        # Show in GUI
        messagebox.showinfo("Recommendation", output_text)
    
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Tkinter GUI
root = Tk()
root.title("Recommendation System")

label = Label(root, text="Click button to calculate recommendations")
label.pack(pady=10)

btn = Button(root, text="Recommend", command=recommend_items)
btn.pack(pady=10)

root.mainloop()
