#mean subtraction
# 평균의 제곱과 제곱의 평균
score1 = 10
score2 = 20
score3 = 30
n_student = 3

mean = (score1 + score2 + score3)/n_student
square_of_mean = mean**2
mean_of_square = (score1**2 + score2**2 + score3**2)/n_student
print("square of mean:", square_of_mean)
print("mean of square", mean_of_square)

#분산과 표준편차
score1 = 10
score2 = 20
score3 = 30
n_student = 3

score_mean = (score1 +score2 + score3)/n_student
square_of_mean = score_mean**2
mean_of_square = (score1**2 + score2**2 + score3**2)/n_student
score_variance = mean_of_square - square_of_mean
score_std = score_variance ** 0.5
print("mean: ", score_mean)
print("variance: ", score_variance)
print("standard deviation: ", score_std)

# standardization
score1 = 10
score2 = 20
score3 = 30
n_student = 3

score_mean = (score1 +score2 + score3)/n_student
square_of_mean = score_mean**2
mean_of_square = (score1**2 + score2**2 + score3**2)/n_student
score_variance = mean_of_square - square_of_mean
score_std = score_variance ** 0.5
print("mean: ", score_mean)
print("variance: ", score_variance)
print("standard deviation: ", score_std)

score1 = (score1 - score_mean)/score_std
score2 = (score2 - score_mean)/score_std
score3 = (score3 - score_mean)/score_std

score_mean = (score1 + score2 + score3)/n_student
square_of_mean = score_mean**2
mean_of_square = (score1**2+ score2**2 + score3**2)/n_student
score_variance = mean_of_square - square_of_mean
score_std = score_variance**0.5
print("mean: ", score_mean)
print("standard deviation: ", score_std)

# vector-vector operations
x1, y1, z1 = 1, 2, 3
x2, y2, z2 = 3, 4, 5
x3, y3, z3 = x1 + x2, y1 + y2, z1 + z2
x4, y4, z4 = x1 - x2, y1 - y2, z1 - z2
x5, y5, z5 = x1 * x2, y1 * y2, z1 * z2

print(x3, y3, z3)
print(x4, y4, z4)
print(x5, y5, z5)

# scalar-vector operations
a = 10
x1, y1, z1 = 1, 2, 3
x2, y2, z2 = a*x1, a*y1, a*z1
x3, y3, z3 = a+x1, a+y1, a+z1
x4, y4, z4 = a -x1, a-y1, a-z1

print(x2, y2, z2)
print(x3, y3, z3)
print(x4, y4, z4)

# vector norm
x, y, z = 1, 2, 3

norm = (x**2 + y**2 + z**2)**0.5
print(norm)

# making unit vectors
x, y, z = 1, 2, 3

norm = (x**2 + y**2 + z**2)**0.5
print(norm)

x, y, z = x/norm, y/norm, z/norm
norm = (x**2 + y**2 + z**2)**0.5
print(norm)


