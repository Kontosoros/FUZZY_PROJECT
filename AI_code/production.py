import pickle
from PIL import Image
import pandas as pd
from numpy import asarray
import glob

# Load the model
with open("my_dumped_classifier.pkl", "rb") as file:
    ai_model = pickle.load(file)


def use_the_model(img):
    collect_imgs = []
    # Convert Images into specific shape 250 x 250
    image = Image.open(img).convert("L").resize((250, 250))
    # Do Normalization for all the values in order to be in the range of (0:1)
    image_to_numpy = asarray(image) / 255
    collect_imgs.append(image_to_numpy.ravel())
    d = {"images": collect_imgs}
    # We convert the previous dictionary into pandas data frame
    pandas_data_frame = pd.DataFrame.from_dict(d, orient="index")
    data = pandas_data_frame.transpose()
    Xtest = data["images"]
    Xtest_array = [img for img in Xtest]
    # Our model makes  a prediction
    Ypredict = ai_model.predict(Xtest_array)
    return "Negative" if Ypredict[0] == 0 else "Positive"





    