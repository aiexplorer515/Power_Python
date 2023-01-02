# unit vector
vectors=[[1,11,21],[2,12,22],[3,13,23],[4,14,24]]

n_vector = len(vectors[0])
n_dim = len(vectors)

n_norms = list()
for _ in range(n_vector):
    n_norms.append(0)

for vector in vectors:
    for idx in range(n_vector):
        n_norms[idx] += vector[idx]**2

for idx in range(n_vector):
    n_norms[idx] **= 0.5

print(n_norms)

for dim_idx in range(n_dim):
    for vec_idx in range(n_vector):
        vectors[dim_idx][vec_idx] /= n_norms[vec_idx]

n_norms = list()
for _ in range(n_vector):
    n_norms.append(0)

for vector in vectors:
    for idx in range(n_vector):
        n_norms[idx] += vector[idx]**2

for idx in range(n_vector):
    n_norms[idx] **= 0.5

print(n_norms)
# norm 구하기
vectors=[[1,11,21],[2,12,22],[3,13,23],[4,14,24]]
n_vector = len(vectors[0])

v_norms=list()
for _ in range(n_vector):
    v_norms.append(0)
print(v_norms)

for dim_data in vectors:
    for dim_idx in range(n_vector):
        v_norms[dim_idx] += dim_data[dim_idx]**2
print(v_norms)

for vec_idx in range(n_vector):
    v_norms[vec_idx]**0.5
print(v_norms)

# standardization
scores =[[10,15,20],[20,25,30],[30,35,40],[40,45,50]]

score_sums, score_square_sums = list(), list()
n_class = len(scores[0])
n_student = len(scores)

score_variance, score_std, score_mean=list(), list(), list()
for _ in range(n_class):
    score_sums.append(0)
    score_square_sums.append(0)

for student_idx in range(n_student):
    for class_idx in range(n_class):
        score_sums[class_idx] += scores[student_idx][class_idx]
        score_square_sums[class_idx] += scores[student_idx][class_idx]**2

for class_idx in range(n_class):
    mean_of_square = score_square_sums[class_idx]/n_student
    square_of_mean = (score_sums[class_idx]/n_student)**2

    variance = mean_of_square - square_of_mean
    std = variance**0.5
    score_mean.append(score_sums[class_idx]/n_student)
    score_variance.append(variance)
    score_std.append(std)

print("standard deviations:", score_std)

for student_idx in range(n_student):
    print("stu", student_idx)
    for class_idx in range(n_class):
        print("clss", class_idx)
        scores[student_idx][class_idx] = \
            (scores[student_idx][class_idx]-score_mean[class_idx])/score_std[class_idx]

# 초기화
score_sums, score_square_sums = list(), list()
score_variance, score_std, score_mean=list(), list(), list()

for _ in range(n_class):
    score_sums.append(0)
    score_square_sums.append(0)

for student_idx in range(n_student):
    for class_idx in range(n_class):
        score_sums[class_idx] += scores[student_idx][class_idx]
        score_square_sums[class_idx] += scores[student_idx][class_idx]**2

for class_idx in range(n_class):
    mean_of_square = score_square_sums[class_idx]/n_student
    square_of_mean = (score_sums[class_idx]/n_student)**2

    variance = mean_of_square - square_of_mean
    std = variance**0.5
    score_mean.append(score_sums[class_idx]/n_student)
    score_variance.append(variance)
    score_std.append(std)

print("standard deviations:", score_std)

###
math_scores, english_scores=[50,60,70],[30,40,50]
n_student=len(math_scores)

math_sum, english_sum = 0, 0
math_square_sum, english_square_sum = 0, 0
for i in range(n_student):
    math_sum += math_scores[i]
    english_sum += english_scores[i]
    math_square_sum += math_scores[i]**2
    english_square_sum += english_scores[i]**2

math_mean = math_sum/n_student
english_mean = english_sum/n_student
math_variance = math_square_sum/n_student - math_mean**2
english_variance = english_square_sum/n_student - english_mean**2
math_std = math_variance**0.5
english_std = english_variance**0.5

for student_idx in range(n_student):
    math_scores[student_idx] = (math_scores[student_idx]-math_mean)/math_std
    english_scores[student_idx] = (english_scores[student_idx] - english_mean)/english_std

math_sum, english_sum = 0, 0
math_square_sum, english_square_sum = 0, 0
for i in range(n_student):
    math_sum += math_scores[i]
    english_sum += english_scores[i]
    math_square_sum += math_scores[i]**2
    english_square_sum += english_scores[i]**2

math_mean = math_sum/n_student
english_mean = english_sum/n_student
math_variance = math_square_sum/n_student - math_mean**2
english_variance = english_square_sum/n_student - english_mean**2
math_std = math_variance**0.5
english_std = english_variance**0.5

print("math scores after standardization", math_scores)
print("english scores after standardization", english_scores)
print("mean/std of math", math_mean, math_std)
print("mean/std of english", english_mean, english_std)
# standardization
scores=[10,20,30]
n_student = len(scores)

score_sum = 0
square_sum = 0
for score in scores:
    score_sum += score
    square_sum += score**2
mean = score_sum / len(scores)
square_of_mean = mean**2
mean_of_square = square_sum / len(scores)
variance = mean_of_square - square_of_mean
std = variance**0.5

for student_idx in range(n_student):
    scores[student_idx] = (scores[student_idx]-mean)/std
print(scores)

score_sum = 0
square_sum = 0
for score in scores:
    score_sum += score
    square_sum += score**2

mean = score_sum / len(scores)
square_of_mean = mean**2
mean_of_square = square_sum / len(scores)
variance = mean_of_square - square_of_mean
std = variance**0.5
print(mean, std)

#분산과 표준편차
scores=[10,20,30]
n_student=len(scores)
score_sum, score_square_sum = 0,0

for score in scores:
    score_sum += score
    score_square_sum += score**2

mean = score_sum/n_student
square_of_mean = mean**2
mean_of_square = score_square_sum /n_student

variance = mean_of_square - square_of_mean
std = variance**0.5

print("variance", variance)
print("standard deviation", std)

#mean subtraction
math_scores=[40,60,80]
english_scores=[30,40,50]
n_student=len(math_scores)

score_mean = list()

for i in range(2):
    score_mean.append(0)

m_sum = 0
e_sum = 0
for i in range(len(math_scores)):
    m_sum += math_scores[i]
    e_sum += english_scores[i]
score_mean[0] = m_sum/len(math_scores)
score_mean[1] = e_sum/len(english_scores)

for student_idx in range(n_student):
    math_scores[student_idx] -= score_mean[0]
    english_scores[student_idx] -= score_mean[1]

print("math scores after mean subtractions:", math_scores)
print("English scores after mean subtraction", english_scores)

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


