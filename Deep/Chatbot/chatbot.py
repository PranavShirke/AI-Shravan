import google.generativeai as genai
import tkinter as tk
from tkinter import scrolledtext, Frame, Label, Entry, Button

# Configure Gemini API
GENAI_API_KEY = "AIzaSyDmoG7pgQSdF4N6mnCKvEWcSGUwCcjow90"
genai.configure(api_key=GENAI_API_KEY)

# Chat history storage
chat_history = []

def generate_response(query):
    """Generate response using Gemini AI"""
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        conversation = "\n".join(chat_history[-10:]) + f"\nYou: {query}"  # Keep last 10 exchanges
        response = model.generate_content(conversation, generation_config=genai.GenerationConfig(
            max_output_tokens=300,  # Increased for longer responses
            temperature=0.1,
        ))
        return response.text if response.text else "I'm not sure how to respond to that."
    except Exception as e:
        return f"Sorry, I encountered an error: {e}"

def handle_user_input():
    """Handles user input in the chatbot UI"""
    user_input = entry_field.get().strip()
    if user_input:
        display_message("You", user_input)
        chat_history.append(f"You: {user_input}")
        entry_field.delete(0, tk.END)
        
        response = generate_response(user_input)
        display_message("Jarvis", response)
        chat_history.append(f"Jarvis: {response}")

def display_message(sender, message):
    """Displays a message in the chat area with a formatted look"""
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, f"{sender}:\n", "sender")
    chat_area.insert(tk.END, f"{message}\n\n", "message")
    chat_area.config(state=tk.DISABLED)
    chat_area.yview(tk.END)  # Auto-scroll to latest message

def end_chat():
    """End the chat session."""
    display_message("Jarvis", "Chat ended. Have a great day!")
    root.quit()

def start_chatbot():
    """Initialize the chatbot GUI with an improved interface"""
    global root, chat_area, entry_field
    
    root = tk.Tk()
    root.title("AI Chatbot")
    root.geometry("400x500")
    root.configure(bg="#1e1e1e")
    
    # Chat display area
    chat_frame = Frame(root, bg="#1e1e1e")
    chat_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    
    chat_area = scrolledtext.ScrolledText(chat_frame, wrap=tk.WORD, width=40, height=20, font=("Arial", 12), bg="#2b2b2b", fg="white", state=tk.DISABLED)
    chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    chat_area.tag_configure("sender", font=("Arial", 10, "bold"), foreground="#00bfff")
    chat_area.tag_configure("message", font=("Arial", 12), foreground="white")
    
    # Input and buttons area
    input_frame = Frame(root, bg="#1e1e1e")
    input_frame.pack(pady=5, fill=tk.X)
    
    entry_field = Entry(input_frame, width=30, font=("Arial", 12), bg="#3c3c3c", fg="white", insertbackground="white")
    entry_field.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)
    entry_field.bind("<Return>", lambda event: handle_user_input())
    
    send_button = Button(input_frame, text="Send", font=("Arial", 12), command=handle_user_input, bg="#00bfff", fg="black")
    send_button.pack(side=tk.RIGHT, padx=5)
    
    end_button = Button(root, text="End Chat", font=("Arial", 12), command=end_chat, bg="#ff4d4d", fg="white")
    end_button.pack(pady=5)
    
    root.mainloop()

# Start the chatbot
if __name__ == "__main__":
    start_chatbot()
