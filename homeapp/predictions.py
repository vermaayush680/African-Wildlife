import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import numpy as np
from tensorflow import keras
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from tensorflow.keras.preprocessing import image
import paths
def check(img):
    try:
        os.chdir('homeapp')
    except:
        pass
    lr = keras.models.load_model('weights.h5')

    print('loaded')
    class Preprocessor(BaseEstimator, TransformerMixin):
        def fit(self,img_object):
            return self
        
        def transform(self,img_object):
            img_array = image.img_to_array(img_object)
            expanded = (np.expand_dims(img_array,axis=0))
            return expanded

    class Predictor(BaseEstimator, TransformerMixin):
        def fit(self,img_array):
            return self
        
        def predict(self,img_array):
            probabilities = lr.predict(img_array)
            predicted_class = ['Buffalo', 'Elephant', 'Rhino', 'Zebra'][probabilities.argmax()]
            return predicted_class

    full_pipeline = Pipeline([('preprocessor',Preprocessor()),
                            ('predictor',Predictor())])

    os.chdir(paths.ROOT_DIR)
    os.chdir('media')
    print(os.getcwd())
    a= image.load_img(img)
    a=a.resize((256,256))
    predic = full_pipeline.predict(a)
    return(predic)