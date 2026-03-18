grades = [1, 3, -2, 4]

def show_grades(grades):
    for g in grades:
        print(g, end=" ")

show_grades(grades)

def grades_sum(grades):
    tot = 0
    for g in grades:
        tot += g
        return tot
    
print("합은", grades_sum(grades))

def grades_ave(grades):
    ave = grades_sum(grades) / len(grades)
    return ave

print("평균은", grades_ave(grades))

def grades_variance(grades):
    ave = grades_ave(grades)
    vari = 0
    for su in grades:
        vari += (su - ave) ** 2
        return vari / len(grades)
        # return vari / len(grades) - 1

print("분산은", grades_variance(grades))
