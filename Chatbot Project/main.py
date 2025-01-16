import random
import json
import time
import logging

def load_responses():
    with open('responses.json') as f:
        return json.load(f)

def get_random_agent_name():
    names = ["Alex", "Suresh", "Taylor", "Morgan"]
    return random.choice(names)

def get_random_response():
    responses = ["Interesting, tell me more.", "Can you elaborate?", "I see.", "That's fascinating!"]
    return random.choice(responses)

def get_response(question, responses, user_name):
    key_words = responses.keys()
    for word in key_words:
        if word in question.lower():
            response = responses[word]
            # if random.random() < 0.5:
            #     response = f"{user_name}, {response}"
            return response
    return get_random_response()

def main():
    logging.basicConfig(filename='chat_log.txt', level=logging.INFO)
    responses = load_responses()
    user_name = input("Enter your name: ")
    agent_name = get_random_agent_name()
    print(f"Hello {user_name}! My name is {agent_name}. How can I assist you today?")
    logging.info(f"Agent Name: {agent_name}")
    logging.info(f"User Name: {user_name}")

    while True:
        if random.random() < 0.1:  # 10% chance to randomly disconnect
            print("The connection has been lost. Please try again later.")
            logging.info("Random disconnection occurred.")
            break
        question = input("> ")
        logging.info(f"Question: {question}")
        if question.lower() in ["bye", "quit", "exit"]:
            print("Goodbye!")
            logging.info("Session ended by user.")
            break
        response = get_response(question, responses, user_name)
        print(f"{response}")
        logging.info(f"Response: {response}")
        time.sleep(1)  # Simulate delay in response

if __name__ == "__main__":
     main()
