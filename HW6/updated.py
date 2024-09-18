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
        user = input('Enter a test score: ')
        if user.isdigit():
            score = int(user)
            if 0 <= score <= 100:
                scores.append(score)
                user_val = input('Do you want to add another score?\ny = yes, anything else = no: ').lower()
                if user_val == 'y':
                    continue
                else:
                    return scores
            else:
                print('Please enter a valid value.')
        else:
            print('Please enter a valid value.')
def get_total(scores):
    scores.remove(min(scores))
    Sum = sum(scores)
    return Sum
def getAverage(total, scores):
    Avg = total / (len(scores))
    return Avg
def display(average):
    print('Average with lowest score dropped:', average)
main()