# BJTU-2023-AI-Project

> 北京交通大学 软件学院 2023春季 人工智能基础课程 专题研究大作业

## 1. 简介

## 2. 安装

### 2.1 Conda

- ```
  conda create -n ai-project python=3.7
  conda activate ai-project
  conda install --yes --file requirements.txt
  ```

## 3. 使用

- `python main.py`

## 4. 项目流程与小组分工

- 搭建原型
  - `已完成`
  - [YXH]

- 数据处理
  - 在原MNIST数据集上新增白底黑字
  - 可选：实现DataAugment,新增旋转数字的数据
  - 本部分功能位于 `main.py` 的 `2. Load Dataset` 片段
  - [ZSY]

- 模型
  - 至少需要2个不同CNN模型
  - 可选：尝试不同参数（增加层、删除层、修改层等）
  - 本部分功能位于 `main.py` 的 `4. Define Model` 片段
  - [YLW]

- Loss函数
  - 本部分功能位于 `main.py` 的 `5. Configure Model` 片段
  - [WW]

- 优化算法
  - 本部分功能位于 `main.py` 的 `5. Configure Model` 片段
  - [YXH]

- 可视化与数据分析

## 5. 注意事项

- 在研究参数和模型的时候，一定要记录下你的结果！
  - 比如你需要记录下：参数、结果Loss、结果Accuracy、运行时间等

## 6. 参考

- [AI-Studio](https://aistudio.baidu.com/aistudio/projectdetail/1514092)
