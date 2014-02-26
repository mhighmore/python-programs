score = 0

# question 1
ans1 = int(input("How many sides does a triangle have?"))
if ans1 == 3:
    score = score + 1
    print("Well done you now have",score,"score")
else:
    print("Wrong answer, your score is",score)


# question 2
ans2 = int(input("How many sides does a square have?"))
if ans2 == 4:
    score = score + 1
    print("Well done you now have achieved of ",score," points")
else:
    print("Wrong answer, your score is",score)

# now add some more questions (copy and paste some of the code from above)

# question 3
ans2 = input("Who is the the mayor of London?")
if ans2 == "Boris Johnson":
    score = score + 1
    print("Well done you now have",score,"score")
else:
    print("Wrong answer, your score is",score)
