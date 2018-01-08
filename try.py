score = input('Enter a score between 0.0 and 1.0: ')
try:
    grade = float(score)
except:
    print('That was not a number. Rerun the program or figure out how to loop back to the beginning.')
    quit(True)
if grade < 0.0 :
    print('A number between 0.0 and 1.0!')
elif grade > 1.0 :
    print('A number between 1.0 and 0.0!')
elif grade >= 0.9 :
    print('A')
elif grade >= 0.8 :
    print('B')
elif grade >= 0.7 :
    print('C')
elif grade >= 0.6 :
    print('D')
elif grade < 0.6 :
    print('F')
