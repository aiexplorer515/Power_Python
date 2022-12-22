# 두 과목의 평균 구하기
math_scores=[40,60,80]
english_scores=[30,40,50]

n_class = 2
n_student=len(math_scores)

score_sums=list()
score_means=list()

for _ in range(n_class):
    score_sums.append(0)
for student_idx in range(n_student):
    score_sums[0] += math_scores[student_idx]
    score_sums[1] += english_scores[student_idx]
print("sum of scores:", score_sums)
for class_idx in range(n_class):
    class_mean = score_sums[class_idx]/n_student
    score_means.append(class_mean)
print("means of scores", score_means)

#mean subteaction
scores=[10,20,30]
score_sum=0
for i in range(len(scores)):
    score_sum +=scores[i]
score_mean = score_sum / len(scores)
scores_ms = list()
for score in scores:
    scores_ms.append(score-score_mean)
print(scores_ms)

for score_idx in range(len(scores)):
    scores[score_idx]-=score_mean
print(scores)


# 수학점수 평균
scores=[10,20,30]

score_sum = 0
n_student=0
for score in scores:
    score_sum += score
    n_student += 1
score_mean = score_sum/n_student
print("score mean", score_mean)

score_sum = 0
for score_idx in range(len(scores)):
    score_sum += scores[score_idx]
score_mean = score_sum / len(scores)
print("score mean:", score_mean)

#두개의 list 접근하기
list1=[10,20,30]
list2=[100,200,300]

for idx in range(len(list1)):
    print(list1[idx], list2[idx])
# for loop list 원소 수정
scores=[10,20,30,40,50]
for score_idx in range(len(scores)):
    scores[score_idx] += 10
print(scores)

# for loop 원소 접근
scores=[10,20,30]

for score in scores:
    print(score)
for score_idx in range(len(scores)):
    print(scores[score_idx])

# 100개의 0을 가진 list
numbers=list()
for _ in range(101):
    numbers.append(0)
print(numbers)

# 1-100 list 만들기
numbers = list()
for i in range(101):
    numbers.append(i)
print(numbers)

# 1-100 sum
num_sum=0
for i in range(101):
    num_sum+=i
print(num_sum)

# iteration 횟수 구하기
numbers=[1,4,5,6,4,2,1]
iter_cnt=0
for _ in numbers:
    iter_cnt += 1
print(iter_cnt)

# 리스트 합
scores=[10,20,30]
score_sum = 0
for score in scores:
    score_sum+=score
print(score_sum)


#for list 원소 접근
scores=[10,20,30]
for score in scores:
    print(score)

#mean squared error
predictions=[10,20,30]
labels=[10,25,40]
n_data=len(predictions)
mse=0
mse+=(predictions[0]-labels[0])**2
mse+=(predictions[1]-labels[1])**2
mse+=(predictions[2]-labels[2])**2
mse /= n_data
print(mse)

# euclidean distance
v1, v2=[1,2,3],[3,4,5]
e_distance=0
e_distance+=(v1[0]-v2[0])**2
e_distance+=(v1[1]-v2[1])**2
e_distance+=(v1[2]-v2[2])**2
e_distance **=0.5
print(e_distance)

#dot product
v1, v2=[1,2,3],[3,4,5]
dot_prod=v1[0]*v2[0]+v1[1]*v2[1]+v1[2]*v2[2]
print(dot_prod)

dot_prod=0
dot_prod += v1[0]*v2[0]
dot_prod += v1[1]*v2[1]
dot_prod += v1[2]*v2[2]
print(dot_prod)

# dot product
v1=[1,2,3]
norm = (v1[0]**2+v1[1]**2+v1[2]**2)**0.5
print(norm)

v1=[v1[0]/norm, v1[1]/norm, v1[2]/norm]
norm = (v1[0]**2+v1[1]**2+v1[2]**2)**0.5
print(norm)

# vector norm
v1=[1,2,3]
norm = (v1[0]**2+v1[1]**2+v1[2]**2)**0.5
print(norm)
norm = 0
norm += v1[0]**2
norm += v1[1]**2
norm += v1[2]**2
norm **=0.5
print(norm)

# hadamard product
v1, v2=[1,2,3],[3,4,5]
v3=list()
v3.append(v1[0]*v2[0])
v3.append(v1[1]*v2[1])
v3.append(v1[2]*v2[2])
print(v3)

# list append
v1=list()
print(v1)
v1.append(1)
print(v1)
v1.append(2)
print(v1)
v1.append(3)
print(v1)

#hadamard product
v1, v2 = [1,2,3], [3,4,5]
v3 = [v1[0]*v2[0], v1[1]*v2[1], v1[2]*v2[2]]
print(v3)

v1, v2 = [1,2,3], [3,4,5]
v3=[0,0,0]

v3[0]=v1[0]*v2[0]
v3[1]=v1[1]*v2[1]
v3[2]=v1[2]*v2[2]
print(v3)
#분산과 표준편차
scores=[10,20,30]
n_student=len(scores)

mean = (scores[0]+scores[1]+scores[2])/n_student
square_of_mean = mean**2
mean_of_square = (scores[0]**2+scores[1]**2+scores[2]**2)/n_student

variance = mean_of_square - square_of_mean
std = variance**0.5
print("score mean:", mean)
print("score standard deviation", std)

#standardization
scores=[10,20,30]
n_student=len(scores)

mean = (scores[0]+scores[1]+scores[2])/n_student
square_of_mean = mean**2
mean_of_square = (scores[0]**2+scores[1]**2+scores[2]**2)/n_student

variance = mean_of_square - square_of_mean
std = variance**0.5
print("score mean:", mean)
print("score standard deviation", std)

#mean subtraction
scores=[10,20,30]
n_student=len(scores)

mean=(scores[0]+scores[1]+scores[2])/n_student
print("score mean:", mean)

scores[0]-=mean
scores[1]-=mean
scores[2]-=mean
mean=(scores[0]+scores[1]+scores[2])/n_student
print("scores mean", mean)

#수학점수 평균구하기
scores=[10,20,30]
n_student=len(scores)

mean = (scores[0]+scores[1]+scores[2])/n_student
print("score mean", mean)

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


# mean squared error
pred1, pred2, pred3 = 10, 20, 30
y1, y2, y3 = 10, 25, 40

n_data =3
s_error1 = (pred1 - y1)**2
s_error2 = (pred2 - y2)**2
s_error3 = (pred3 - y3)**2

mse = (s_error1+s_error2+s_error3)/n_data
print(mse)

#list, 원소접근하기
score=[10,20,30]
print(score[0])
print(score[1])
print(score[2])

#list의 원소수정하기
score=[10,20,30]
print(score)

score[0]=100
score[1]=200
print(score)