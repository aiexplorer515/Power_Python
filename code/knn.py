import numpy as np

v1 = np.array([5.00, 2.50])
v2 = np.array([5.25, 9.50])
# Manhattan
m_dis = np.sum(abs(v1-v2))
print("Manhattan:" , m_dis)

# Euclidean
e_dis = np.sqrt(np.sum((v1-v2)**2))
print("Euclidean:", round(e_dis, 4))
====================================
import numpy as np

instances = np.array([[5., 2.5, 3], [2.75, 7.50, 4],
                      [9.10, 4.5, 5], [8.9, 2.3, 6]])

test_instance = instances[0]

distances=[]

for instance in instances:
    distance = np.sqrt(np.sum((instance-test_instance)**2))
    distances.append(distance)
print(distance)

# column based
instances = np.array([[5., 2.5, 3], [2.75, 7.50, 4],
                      [9.10, 4.5, 5], [8.9, 2.3, 6]])

test_instance = instances[:, 0]
n_cols = instances.shape[1]
distances = []

for col_idx in range(n_cols):
    instance = instances[:, col_idx]
    distance = np.sqrt(np.sum((instance - test_instance)**2))
    distances.append(distance)
print(distances)

=======================
import numpy as np

instances = np.array([[5., 2.5, 3], [2.75, 7.50, 4],
                      [9.10, 4.5, 5], [8.9, 2.3, 6]])

test_instance = instances[0]

distances=[]

for instance in instances:
    distance = np.sqrt(np.sum((instance-test_instance)**2))
    distances.append(distance)
print(distance)


======
instances = [[5.00, 2.50], [2.75, 7.50]]

diff = 0

for dim_idx in range(len(instances[0])):
    diff += (instances[0][dim_idx] - instances[1][dim_idx])**2
e_distance = diff**0.5
print(e_distance)

abs_sum = 0
for dim_idx in range(len(instances[0])):
    diff = instances[0][dim_idx] - instances[1][dim_idx]
    if diff < 0:
        abs_sum += -diff
    elif diff >= 0:
        abs_sum += diff
m_distance = abs_sum
print(m_distance)


# Manhattan
import numpy as np
v1 = [1, 3, 5, 2, 1, 5, 2]
v2 = [2, 3, 1, 5, 2, 1, 3]
v3=abs(np.array(v1)-np.array(v2))
print(np.sum(v3))

# Euclidean Distance
vectors = [[1, 11], [2, 12],[3, 13],[4, 14]]
v1 = np.array([[1, 11], [2, 12],[3, 13],[4, 14]])
v_euc = (v1[:,0]-v1[:,1])**2
e_distance = np.sqrt(np.sum(v_euc))
print(e_distance)



v1 = np.array([2.75, 7.50])
v2 = np.array([5.00, 2.50])
v_mul = [2]
# Manhattan
v3 = abs(v1-v2)
m_dis = np.sum(v3)
print(m_dis)

# Euclidean
v_diff_rad = (v1-v2)**2
e_dis = np.sqrt(np.sum(v_diff_rad))
print(round(e_dis, 4))