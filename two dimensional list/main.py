# An empty 2-D list
scores = [[]]

# Get number of students and quizzes
r=int(input("How many students? "))
c=int(input("How many quizzes? "))
#the reason why is because the int is called when getting input 
# Create r empty inner lists to represent each student 
for i in range(r-1):
    scores.append([])

# Insert quiz scores for each student using nested loop
for i in range(r):
    print("Enter scores for student",i+1)
    for j in range(c):
        num=int(input("Enter quiz" + str(j+1) + " score:"))
        scores[i].append(num)

# Display all scores of each student
for i in range(len(scores)):
     print('Student Average ', i+1, 'scores:',end=" ")
     for j in range(len(scores[i])):
         print(scores[i][j],end="  ")
     print()

# Display the average quiz score of each student
for i in range(len(scores)):
    
    Sum = sum(scores[i]) 
    Avg = Sum / (len(scores[i]))
    print('Student', i+1, 'average:', round(Avg , 1))
   
