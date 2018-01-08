# Conditional execution.
print('This is an example of conditional execution.')
print('x = 5')
 # IF statements end in a :
print('if x < 10:')
# Indents are usually 4 spaces
print('    print("Smaller")')
print('if x > 20:')
# Indents are usually 4 spaces
print('    print("Bigger")')
print('print("Finis")')

# Comparision Operators - Evaluate
print('')
print('Boolean expressions ask a question and produce a Yes or No result which')
print('we use to control program flow.')
print('')
print('Boolean expressions using Comparison Operators evaluate to True/False or')
print('Yes / No.')
print('')
print('Comparison operators look at variables but do not change the variables.')
print('')
print('Comparison Operators')
print('< - Less than')
print('<= - Less than or Equal to')
print('== - Equal to')
print('>= - Greater than or Equal to')
print('> - Greater than')
print('!= - Not equal to')
print('')
print('Look at the code below this line in the editor')
x = 5
if x == 5 :
    print('Equals 5')
if x > 4 :
    print('Greater than 4')
if x >= 5 :
    print('Greater than or Equals to 5')
if x <= 5 :
    print('Less than or Equals to 5')
if x != 6 :
    print('Not equal to 6')
print('')
print('Look at the code below this line in the editor')
x = 5
print('Before 5')
if x == 5 :
    print('Is 5')
    print('Is still 5')
    print('Third 5')
print('The next sequential statement')
print('Before 6')
if x == 6 :
    print('Is 6')
    print('Is still 6')
    print('Third 6')
print('The last sequential statement')
print('')

#help(range)
print('Look at the code below this line in the editor')
print('Get help with the "range" function with help("range")')
x = 5
if x > 2 :
    print('Bigger than 2')
    print('Still bigger')
print('Done with 2')

for m in range(5) :
    print(m)
    if m > 2 :
        print('Bigger than 2')
    print('Done with m', m)
print('All done')
print('')
# Two-way Decisions with else / if/else runs one or the other
print('Look at the code below this line in the editor')
x = 0
if x > 2 :
    print('Greater than 2')
else :
    print('Less than 2')
print('All done')
print('')

# Multi-way using elif (else if) /  elif only triggers one part of the block
print('Look at the code below this line in the editor')
x = 0
if x < 2 :
    print('Smaller')
elif x < 10 :
    print('Medium')
else :
    print('Large')
print('All done')



x = 55
if x < 10 :
    print("Smaller")
if x > 20 :
    print("Bigger")
print("")
print("Finis")