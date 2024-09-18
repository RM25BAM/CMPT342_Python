def main():
    scores = get_scores()
    if len(scores) == 1:
        print('You entered a single score, the average cannot be calculated.')
    else:
        total = get_total(scores)
        average = getAverage(total, scores)
        display(average)
def get_scores(): 
    scores = []
    while True:
        user = int(input('Enter a test score: '))
        scores.append(user)
        user_val = input('Do you want to add another score?').lower()
        if user_val == 'y':
            continue
        else:
            scores.remove(min(scores))
            return scores
def get_total(scores):
    Sum = sum(scores)
    return Sum
def getAverage(total, scores):
    Avg = total / (len(scores))
    return Avg
def display(average):
    print('Average with lowest score dropped:', average)
main()
"""
for i in range(0, len(scores)):
        if scores[i] > 100:
            print("You entered a score greater than 100. Scores average can't be calculated")
            break
        if scores[i] < 0:
            print("You entered a score less than 0. Scores average can't be calculated")
            break

"""