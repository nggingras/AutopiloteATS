"""
generateDataset.py

This script records frames from the screen and saves them along with corresponding output to generate a training dataset.
It uses the mss library to capture frames, OpenCV to process the frames, and the pynput library to capture user input.
The captured frames and outputs are saved to separate numpy files for training a machine learning model.

Author: Nicolas
Date: 16 March 2024
"""

import time
import numpy as np
from numpy import ones, vstack
from numpy.linalg import lstsq
from statistics import mean
from mss import mss
import cv2
from pynput import keyboard
import time
import numpy as np
from numpy import ones, vstack
from numpy.linalg import lstsq
from statistics import mean
from mss import mss
import cv2
from pynput import keyboard

keys = [] 

def key_check():
    """
    Listens for keyboard events and calls the corresponding functions.

    This function uses the `keyboard.Listener` class from the `keyboard` module to listen for keyboard events.
    It takes two arguments, `on_press` and `on_release`, which are the callback functions to be called when a key is pressed or released, respectively.
    The function will continue listening for keyboard events until the listener.stop method is called.

    Note: Make sure to import the `keyboard` module and define the `on_press` and `on_release` functions before calling `key_check()`.

    Example usage:
    ```
    def on_press(key):
        # Handle key press event

    def on_release(key):
        # Handle key release event

    key_check()
    ```

    """
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

def on_press(key):
    """
    Function to handle key press events.

    This function is called when a key is pressed. It checks if the key is alphanumeric or a special key.
    If the key is alphanumeric, it prints the key character and appends the key to a list called 'keys'.
    If the key is a special key, it prints the key itself.

    Parameters:
    - key: The key object representing the pressed key.

    Returns:
    - False: Indicates that the key press event has been handled.
    """
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
        keys.append(str(key))
        return False
    except AttributeError:
        print('special key {0} pressed'.format(
            key))
        return False

def on_release(key):
    """
    Callback function that is called when a key is released.

    This function prints the key that was released and checks if it is the 'esc' key.
    If the released key is the 'esc' key, the listener should stop.

    Parameters:
    - key: The key that was released.

    Returns:
    - False: If the released key is the 'esc' key, indicating that the listener should stop.
    """
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def keys_to_output(keys):
    """
    Convert a list of keys into a corresponding output list.

    Args:
        keys (list): A list of keys.

    Returns:
        list: A list representing the output based on the given keys.
            The output list has three elements, where the first element
            represents the 'a' key, the second element represents the 'w' key,
            and the third element represents the 'd' key. If none of these
            keys are present in the input list, all elements in the output
            list will be 0.

    """
    if "'a'" in keys:
        return [1, 0, 0]
    elif "'d'" in keys:
        return [0, 0, 1]
    elif "'w'" in keys:
        return [0, 1, 0]
    else:
        return [0, 0, 0]

def save_training_data(file_name, data):
    """
    Save the training data to a file.
    """
    with open(file_name, 'w') as file:
        for entry in data:
            line = f"{entry[0].tolist()} {entry[1]}\n"
            file.write(line)

# Record frames from the screen
def record_frames(file_name):
    """
    Records frames from the screen and saves them along with corresponding output.
    """
    # 4 seconds delay to open the game.
    for i in list(range(4))[::-1]:
        print(i + 1)
        time.sleep(1)

    with mss() as sct:
        training_data = []
        
        # Part of the screen to capture
        monitor = {"top": 79, "left": 0, "width": 2000, "height": 800}

        while "Screen capturing":
            # Record the current time
            last_time = time.time()

            # Capture the screen using the screen capture tool (sct) and convert it to a numpy array
            # The size of the array depends on the size of the screen capture
            screen = np.array(sct.grab(monitor))
            # Print the frames per second (fps), which is the reciprocal of the time taken to capture one frame
            print("fps: {}".format(1 / (time.time() - last_time)))

            # Record the current time again for calculating fps for the next operations
            last_time = time.time()
            # Convert the color of the screen capture from BGR to RGB because OpenCV uses BGR by default and the screen capture tool uses RGB
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
            # Resize the screen capture to 1000x1000 pixels because the original size is too large
            screen = cv2.resize(screen, (1000, 1000))
            
            # optional for debugging purposes
            # Display the resized screen capture in a window named 'window2'
            # cv2.imshow('window2', cv2.cvtColor(cv2.resize(screen, (800,600)), cv2.COLOR_BGR2RGB))
            
            # Check for key presses
            key_check()
            # Convert the last key pressed to output using the keys_to_output function
            output = keys_to_output([keys[-1]])

            # Append the screen capture and the output to the training data
            training_data.append([screen, output])

            # If 'q' is pressed, close all windows and break the loop
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
            # If the length of the training data is a multiple of 10, print the length and save the screens and outputs
            if len(training_data) % 10 == 0:
                print(len(training_data))
                # Separate the screens and outputs from the training data
                screens, outputs = zip(*training_data)
                # Save the screens to a numpy file
                np.save(file_name + '_screens', screens)
                # Save the outputs to a numpy file
                np.save(file_name + '_outputs', outputs)

if __name__ == "__main__":
    # keys has to be initialized
    keys = ["'w'"]
    file_name = "train_data"
    
    # main loop
    record_frames(file_name)
