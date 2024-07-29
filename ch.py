# Simple Chatbot Class

class SimpleChatbot:
    def __init__(self):
        """
        Initialize the Simple Chatbot with a set of predefined responses.

        The responses are stored in a dictionary, where each key is a keyword
        and the value is the corresponding response.
        """
        self.responses = {
            "hi": "Hi there!",  # Response to "hello"
            "how are you": "I'm doing well. How can I help you?",  # Response to "how are you"
            "name": "I'm a jalgaar.",  # Response to "name"
            "bye": "Goodbye! Have a great day!"  # Response to "bye"
        }

    def get_response(self, user_input):
        """
        Get a response to a user's input.

        Parameters:
        user_input (str): The user's input.

        Returns:
        str: The response to the user's input.
        """
        user_input = user_input.lower()  # Convert the input to lowercase for case-insensitive matching
        for keyword in self.responses:
            if keyword in user_input:  # Check if the keyword is in the user's input
                return self.responses[keyword]  # Return the corresponding response
        return "I'm sorry, I don't understand that."  # Return a default response if no keyword is found

# Create an instance of the Simple Chatbot
bot = SimpleChatbot()

# Start the chatbot conversation
print("Chatbot: Hello! How can I assist you today?")

while True:
    user_input = input("You: ")  # Get the user's input
    if "bye" in user_input.lower():  # Check if the user wants to exit
        print("Chatbot:", bot.get_response("bye"))  # Respond with a goodbye message
        break  # Exit the loop
    print("Chatbot:", bot.get_response(user_input))  # Respond to the user's input