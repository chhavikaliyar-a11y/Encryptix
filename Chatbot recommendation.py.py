import tkinter as tk
from tkinter import scrolledtext

class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.setup_ui()
        
    def setup_ui(self):
        # Window configuration
        self.root.title("AI Chatbot")
        self.root.geometry("500x600")
        
        # Chat display area
        self.chat_area = scrolledtext.ScrolledText(
            self.root,
            wrap=tk.WORD,
            width=50,
            height=20,
            state='normal'  # Changed from disabled to allow updates
        )
        self.chat_area.pack(pady=10)
        
        # Input frame
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)
        
        # User input field
        self.entry_user_input = tk.Entry(
            input_frame,
            width=40,
            font=('Arial', 12)
        )
        self.entry_user_input.pack(side=tk.LEFT, padx=5)
        self.entry_user_input.bind("<Return>", lambda event: self.send_message())

        # Send button
        self.send_button = tk.Button(
            input_frame,
            text="Send",
            command=self.send_message,
            bg='#4CAF50',
            fg='white',
            relief=tk.RAISED
        )
        self.send_button.pack(side=tk.LEFT)

    def chatbot_response(self, user_input):
        user_input = user_input.lower()
        
        responses = {
            ('hello', 'hi', 'hey'): "Hello! How can I help you today?",
            ('how are you',): "I'm functioning well! How about you?",
            ('your name',): "I'm an AI chatbot assistant.",
            ('bye', 'goodbye', 'exit'): "Goodbye! Have a nice day!",
        }
        
        for keywords, response in responses.items():
            if any(keyword in user_input for keyword in keywords):
                return response
        
        return "I didn't understand that. Could you rephrase or ask something else?"

    def send_message(self):
        user_input = self.entry_user_input.get().strip()
        
        if not user_input:
            return
            
        # Display user message
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, f"You: {user_input}\n")
        
        # Get and display bot response
        response = self.chatbot_response(user_input)
        self.chat_area.insert(tk.END, f"Bot: {response}\n")
        
        # Clear input and auto-scroll
        self.entry_user_input.delete(0, tk.END)
        self.chat_area.see(tk.END)
        self.chat_area.config(state='disabled')
        
        # Exit if goodbye
        if any(word in user_input.lower() for word in ['bye', 'goodbye', 'exit']):
            self.root.after(1500, self.root.destroy)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotApp(root)
    root.mainloop()
