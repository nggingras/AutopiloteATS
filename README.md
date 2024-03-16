# AutopiloteATS

## Introduction
This project aims to develop an autopilot system using machine learning techniques. The system will be trained on a dataset to predict the steering angle of a vehicle based on input images. The game American Truck Simulator is used.

At the moment, the best performance is around 29% error rate. More dataset are needed to improve performance, which means more hours to play the game.

The main driving script is not done yet. 

## Setup
To set up the project environment, follow these steps:

1. Install MiniConda by visiting the official website and downloading the appropriate version for your operating system.
2. Open a terminal or command prompt and navigate to the project directory:
3. Create a new virtual environment using the following command:
  ```
  conda create --name venvAutopiloteAts
  ```

  Here is an example
   ```
  (base) PS C:\WINDOWS\system32> cd C:\Users\Nicolas\Documents\GitHub\VirtualEnv-Project
(base) PS C:\Users\Nicolas\Documents\GitHub\VirtualEnv-Project> conda --version
conda 23.11.0
(base) PS C:\Users\Nicolas\Documents\GitHub\VirtualEnv-Project> conda create --name venvAutopiloteAts
Retrieving notices: ...working... done
Channels:
 - defaults
Platform: win-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: C:\Users\Nicolas\miniconda3\envs\venvAutopiloteAts



Proceed ([y]/n)? y

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate venvAutopiloteAts
#
# To deactivate an active environment, use
#
#     $ conda deactivate

(base) PS C:\Users\Nicolas\Documents\GitHub\VirtualEnv-Project> conda activate venvAutopiloteAts
(venvAutopiloteAts) PS C:\Users\Nicolas\Documents\GitHub\VirtualEnv-Project>Python -V
Python 3.11.5
```
4. Activate the virtual environment:
  ```
  conda activate venvAutopiloteAts
  ```
5. Install the required Python packages by running the following command:
  ```
  pip install -r requirements.txt
  ```

## Generate Dataset
To generate the dataset, run the `generateDataset.py` script. This script will collect images and corresponding steering angles (keyboard input) to be used for training the autopilot model. Dataset are saved as numpy array under the project folder.

## Train the model
To train the model, run the "trainDrivingModel.py' script. This script is a Python script that uses the fastai library to train a model for a driving simulator. The model is trained to predict the direction (left, straight, or right) based on the input image.
Note that the script is also available as a Jupyter Notebook. This is because I recommend you run it from a machine learning cloud services as Kaggle or Colab. Training the AI requires important GPU performances. 
My current datasets are available in Google drive here: https://drive.google.com/drive/folders/1FGG7YJaUYI8urVIIFzu1SiAEEbr3P-5Z. Download everything and drop them under a data folder 
  ```
  .\data\%dataset%
  ```

## Reference
This model is higly based on FastiAi lesssons and https://medium.datadriveninvestor.com/how-i-developed-an-in-game-self-driving-vehicle-using-fast-ai-and-american-truck-simulator-2524891dbaf
