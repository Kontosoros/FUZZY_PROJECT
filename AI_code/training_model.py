import pandas as pd
import glob
from PIL import Image
from numpy import asarray
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

def convert_images(path):
    PNEFMONIA_PIXELS = []
    PNEFMONIA_label = []
    NORMAL_PIXELS = []
    NORMAL_label = []
    # We load the folder that contains 1341 NORMAL images
    for image_path in glob.glob(path + "NORMAL/*.jpeg"):
        # Convert Images into specific shape 250 x 250
        image = Image.open(image_path).convert("L").resize((250, 250))
        # Do Normalization for all the values in order to be in the range of (0:1)
        image_to_numpy = asarray(image) / 255
        # IMAGE PIXELS
        NORMAL_PIXELS.append(image_to_numpy.ravel())
        # IMAGE LABEL: Add the label 0 for the images that dont have pnefmonia
        NORMAL_label.append(0)
    # We load the folder that contains 1341 PNEFMONIA images
    for image_path in glob.glob(path + "PNEUMONIA/*.jpeg"):
        # Convert Images into specific shape 250 x 250
        image = Image.open(image_path).convert("L").resize((250, 250))
        # Do Normalization for all the values in order to be in the range of (0:1)
        image_to_numpy = asarray(image) / 255
        if len(NORMAL_PIXELS) < len(PNEFMONIA_PIXELS):
            PNEFMONIA_PIXELS.append(image_to_numpy.ravel())
            # IMAGE LABEL: Add the label 1 for the images that have pnefmonia
            PNEFMONIA_label.append(1)
    """
    Note:
        d = {images:[[NORMAL_PIXELS]........,[PNEFMONIA_PIXELS].......],'labels':[1,1,0,0.....]}
    """
    d = {"images": NORMAL_PIXELS + PNEFMONIA_PIXELS, "labels": NORMAL_label + PNEFMONIA_label}
    # We convert the previous dictionary into pandas data frame
    pandas = pd.DataFrame.from_dict(d, orient="index")
    df = pandas.transpose()
    X = df["images"]
    y = df["labels"]
    return X, y






def train_test_model(X, y):
    # We split our dataset into training and testing dataset
    training_images, test_images, training_labels, test_labels = train_test_split(X, y, test_size=0.2, random_state=42)
    # Labels for training dataset
    taining_labels_neo = [i for i in training_labels]
    # Values for training dataset
    training_images_neo = [img for img in training_images]
    # Values for testing dataset
    test_neo = [img for img in test_images]
    # Labels for testing dataset
    test_labels_neo = [i for i in test_labels]
    # We load our model
    clf = svm.SVC(decision_function_shape="ovo")
    # We train our model
    clf.fit(training_images_neo, taining_labels_neo)
    # We test our model
    Y_preds = clf.predict(test_neo)
    # The accuracy of the model is 0.96 %
    score = accuracy_score(test_labels_neo, Y_preds)
    # SAVE THE MODEL
    # with open('my_dumped_classifier.pkl', 'wb') as fid:
    #    pickle.dump(clf, fid)
load_data_for_training = "C:/My_python_projects/COMPLETED_ML_PROJECTS/PNEFMONIA_AI_DIAGNOSIS/"
X, y = convert_images(load_data_for_training)
train_test_model(X, y)