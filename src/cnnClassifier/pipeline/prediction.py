# import numpy as np
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image
# import os



# class PredictionPipeline:
#     def __init__(self,filename):
#         self.filename =filename


    
#     def predict(self):
#         ## load model
        
#         # model = load_model(os.path.join("artifacts","training", "model.h5"))
#         model = load_model(os.path.join("model", "model.h5"))

#         imagename = self.filename
#         test_image = image.load_img(imagename, target_size = (224,224))
#         test_image = image.img_to_array(test_image)
#         test_image = np.expand_dims(test_image, axis = 0)
#         result = np.argmax(model.predict(test_image), axis=1)
#         print(result)

#         if result[0] == 1:
#             prediction = 'Normal'
#             return [{ "image" : prediction}]
#         else:
#             prediction = 'Adenocarcinoma Cancer'
#             return [{ "image" : prediction}]


# import numpy as np
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image
# import os

# class PredictionPipeline:
#     def __init__(self,filename):
#         self.filename = filename

#     def predict(self):
#         ## load model
#         model = load_model(os.path.join("model", "model.h5"))

#         imagename = self.filename
#         test_image = image.load_img(imagename, target_size = (224,224))
#         test_image = image.img_to_array(test_image)
#         test_image = np.expand_dims(test_image, axis = 0)
#         result = np.argmax(model.predict(test_image), axis=1)

#         if result[0] == 0:  # Modified condition
#             prediction = 'Adenocarcinoma Cancer'
#             return [{"image": prediction}]
#         else:
#             prediction = 'Normal'
#             return [{"image": prediction}]

import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        # Load model
        model = load_model(os.path.join("model", "model.h5"))

        # Load and preprocess the image
        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)

        # Predict the probabilities for each class
        probabilities = model.predict(test_image)[0]

        # Get the index of the class with the highest probability
        predicted_class_index = np.argmax(probabilities)

        # Define class labels
        class_labels = ['Adenocarcinoma Cancer', 'Normal']

        # Get the predicted class label
        predicted_class_label = class_labels[predicted_class_index]

        return [{"image": predicted_class_label}]
