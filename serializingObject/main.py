import pickle
phonebook = {'Joanne': '555-1111', 'Chris':'555-2222'}

with open('phonebook.dat','wb') as output_file:
    pickle.dump(phonebook, output_file)
with open('phonebook.dat','rb') as input_file:
    pb=pickle.load(input_file)
print(pb)