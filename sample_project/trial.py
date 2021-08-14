import tensorflow as tf
import os
from random import shuffle
#from tqdm import tqdm
import matplotlib.pyplot as plt
#import tflearn


a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)

addition = tf.add(a,b)
num1 = 3
num2 = 8

with tf.Session() as sess:
    output= sess.run(addition, feed_dict={a: num1, b: num2})
    print('the sum of {} and {} is {}'.format(num1, num2, output))


