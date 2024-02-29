# Eye-Blink Controlled Keyboard

This Python code uses the dlib library and computer vision techniques to create a virtual keyboard controlled by eye blinks. The program captures video from the default camera (`cv2.VideoCapture(0)`) and tracks the user's face and eyes to detect blinks. The keyboard layout is displayed on the screen, and the user can select keys by blinking.

## Dependencies
- OpenCV (`cv2`)
- NumPy (`np`)
- dlib
- Math (`hypot`)

## Installation and Setup
1. Install the required libraries:
    ```bash
    pip install opencv-python numpy dlib
    ```
2. Download the pre-trained facial landmark predictor model file (`shape_predictor_68_face_landmarks.dat`) from [dlib's official website](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2) and place it in the same directory as the script.

## How to Use
1. Run the script:
    ```bash
    python your_script_name.py
    ```
2. A window will open showing your camera feed with a rectangular frame around your face.
3. The virtual keyboard will be displayed on the screen.
4. Blink to select keys. Each blink will select a column first, and subsequent blinks will select a letter in that column.
5. The selected letters will be displayed on a board at the top left corner of the window.
6. Press the 'Esc' key to exit the program.

## Customization
- You can modify the `keyset` dictionary to customize the keys on the virtual keyboard.
- Adjust the layout of the keys in the `letter` function if needed.
- Fine-tune the blink detection thresholds in the `get_eyes_ratios` function.

## Notes
- The script uses a basic layout for demonstration purposes, and you may want to customize it based on your preferences or specific use case.

## Acknowledgments
- The facial landmark predictor model used in this code is provided by the dlib library.

## License
This code is provided under the MIT License. Feel free to use, modify, and distribute it as needed.
