#coding=utf-8

import tensorflow as tf

# 训练数据
X = [[0, 0], [0, 1], [1, 0], [1, 1]]
Y = [[0], [0], [0], [1]]

# 定义网络结构
N_INPUT_NODE = 2  # 2 个输入节点
N_OUTPUT_NODE = 1 # 1 个输出节点

# 定义训练迭代次数
N_STEPS = 20000   # 执行 20000 次训练
N_EPOCH = 1000    # 每隔 1000 次输出一次训练结果

# 定义学习率，即每次递减下降的大小
LEARNING_RATE = 0.02

# 定义接收训练数据的占位符
x_ = tf.placeholder(tf.float32, shape=[len(X), N_INPUT_NODE], name="x-input")
y_ = tf.placeholder(tf.float32, shape=[len(Y), N_OUTPUT_NODE], name="y-input")

# 定义权重值和偏置项
weight = tf.Variable(tf.random_uniform([N_INPUT_NODE, N_OUTPUT_NODE], -1, 1), name="weight")
bias = tf.Variable(tf.zeros(N_OUTPUT_NODE), name="bias")

# 定义向前传播函数
output = tf.sigmoid(tf.matmul(x_, weight) + bias)

# 定义损失函数（最小均方差），描述预测值和真实值之间的差距
cost = tf.reduce_mean(tf.square(Y - output))

# 定义反向传播函数，即使用梯度下降的方法，求解损失函数的最小值
train = tf.train.GradientDescentOptimizer(LEARNING_RATE).minimize(cost)

# 初始化变量
init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)

# 开始训练过程
for i in range(N_STEPS):
    # 执行训练函数，将训练数据 feed 到模型中
    sess.run(train, feed_dict={x_:X, y_:Y})
    if i % N_EPOCH == 0:
        # 每隔 N_EPOCH 轮，输出一次训练结果
        print('STEPS: ', i, ' cost: ', sess.run(cost, feed_dict={x_:X, y_:Y}))

# 训练结束，执行一次预测过程，并查看结果
print('output: ', sess.run(output, feed_dict={x_:X, y_:Y}))
