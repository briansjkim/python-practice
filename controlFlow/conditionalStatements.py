# Write an if statement that lets a competitor know which of these prizes they won based on the number of points they scored, which is stored in the integer variable points

# Points   Prize
# ---------------
# 1-50     wooden rabbit
# 51-150   no prize
# 151-180  wafer-thin mint
# 181-200  penguin

points = 174

if points <= 50:
    result = 'Congratulations! You won a wooden rabbit!'
elif points <= 150:
    result = 'Oh dear, no prize this time.'
elif points <= 180:
    result = 'Congratulations! You won a wafer-thin mint!'
else:
    result = 'Congratulations! You won a penguin!'

print(result)

# Using complex conditional statements
points = 174

prize = None

if points <= 50:
    prize = 'wood rabbit'
elif 150 <= points <= 180:
    prize = 'wafer-thin mint'
elif points >= 181:
    prize = "penguin"

if prize:
    result = 'Congratulations! You have won a {}!'.format(prize)
else:
    result = 'Oh dear, no prize this time.'

print(result)
