import random

quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer",
    "What lies behind us and what lies before us are tiny matters compared to what lies within us. - Ralph Waldo Emerson",
    "The best time to plant a tree was 20 years ago. The second best time is now. - Chinese Proverb",
    "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "Success usually comes to those who are too busy to be looking for it. - Henry David Thoreau",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "Act as if what you do makes a difference. It does. - William James",
    "Success is not in what you have, but who you are. - Bo Bennett",
    "Hardships often prepare ordinary people for an extraordinary destiny. - C.S. Lewis",
    "Your limitation—it's only your imagination.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it.",
    "Success doesn’t just find you. You have to go out and get it.",
    "The harder you work for something, the greater you’ll feel when you achieve it.",
    "Dream bigger. Do bigger.",
    "Don't stop when you're tired. Stop when you're done."
]

facts = [
    "People who are more grateful tend to be happier.",
    "Writing down your thoughts can help clear your mind.",
    "You can't pour from an empty cup; take care of yourself first.",
    "Your mind will believe comforting lies while also seeking powerful truths.",
    "The best way to predict the future is to create it."
]

def display_quote():
    print("Motivational Quote:")
    print(random.choice(quotes))
    print()

def display_fact():
    print("Psychological Fact:")
    print(random.choice(facts))
    print()

def main():
    while True:
        display_quote()
        display_fact()
        again = input("Would you like to see another quote and fact? (y/n): ").lower()
        if again != 'y':
            print("Goodbye!")
            break


main()
