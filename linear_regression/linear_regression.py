# A linear regression learning algorithm example using TensorFlow library.
from __future__ import print_function

import tensorflow as tf
import numpy
import matplotlib.pyplot as plt
rng = numpy.random

# Parameters
learning_rate = 0.1
training_epochs = 1000
display_step = 100

# y = 4x+delta
train_X = numpy.asarray(range(100,501))
train_Y = numpy.asarray(numpy.multiply(1.2, train_X))

# Training Data
#train_X = numpy.asarray([3.3,4.4,5.5,6.71,6.93,4.168,9.779,6.182,7.59,2.167,
#                         7.042,10.791,5.313,7.997,5.654,9.27,3.1])
#train_Y = numpy.asarray([1.7,2.76,2.09,3.19,1.694,1.573,3.366,2.596,2.53,1.221,
#                         2.827,3.465,1.65,2.904,2.42,2.94,1.3])


#train_X = numpy.asarray([1,2,3,4,5,6,8,9,4,6,9])

#train_Y = numpy.asarray([4,8,12,16,20,24,32,36,16, 24,36])



#train_X = numpy.asarray([5.0,5.1,6.3,6.1,6.0, 5.1, 5.5, 5.4, 5.4,5.3, 4.9, 5.7, 6.0, 6.0, 5.3, 5.5, 5.9, 5.8, 5.1, 5.7])
#train_Y = numpy.asarray([5.4, 5.7, 8.1, 8.9, 7.5, 4.8, 6.0, 6.3, 6.2, 6.1, 5.4, 4.5, 7.0, 8.5, 8.8, 6.1, 5.9, 6.7, 8.3, 9.0])


train_X = train_X/100
train_Y = train_Y/100
n_samples = train_X.shape[0]

# tf Graph Input
X = tf.placeholder("float")
Y = tf.placeholder("float")

# Set model weights
W = tf.Variable(rng.randn(), name="weight")
b = tf.Variable(rng.randn(), name="bias")



# Construct a linear model
pred = tf.add(tf.multiply(X, W), b)

# Mean squared error
cost = tf.reduce_sum(tf.pow(pred-Y, 2))/(2*n_samples)
# Gradient descent
#  Note, minimize() knows to modify W and b because Variable objects are trainable=True by default
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

# Initialize the variables (i.e. assign their default value)
init = tf.global_variables_initializer()

# Start training
with tf.Session() as sess:

    # Run the initializer
    sess.run(init)

    # Fit all training data
    for epoch in range(training_epochs):
        for (x, y) in zip(train_X, train_Y):   # zip- Iterate over two lists in paralle
            sess.run(optimizer, feed_dict={X: x, Y: y})

        # Display logs per epoch step
        if (epoch+1) % display_step == 0:
            c = sess.run(cost, feed_dict={X: train_X, Y:train_Y})
            print("Epoch:", '%04d' % (epoch+1), "cost=", "{:.9f}".format(c), \
                "W=", sess.run(W), "b=", sess.run(b))
        # Graphic display
            plt.plot(train_X, train_Y, 'ro', label='Original data')
            plt.plot(train_X, sess.run(W) * train_X + sess.run(b), label='Fitted line')
            plt.legend()
            plt.show()
    print("Optimization Finished!")
    training_cost = sess.run(cost, feed_dict={X: train_X, Y: train_Y})
    print("Training cost=", training_cost, "W=", sess.run(W), "b=", sess.run(b), '\n')


