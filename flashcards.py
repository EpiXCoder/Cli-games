# flashcards.py
import json

with open('me-capitals.json', 'r') as f:
    data = json.load(f)

# initialize total as the length of the cards array
total = len(data["cards"])
# initialize score as 0
score = 0

for i in data["cards"]:
    guess = input(i["q"] + " > ")

    if guess.lower() == i["a"].lower():
        # increment score up one
        score += 1
        # interpolate score and total into the response
        print(f"Correct! Current score: {score}/{total}")
    else:
        print("Incorrect! The correct answer was", i["a"])
        print(f"Current score: {score}/{total}")

if score < (total/2):
    print(f"Thanks for playing! You scored {score} out of {total} correct. You need practice!")
elif score> (total/2) and score < total:
    print(f"Thanks for playing! You scored {score} out of {total} correct. Good work!")
elif score==total:
    print(f"Thanks for playing! You scored {score} out of {total} correct. Perfect Score! Amazing!")
