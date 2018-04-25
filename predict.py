import numpy as np
import os
from scipy import  misc
from keras.models import model_from_json
import pickle



classifier_f = open("int_to_word_out.pickle", "rb")
int_to_word_out = pickle.load(classifier_f)
classifier_f.close()



# load json and create model
json_file = open('model_face.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model_face.h5")
print("Model is now loaded in the disk")
num_to_dict = {'1':'Plane', '2':'Bird', '3':'car', '4':'cat', '5':'deer', '6':'dog', '7':'horse', '8':'monkey', '9':'ship', '10':'Truck'}
print (os.listdir("predict"))
for img in os.listdir('predict'):
    # img=os.listdir("predict")[1]
    image=np.array(misc.imread("predict/"+img))
    image = misc.imresize(image, (64, 64))
    image = image[:,:,0:3]
    image=np.array([image])
    image = image.astype('float32')
    image = image / 255.0

    prediction=loaded_model.predict(image)

    # print('Prediction probabilities:', prediction)

    # print(np.max(prediction))

    print(img, ':', num_to_dict[int_to_word_out[np.argmax(prediction)]])
