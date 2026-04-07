# Mad Libs Game

print("Welcome to the Mad Libs Game!")
    
    # Get user input for different parts of speech
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
adverb = input("Enter an adverb: ")
    
    # Create a story using the user inputs
story = f"Once upon a time, there was a {adjective} {noun} who loved to {verb} {adverb}."
    
    # Print the final story
print("\nHere's your Mad Libs story:")
print(story)