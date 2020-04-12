import tensorflow as tf

# ten = tf.constant([1, 2, 3, 4, 5, 6, 7])
#
# sess = tf.InteractiveSession()
# a = tf.constant(5.0)
# b = tf.constant(6.0)
# c = a * b
# # We can just use 'c.eval()' without passing 'sess'
#
# print(ten.eval())
# #sess.run()
# sess.close()

# t = tf.constant(42.0)
# sess = tf.Session()
# with sess.as_default():   # or `with sess:` to close on exit
#     assert sess is tf.get_default_session()
#     assert t.eval() == sess.run(t)
#
# t = tf.constant(42.0)
# u = tf.constant(37.0)
# tu = t * u
# ut = t * t
# with sess.as_default():
#    print(tu.eval())  # runs one step
#    print(ut.eval())  # runs one step
#    print(sess.run([tu, ut]))  # evaluates both tensors in a single step


e = tf.placeholder("float", None)
x = tf.placeholder("float", [None, 3])
y = x * 2 + e
w = e + 1

with tf.Session() as session:
    x_data = [[1, 2, 3],
              [4, 5, 6], ]
    result = session.run(y, feed_dict={x: x_data, e: 23})
    print(result)