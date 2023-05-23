#!/usr/bin/env python
# coding: utf-8

# ===== 1. Import Basic Package =====

import paddle
import numpy as np
import matplotlib.pyplot as plt

paddle.__version__


# ===== 2. Load Dataset =====
import paddle.vision.transforms as T

transform = T.Normalize(mean=[127.5], std=[127.5])

train_dataset = paddle.vision.datasets.MNIST(mode='train', transform=transform)

eval_dataset = paddle.vision.datasets.MNIST(mode='test', transform=transform)

print('训练样本量：{}，测试样本量：{}'.format(len(train_dataset), len(eval_dataset)))


# ===== 3. Display Some Data =====

print('图片：')
print(type(train_dataset[0][0]))
print(train_dataset[0][0].shape)
print('标签：')
print(type(train_dataset[0][1]))
print(train_dataset[0][1])

plt.figure()
plt.imshow(train_dataset[0][0].reshape([28,28]), cmap=plt.cm.binary)
plt.show()

# ===== 4. Define Model =====

import paddle.nn as nn

# Network 1 (LeNet)
network = nn.Sequential(
    nn.Conv2D(in_channels=1, out_channels=6, kernel_size=5, stride=1, padding=0),  # C1 卷积层
    nn.Tanh(),
    nn.AvgPool2D(kernel_size=2, stride=2),  # S2 平局池化层
    nn.Sigmoid(),   # Sigmoid激活函数
    nn.Conv2D(in_channels=6, out_channels=16, kernel_size=5, stride=1, padding=0),  # C3 卷积层
    nn.Tanh(),
    nn.AvgPool2D(kernel_size=2, stride=2),  # S4 平均池化层
    nn.Sigmoid(),  # Sigmoid激活函数
    nn.Conv2D(in_channels=16, out_channels=120, kernel_size=5, stride=1, padding=0), # C5 卷积层
    nn.Tanh(),
    nn.Flatten(),
    nn.Linear(in_features=120, out_features=84), # F6 全连接层
    nn.Tanh(),
    nn.Linear(in_features=84, out_features=10) # OUTPUT 全连接层
)

paddle.summary(network, (1, 1, 32, 32))

# Network 2 (LeNet)
network_2 = nn.Sequential(
    nn.Conv2D(in_channels=1, out_channels=6, kernel_size=3, stride=1, padding=1),
    nn.ReLU(),
    nn.MaxPool2D(kernel_size=2, stride=2),
    nn.Conv2D(in_channels=6, out_channels=16, kernel_size=5, stride=1, padding=0),
    nn.ReLU(),
    nn.MaxPool2D(kernel_size=2, stride=2),
    nn.Flatten(),
    nn.Linear(in_features=400, out_features=120),  # 400 = 5x5x16，输入形状为32x32， 输入形状为28x28时调整为256
    nn.Linear(in_features=120, out_features=84),
    nn.Linear(in_features=84, out_features=10)
)

paddle.summary(network_2, (1, 1, 28, 28))

# Network 3 (LeNet) (using Class)
class LeNet(nn.Layer):
    """
    继承paddle.nn.Layer定义网络结构
    """

    def __init__(self, num_classes=10):
        """
        初始化函数
        """
        super(LeNet, self).__init__()

        self.features = nn.Sequential(
            nn.Conv2D(in_channels=1, out_channels=6, kernel_size=3, stride=1, padding=1),  # 第一层卷积
            nn.ReLU(), # 激活函数
            nn.MaxPool2D(kernel_size=2, stride=2),  # 最大池化，下采样
            nn.Conv2D(in_channels=6, out_channels=16, kernel_size=5, stride=1, padding=0), # 第二层卷积
            nn.ReLU(), # 激活函数
            nn.MaxPool2D(kernel_size=2, stride=2) # 最大池化，下采样
        )

        self.fc = nn.Sequential(
            nn.Linear(400, 120),  # 全连接
            nn.Linear(120, 84),   # 全连接
            nn.Linear(84, num_classes) # 输出层
        )

    def forward(self, inputs):
        """
        前向计算
        """
        y = self.features(inputs)
        y = paddle.flatten(y, 1)
        out = self.fc(y)

        return out

network_3 = LeNet()

paddle.summary(network_3, (1, 1, 28, 28))

# Network 4 (LeNet) (Using API)
network_4 = paddle.vision.models.LeNet(num_classes=10)

paddle.summary(network_4, (1, 1, 28, 28))

# ===== 5. Configure Model =====

# 模型封装
model = paddle.Model(network_4)

# 模型配置
model.prepare(paddle.optimizer.Adam(learning_rate=0.001, parameters=model.parameters()), # 优化器
              paddle.nn.CrossEntropyLoss(), # 损失函数
              paddle.metric.Accuracy()) # 评估指标

# ===== 6. Training =====
model.fit(train_dataset,  # 训练数据集
          eval_dataset,   # 评估数据集
          epochs=5,       # 训练轮次
          batch_size=64,  # 单次计算数据样本量
          verbose=1)      # 日志展示形式

# ===== 7. Evaluating =====
result = model.evaluate(eval_dataset, verbose=1)

print(result)

# ===== 8. Testing (Predicting) =====
result = model.predict(eval_dataset)

# ===== 9. Display Result =====
def show_img(img, predict):
    plt.figure()
    plt.title('predict: {}'.format(predict))
    plt.imshow(img.reshape([28, 28]), cmap=plt.cm.binary)
    plt.show()

# 抽样展示
indexs = [2, 15, 38, 211]

for idx in indexs:
    show_img(eval_dataset[idx][0], np.argmax(result[0][idx]))

