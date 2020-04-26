import numpy as np
from keras.preprocessing import image
from keras.applications.imagenet_utils import preprocess_input
from keras.models import load_model
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow

from keras.utils.vis_utils import model_to_dot
from keras.utils import plot_model
from IPython.display import SVG



happyModel = load_model('happymodel.h5')

# plot_model(happyModel, to_file='HappyModel.png')
# SVG(model_to_dot(happyModel).create(prog='dot', format='svg'))

### START CODE HERE ###
# img_path = 'images/my_image.jpg'
img_path = 'images/cry.jpg'
### END CODE HERE ###
img = image.load_img(img_path, target_size=(64, 64))
imshow(img)
plt.show()

x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

print(happyModel.predict(x))