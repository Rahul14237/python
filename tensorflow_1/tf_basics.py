import tensorflow as tf

# declare parameters which are changed to make loss minimum at same time initialize variables
w = tf.Variable([0.3], tf.float32)
b = tf.Variable([0.5], tf.float32)
init = tf.global_variables_initializer()

# declare placeholders
x = tf.placeholder(tf.float32)
y= tf.placeholder(tf.float32)

# define computation graph
y_ = w*x+b
loss = tf.reduce_sum(tf.square(y_- y))
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

# start session and initialize variables
sess =tf.Session()
sess.run(init)

# training data
x_train = [1, 2, 3, 4]
y_train = [0, -1, -2, -3]

for i in range(10000):
    sess.run(train, {x: x_train, y: y_train})

# loss with updated parameters
curr_W, curr_b, curr_loss = sess.run([w, b, loss], {x: x_train, y: y_train})
print("W: %s b: %s loss: %s"%(curr_W, curr_b, curr_loss))
sess.close()
