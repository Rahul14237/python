import tensorflow as tf
hello = tf.constant('Hello TensorFlow world')
sess = tf.Session()
print(sess.run(hello))
print("first project, hello from PYTHON")
# players = [10, 30, 40]
# p = players+[0, 0]
# p = p[1:3] # p[:] will print every element of p
# print(players, p)

# name = 'archi'
# if name is 'rahul':          # every looping statement ends with :
#     print('hello rahul')
# elif name is 'vijay':
#      print('hello vijay')
# else:
#      print('hi')
#      print('please sign up first')

# item = ['banana', 'chiku', 'apple', 'grapes', 'waterMelon' 'one']
# for i in item[1:3]:
#     print(i)
#     print(len(i))
# for j in range(10):
#     print(j)
# for k in range(5, 7):
#     print(k)
# for l in range(50, 500, 100):
#     print(l)


# """i=2;
# while i<5:
#     print(i+1)
#     i+=1
# """

'''for i in range(1, 110):
    if i%10 is 0:
        print(i)
'''

'''def firstFunction(name, ruppes):
    print(name, 'has', ruppes, 'in his pocket')
    func_name = 'secondFunction in first function'
    secondfunc(func_name)

def secondfunc(name):
    print(name)

firstFunction('rahul',100)
#firstFunction('vijay', 100)
#firstFunction('mayur', 100)
'''

'''def eating_Timings(lunch_Timings = 1.5):
    eating_time = lunch_Timings+6
    return  eating_time
eating_time = eating_Timings(2)
print("ross's dinner time is", eating_time)
eating_time = eating_Timings(1)
print("monica's dinner timings is ", eating_time)
eating_time = eating_Timings()
print("chandler's dinner timings is ", eating_time)
'''

'''def functionName(*args):
    total = 0
    for a in args:
        total += a
    print(total)
functionName(2, 3, 4)
functionName(21342, 1342536, 4345678689, 214353678, 342)
'''

'''def unpackinglist(efficiency, inTime, outTime, lunchHours):
    effectiveworkinghour = ((outTime - inTime)-lunchHours)*efficiency
    print(effectiveworkinghour)

list = [.8, 1000, 1800, 50]
unpackinglist(*list)
'''

'''
dictionary = {'key1' : 'value1', 'key2' : 'value2', 'key3' : 'value3', 'key4' : 'value4'}

for k, v in dictionary.items():
    print(k, v)
'''

'''import calculate_sum
calculate_sum.sum()
'''

''' import random
import urllib.request

def download_img(url):
    name = random.randrange(1,100)
    file_name = str(name)+'.jpg'
    urllib.request.urlretrieve(url, file_name)
download_img('https://www.w3schools.com/css/trolltunga.jpg')
'''

# import urllib.request
#
#
# google_url = 'http://chart.finance.yahoo.com/table.csv?s=GOOG&a=1&b=28&c=2017&d=2&e=28&f=2017&g=d&ignore=.csv'
#
#
# def download_file_from_internet(url):
#     response = urllib.request.urlopen(url)
#     csv = response.read()
#     csv_str = str(csv)
#     lines = csv_str.split('\\n')
#     write_dir = 'goog.csv'
#     fx = open(write_dir, 'w')
#     for line in lines:
#         fx.write(line + '\n')
#     fx.close()
#
# download_file_from_internet(google_url)

# while True:
#  try:
#    number = int(input('enter u r fac number\n'))
#    print(1000/number)
#    break
#  except ValueError:
#       print("Enter correct  number")
#  except ZeroDivisionError:
#       print("can't divide by zero")
#  # except:
#  #      print('Make sure for input')
#  finally:
#       print('i am still in the loop')

# class boy:
#     gender = 'male'
#
#
#     def __init__(self, name):
#         self.name = name
#
#
# r = boy('rahul')
# s = boy('vijay')
#
# print(r.gender)
# print(s.gender)
# print(r.name)
# print(s.name)

'''class mario():
    def move(self):
        print('i am moving')

class eat():
    def eating(self):
        print('i am eating')

class big_mario(mario,eat):
    def getting_big(self):
        prin('I am bigger now')

a = big_mario()
a.move()
a.eating()
'''


'''import threading

class rahul(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.current_thread().getName())

x = rahul(name = 'eating puran poli')
y = rahul(name = 'Drinking water')
z = rahul(name =  'eating desert')

x.start()
y.start()
z.start()
'''

'''def list_unpacking_funct(list_):
    first, *middle, last = list_
    avg = sum(middle)/(len(middle))
    print(avg)

list_unpacking_funct([2,3,4,5,6,7,8])
'''

'''s1 = input('what is my age '), s2 = input('what is my name ') = argv ;
print(age*2)'''





