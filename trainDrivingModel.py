import numpy as np
from matplotlib import pyplot
import cv2
from fastai.vision.all import *
from fastai.vision.data import ImageBlock, CategoryBlock
from fastai.data.transforms import RandomSplitter
from fastai.vision.augment import Resize
from fastai.vision.all import get_image_files, DataBlock

# trainDrivingModel.py

"""
The script uses the fastai library to create a DataBlock, load the training data, and train a model using transfer learning.
It is recommended to run this code on a high-performing machine, such as Colab or Kaggle, to improve performance.

Author: Nicolas
Date: [current date]

"""

PATH = "data/"

def save_images(train_data_screens, train_data_outputs, param):
    """
    Save the training data screens as images with corresponding labels folder.

    Args:
        train_data_screens (list): List of training data screens.
        train_data_outputs (list): List of training data outputs.
        param (str): Parameter to modify the .jpg name.

    Returns:
        None
    """
    directions = ['left', 'straight', 'right']
    for i in range(len(train_data_screens)):
        cv2.imwrite(f'data/{directions[np.argmax(train_data_outputs[i])]}/trucksim{param}_{i}.jpg', train_data_screens[i])

if __name__ == "__main__":
    """
    Main script to train the driving model.
    """
    
    # The load and save operation below should be done for as much dataset as there is. The more dataset the better the model will be.
    # save_images third parameter has to be modified to represent the dataset number. It allows to save the images under a different name.
    # Load the training data screens and outputs
    train_data_screens = np.load('train_data_screens_1.npy', allow_pickle=True)
    train_data_outputs = np.load('train_data_outputs_1.npy', allow_pickle=True)

    # Save the training data screens as images with corresponding labels folder
    save_images(train_data_screens, train_data_outputs, 1)
    
    # Load the training data screens and outputs
    train_data_screens = np.load('train_data_screens_2.npy', allow_pickle=True)
    train_data_outputs = np.load('train_data_outputs_2.npy', allow_pickle=True)

    # Save the training data screens as images with corresponding labels folder
    save_images(train_data_screens, train_data_outputs, 2)

    # Define the directions DataBlock
    directions = DataBlock(
        blocks=(ImageBlock, CategoryBlock),
        get_items= get_image_files,
        splitter=RandomSplitter(valid_pct=0.2, seed=42),
        get_y=parent_label,
        item_tfms=Resize(128)
    )

    # Modify the directions DataBlock with additional transformations
    directions = directions.new(
        item_tfms=RandomResizedCrop(224, min_scale=0.5),
        batch_tfms=aug_transforms()
    )
    
    # Create the dataloaders
    dls = directions.dataloaders(PATH)
    
    # Create the vision learner
    learn = vision_learner(dls, resnet18, metrics=error_rate)
    
    # Fine-tune the model
    learn.fine_tune(8)