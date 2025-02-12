from time import *
import random
from typing_speed_data import test

def mistake(paratest, usertext):
    error = 0
    for i in range(len(paratest)):
        try:
            if paratest[i] != usertext[i]:
                error += 1
        except IndexError:  # If user input is shorter than the test text
            error += 1
            
    return error

def speed_time(time_s, time_e, userinput):
    time_taken = round((time_e - time_s), 2)
    speed_wpm = (len(userinput) / 5) / (time_taken / 60)  # WPM calculation (standard 5 characters per word)
    return round(speed_wpm), time_taken

def show_errors(paratest, usertext):
    errors = []
    for i in range(min(len(paratest), len(usertext))):
        if paratest[i] != usertext[i]:
            errors.append((paratest[i], usertext[i]))  # Collect correct and incorrect characters
    if len(paratest) > len(usertext):
        errors.append(("Text is too short", ""))
    elif len(paratest) < len(usertext):
        errors.append(("", "Text is too long"))
    
    return errors

# Randomly select one test paragraph
test_text = random.choice(test)
print("*** Typing Speed Test ***")
print(test_text)
print()

# Record typing start time
time_1 = time()

# User input
test_input = input("ENTER the text above: ")
time_2 = time()

# Calculate speed and errors
speed, time_taken = speed_time(time_1, time_2, test_input)
errors_count = mistake(test_text, test_input)
errors = show_errors(test_text, test_input)

# Display results
print("\nResults:")
print(f"Speed: {speed} WPM")
print(f"Time taken: {time_taken:.2f} seconds")  # Display time taken
print(f"Errors: {errors_count}")

# Show detailed errors
if errors_count > 0:
    print("\nHere are the mistakes you made:")
    for correct, wrong in errors:
        if correct and wrong:
            print(f"Correct: '{correct}' | You typed: '{wrong}'")
        elif correct:
            print(f"Missing part: '{correct}'")
        elif wrong:
            print(f"Extra text typed: '{wrong}'")

# Show the correct text if there were mistakes
if errors_count > 0:
    print("\nThe correct text was:")
    print(test_text)
