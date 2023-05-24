# 2023-BJTU-AI-Project

> 北京交通大学 软件学院 2023春季 人工智能基础课程 专题研究大作业

## 1. 简介

## 2. 安装

### 2.1 下载

- ```
  git clone git@github.com:YXHXianYu/2023-BJTU-AI-Project.github
  cd 2023-BJTU-AI-Project
  ```

### 2.2 安装依赖(以Conda为例)

- ```
  conda create -n ai-project python=3.7
  conda activate ai-project
  conda install --yes --file requirements.txt
  ```

### 2.3 安装依赖(以virtualvenv为例)

- ```
  python -m virtualvenv venv --python=python3.7
  # 若为Windows用户, 请自行替换以下命令为 venv/bin/activate.bat 或 venv/bin/activate.ps1
  source venv/bin/activate
  python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements
  ```

- 若想自行将虚拟环境名称从 `venv` 改为 `其他名字`，请将虚拟环境目录添加进 `.gitignore`，避免虚拟环境被提交到github上！

### 2.4 FAQ

- 为什么我提示找不到 `paddlepaddle==2.4.2`?
  - 请确定目前python版本为 `python3.7`
  - 若仍找不到, 请确定使用了清华源: `https://pypi.tuna.tsinghua.edu.cn/simple`

- 为什么我显卡很好，但是跑代码速度很慢?
  - 默认依赖使用基于CPU的paddlepaddle包
  - 若想启用CUDA，请自行将paddlepaddle版本改为gpu版，见 [PaddlePaddle](https://www.paddlepaddle.org.cn/install/quick)

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

## 6. 如何使用Git&Github来修改仓库

### 6.1 直接Push到主分支

- Clone仓库到本地
  - ```
    git clone git@github.com:YXHXianYu/2023-BJTU-AI-Project.git
    cd 2023-BJTU-AI-Project
    ```
- 获取最新的版本（请务必在push前pull最新的版本）
  - ```
    git pull
    ```

- 提交你的修改
  - ```
    git add .
    git commit -m "请写上本次commit的修改内容"
    git push
    ```

### 6.2 先Fork到自己的Github仓库上，再提交Pull Request

- 先在 [主仓库](https://github.com/YXHXianYu/2023-BJTU-AI-Project) 中点击右上角的Fork，将仓库Fork到自己的账户中。

- 打开自己的仓库，点击右上角绿色的 `Code`，选择 `SSH`，并复制SSH链接。

- Clone仓库到本地
  - ```
    git clone YOUR_SSH_URL
    cd 2023-BJTU-AI-Project
    ```

- 添加上游
  - ```
    git remote add upstream git@github.com:YXHXianYu/2023-BJTU-AI-Project.git
    ```

- 获取最新的版本
  - ```
    git pull upstream main
    ```

- 提交你的修改
  - ```
    git add .
    git commit -m "请写上本次commit的修改内容"
    git push
    ```

- 打开你自己的仓库，在你的仓库中点击 `Pull Request` 提交新版本至主仓库

## 7. 参考

- [AI-Studio](https://aistudio.baidu.com/aistudio/projectdetail/1514092)
