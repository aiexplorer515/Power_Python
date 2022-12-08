# 구글 Colab 사용하기

## "Google Drive + Jupyter Notebook"

![Google Colaboratory](https://i.imgur.com/sb1REE1.png)



# Google Colab
구글 드라이브 기반 Juputer Noteook  서비스 (2017년 10월 공개)

> "Google Colab = Google Drive + Jupyter Noteook" based on GCP




https://colab.research.google.com (접속하면 바로 소개문서 노트북)

1. Jupyter Notebook 기능 포함 (파이썬 실행, 마크다운, 수식, 차트 표현 등)
1. 구글 드라이브의 문서 생성과 공유 기능 (닥스 문서와 동일한 방법으로 생성, 공유)
1. Github 연계
1. 구글 코랩이 2020년 2월 유료화 정책을 시작(https://colab.research.google.com/signup)하면서 무료 버전에 고용량 RAM 모드를 지원하지 않게 되었습니다.

# 상세 소개
https://colab.research.google.com (접속하면 바로 사용가능)

1. Jupyter Notebook 기능 포함 (파이썬 실행, 마크다운, 수식, 차트 표현 등)
1. 구글 드라이브의 문서 생성과 공유, Github 연계 지원
1. 최신 파이썬, 텐서플로우 지원
1. 구글 클라우드(GCP)기반, 가상머신 서비스인 구글 컴퓨트 엔진(GCE)
1. 딥러닝을 위한 GPU, TPU 지원
1. 사이킷런, 텐서플로우 포함 대부분 파이썬 라이브러리 사전 설치 제공



예제/구글드라이브/깃헙 과 업로드 가능

![](https://i.imgur.com/3cpyxB6.png)

Locate In Drive

사용중인 노트북은 Google Drive 에서 확인 가능하다.

![](https://i.imgur.com/KY3qFpn.png)


```python
import tensorflow as tf
import numpy as np

print(tf.__version__, np.__version__)
```

    2.8.2 1.21.6


# GPU 사용하기
* 노트를 생성한 뒤에 메뉴에서 "런타임 / 런타임 유형 변경" 선택 (그림) <br> 무료 하드웨어 가속기(GPU) 사용도 가능

<img src="https://i.imgur.com/YfSBWIi.png" >


# 환경 설정 정보

* CPU, 메모리, OS, HDD, GPU (K80)
* scipy, numpy, pandas 등 대부분의 파이썬 패키지들이 설치되어 있으며
* scikit-learn, tensorflow, keras 등 머신러닝/딥러닝 라이브러리도 설치



```python
# 디스크 용량
! df -h
```


```python
# CPU
! cat /proc/cpuinfo
```


```python
# 메모리
! cat /proc/meminfo
```


```python
# 파이썬
import sys
sys.version_info  
```


```python
# OS 플랫폼
import platform
platform.platform()

```


```python
# 설치된 파이썬 패키지 목록
import pkg_resources
dists = [d for d in pkg_resources.working_set]
dists
```


```python
! pip list
```


```python

```

# 파일 업로드 다운로드와 드라이브 연결


## 구글 드라이브에서 Colab 연결하기

<img src='https://i.imgur.com/QvmPEvD.png'>

검색에서 colab 를 입력하여 Colaboratory 를 찾고 [+연결] 선택


## 파일 업로드, 다운로드

Google Colab 화면 왼쪽을 펼쳐 Colab에 있는 파일을 로컬 PC에 다운로드

<img src='https://i.imgur.com/xO8SA2O.png' width=400>



```python
# cat.jpg 다운로드
from google.colab import files

files.download('cat.jpg')
```

업로드는 아래와 같이 한다. (이 코드는 Colab의 [코스 스니펫]에 있다)


```python
from google.colab import files

uploaded = files.upload()

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))
```

## 구글 Drive와 연결(mount)하기


```python
from google.colab import drive
drive.mount('/content/drive')
```


```python
with open('/drive/MyDrive/foo.txt', 'w') as f:
  f.write('Hello Google Drive!')
  
!cat "/gdrive/MyDrive/foo.txt"
```

새 노트북 만들기
노트북 이름 바꾸기
노트북 파일 위치 확인
코드 입력하고 실행하기 (Shift + Enter)


## 수식
```
$$c = \sqrt{a^2 + b^2}$$
```
$$c = \sqrt{a^2 + b^2}$$

```
$$N(\mu ,\sigma )$$
```
$$N(\mu ,\sigma )$$

# 간단한 차트 그리기


```python

```


```python
import numpy as np

data = np.random.randint(-100, 100, 50)
data
```


```python
import matplotlib.pyplot as plt

plt.plot(data.cumsum())
plt.show()
```

## curl 명령으로 파일 가져오기
위 이미지 링크를 wget 명령으로 가져와 보자

! 를 쓰고 명령을 써준다. 

아래 예는 curl 명령으로 특정 URL의 이미지를 cat.jpg 로 저장하는 예 이다.

```
! curl -o cat.jpg https://amp.businessinsider.com/images/5a69a3d400d0efc1008b4754-960-480.jpg

! ls -l
```

## 코랩: 한글 폰트 설치

1. 한글 폰트 설치

```sh
#폰트 설치
! apt install fonts-nanum*
```

```sh
! apt install fontconfig
```

2. 폰트 캐시 생성

```sh
#폰트 캐시 생성
!fc-cache -fv
```

3. matplotlib에 남아있는 font 캐시 삭제

```sh
# matplotlib에 남아있는 font 캐시 삭제
!rm -rf ~/.cache/matplotlib/*
```

4. Runtime 재실행

5. matplotlib 에서 Nanum 한글 폰트 검색 확인

```python
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 폰트 목록에서 폰트 찾기
for font in fm.fontManager.ttflist:
    if 'Nanum' in font.name:
        print(font.name, font.fname)
```

### matplotlib 한글 확인


```python
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
%matplotlib inline
```


```python
# 폰트 목록에서 폰트 찾기
for font in fm.fontManager.ttflist:
    if 'Nanum' in font.name:
        print(font.name, font.fname)
```


```python
# 전역 폰트 설정 사용
# font_path = 'C:/Windows/Fonts/NanumGothic.ttf'
# font_path = '/Users/qkboo/Library/Fonts/NanumGothic.otf'
font_path = "/usr/share/fonts/truetype/nanum/NanumGothic.ttf"

fontname = fm.FontProperties(fname=font_path, size=18).get_name()  # 폰트 패밀리 이름!
# plt.rc('font', family=fontname)
plt.rcParams["font.family"] = fontname
plt.rcParams["font.size"] = 12

# matplotlib 설정
plt.rcParams["axes.grid"] = True
plt.rcParams["figure.figsize"] = (10,3)
plt.rcParams["axes.formatter.useoffset"] = False
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams["axes.formatter.limits"] = -10000, 10000

plt.title('한글 타이틀...')
```


```python

```

# TensorFlow 2.0


```python
%tensorflow_version 2.x
```

    UsageError: Line magic function `%tensorflow_version` not found.



```python
# GPU 사용 가능 확인 ( "/device:GPU:0" 문자열이 반환되면 GPU 사용 가능함 의미)

import tensorflow as tf
device_name = tf.test.gpu_device_name()
device_name
```

# 케라스 MNIST(손글씨 인식)

https://elitedatascience.com/keras-tutorial-deep-learning-in-python


```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Convolution2D, MaxPooling2D
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

import matplotlib.pyplot as plt
from datetime import  datetime

(X_train, y_train), (X_test, y_test) = mnist.load_data()

print("X_train shape", X_train.shape)
print("y_train shape", y_train.shape)
```

    X_train shape (60000, 28, 28)
    y_train shape (60000,)



```python

for i in range(9):
    plt.subplot(3,3,i+1)
    plt.imshow(X_train[i], cmap='gray', interpolation='none')
    plt.title("Class {}".format(y_train[i]))
```


    
![png](output_46_0.png)
    



```python
X_train = X_train.reshape(X_train.shape[0], 1, 28, 28)
X_test = X_test.reshape(X_test.shape[0], 1, 28, 28)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255
 
Y_train = to_categorical(y_train, 10)
Y_test = to_categorical(y_test, 10)
 
model = Sequential()
model.add(Convolution2D(32, (3, 3), activation='relu', 
                        input_shape=(1,28,28), 
                        data_format='channels_first'))
model.add(Convolution2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
 
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))
 
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
 
start = datetime.now()
model.fit(X_train, Y_train, 
          batch_size=32, epochs=10, verbose=1)

print('Elapsed time :', datetime.now() - start)
```

    Epoch 1/10
    1875/1875 [==============================] - 7s 3ms/step - loss: 0.2558 - accuracy: 0.9237
    Epoch 2/10
    1875/1875 [==============================] - 6s 3ms/step - loss: 0.1024 - accuracy: 0.9700
    Epoch 3/10
    1875/1875 [==============================] - 6s 3ms/step - loss: 0.0808 - accuracy: 0.9765
    Epoch 4/10
    1875/1875 [==============================] - 6s 3ms/step - loss: 0.0652 - accuracy: 0.9801
    Epoch 5/10
    1875/1875 [==============================] - 6s 3ms/step - loss: 0.0555 - accuracy: 0.9829
    Epoch 6/10
    1875/1875 [==============================] - 6s 3ms/step - loss: 0.0500 - accuracy: 0.9845
    Epoch 7/10
    1875/1875 [==============================] - 6s 3ms/step - loss: 0.0445 - accuracy: 0.9858
    Epoch 8/10
    1875/1875 [==============================] - 6s 3ms/step - loss: 0.0391 - accuracy: 0.9878
    Epoch 9/10
    1875/1875 [==============================] - 6s 3ms/step - loss: 0.0364 - accuracy: 0.9884
    Epoch 10/10
    1875/1875 [==============================] - 6s 3ms/step - loss: 0.0328 - accuracy: 0.9899
    Elapsed time : 0:01:00.603713



```python
score = model.evaluate(X_test, Y_test, verbose=0)

print('Test score:', score[0])
print('Test accuracy:', score[1])
```

    Test score: 0.030788956210017204
    Test accuracy: 0.991599977016449


# 구글 Colab 요약
* 사양: 80G HDD 공간, 2.3GHz Xeon CPU, 13G 메모리 (우분투 18.04)
* Tensorflow, SciKit learn 등 다양한 라이브러리 기본 설치
* GPU 지원
* CNN 예제 GPU 미사용시 46분 57초, GPU사용시 3분 42초 소요 (10배 이상 빠르다) 
* 필요한 패키지 추가 설치 가능 (pip)
* 구글 드라이브와 연동


---

