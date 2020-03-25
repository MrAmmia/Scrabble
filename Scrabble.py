one_point = ['A','E','I','L','N','O','R','S','T','U']
two_points = ['G','D']
three_points = ['B','C','M','P']
four_points = ['F','H','V','W','Y']
five_points = ['K']
eight_points = ['J','X']
ten_points = ['Q','Z']
word = input("Enter words only ")
score = 0
def word_score(word):
    for elem in word:
        if elem.title() in one_point:
            point = 1
        elif elem.title() in two_points:
            point = 2
        elif elem.title() in three_points:
            point = 3
        elif elem.title() in four_points:
            point = 4
        elif elem.title() in five_points:
            point = 5
        elif elem.title() in eight_points:
            point = 8
        elif elem.title() in ten_points:
            point = 10
        else :
            print("Invalid word")
        global score
        score += point
    return score
x = word_score(word)
print(x)
        
