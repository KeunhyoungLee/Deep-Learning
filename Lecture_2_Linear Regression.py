# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iY6enAQsa5vAu_kJcDFDrcV-lEP0-fxZ

### **01.** Basic
"""

import tensorflow as tf

hello = tf.constant("Hello, TensorFlow!")

sess = tf.Session()

print(sess.run(hello))

[1. ,2., 3.] 
[[1., 2., 3.], [4., 5., 6.]]
[[[1., 2., 3.]], [[7., 8., 9.]]]

node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0)
node3 = tf.add(node1, node2)

print("node1:", node1, "node2:", node2)
print("node3: ", node3)

sess = tf.Session()

print("sess.run(node1, node2): ", sess.run([node1, node2]))
print("sess.run(node3): ", sess.run(node3))

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)

adder_node = a + b  

print(sess.run(adder_node, feed_dict={a: 3, b: 4.5}))
print(sess.run(adder_node, feed_dict={a: [1,3], b: [2, 4]}))

add_and_triple = adder_node * 3.
print(sess.run(add_and_triple, feed_dict={a: 3, b:4.5}))

"""### **02.** Linear Regression"""

import tensorflow as tf

tf.set_random_seed(777)  # 랜덤난수

# 훈련용 x와 y데이터, 1~3 -> 1~3
x_train = [1, 2, 3]
y_train = [1, 2, 3]

W = tf.Variable(tf.random_normal([1]), name="weight")
b = tf.Variable(tf.random_normal([1]), name="bias")

# 임의의 W,b값을 넣어 가설 만들기 -> 리니어 생성
hypothesis = x_train * 1.0000008 + -1.588774e-06

# 가설 - 실제값을 계산하여 Cost를 계산한다 -> 리니어에서 실제값을 뺀 것 for mean square
# Cost가 낮아야 한다 -> Cost가 낮은 W값을 찾는다
cost = tf.reduce_mean(tf.square(hypothesis - y_train))

# Cost를 미분하여 최적의 Convex=(Cost 최저)를 찾는다 
train = tf.train.GradientDescentOptimizer(learning_rate=0.05).minimize(cost) # learning_rate의 값을 크게 만들면?

print(sess.run(cost))

"""### **03. Linear Regression(placeholder)**"""

import tensorflow as tf
tf.set_random_seed(777)  # for reproducibility

# X and Y data
x_train = [1, 2, 3]
y_train = [1, 2, 3]

# Try to find values for W and b to compute y_data = x_data * W + b
# We know that W should be 1 and b should be 0
# But let TensorFlow figure it out
W = tf.Variable(tf.random_normal([1]), name="weight")
b = tf.Variable(tf.random_normal([1]), name="bias")

# Our hypothesis XW+b
hypothesis = x_train * W + b

# cost/loss function
cost = tf.reduce_mean(tf.square(hypothesis - y_train))

# optimizer
train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)

# Launch the graph in a session.
with tf.Session() as sess:
    # Initializes global variables in the graph.
    sess.run(tf.global_variables_initializer())

    # Fit the line
    for step in range(2001):
        _, cost_val, W_val, b_val = sess.run([train, cost, W, b])

        if step % 20 == 0:
            print(step, cost_val, W_val, b_val)

"""### **04. Cost function / Gradient Decent Algorism**"""

import tensorflow as tf
tf.set_random_seed(777)  


x_train = [1, 2, 3]
y_train = [1, 2, 3]

W = tf.Variable(tf.random_normal([1]), name="weight")
b = tf.Variable(tf.random_normal([1]), name="bias")

hypothesis = x_train * W + b

cost = tf.reduce_mean(tf.square(hypothesis - y_train))

train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)

with tf.Session() as sess:
  
    sess.run(tf.global_variables_initializer())

    
    for step in range(2001):
        _, cost_val, W_val, b_val = sess.run([train, cost, W, b])

        if step % 20 == 0:
            print(step, cost_val, W_val, b_val)

# Lab 3 Minimizing Cost
# This is optional
import tensorflow as tf

# tf Graph Input
X = [1, 2, 3]
Y = [1, 2, 3]

# Set wrong model weights
W = tf.Variable(5.)

# Linear model
hypothesis = X * W

# Manual gradient
gradient = tf.reduce_mean((W * X - Y) * X) * 2

# cost/loss function
cost = tf.reduce_mean(tf.square(hypothesis - Y))

# Minimize: Gradient Descent Optimizer
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)

# Get gradients
gvs = optimizer.compute_gradients(cost)

# Optional: modify gradient if necessary
# gvs = [(tf.clip_by_value(grad, -1., 1.), var) for grad, var in gvs]

# Apply gradients
apply_gradients = optimizer.apply_gradients(gvs)

# Launch the graph in a session.
with tf.Session() as sess:
    # Initializes global variables in the graph.
    sess.run(tf.global_variables_initializer())

    for step in range(101):
      
        gradient_val, gvs_val, _ = sess.run([gradient, gvs, apply_gradients])
        print(step, gradient_val, gvs_val)
