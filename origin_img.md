## 将图像分为8个类别，
图像分布：
train 34862 images; batch=10  test_interval=3500
test  2485  images; batch=20  test_iter=125

8类labes are:

### 0    hand_on_gear
### 1    eat_something
### 2    without_hand
### 3    single_hand
### 4    without_safety_belt
### 5    telephone
### 6    normal
### 7    smoking
## 训练正确率最高为0.95，测试准确率如下：
### use origin image, without segment, 
### hand_on_gear accuracy is 0.9740
### eat_something accuracy is 0.6667
### without_hand accuracy is 0.7909
### single_hand accuracy is 0.9434
### without_safety_belt accuracy is 1.0
### telephone accuracy is 0.9325
### normal accuracy is 0.9649
### smoking accuracy is 0.8894

# average accuracy is 0.9493
### time 177.89s
### 2359 test images.
# 经进一步测试，感觉略有过拟合。主要是驾驶员个数太少。

接下来，尝试通过pose keypoint detection，segmentation等进一步实验。


