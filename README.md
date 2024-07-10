![WhatsApp Image 2024-07-10 at 11 17 46 PM](https://github.com/Neelakandan-1306/OpenCv_Arduino1/assets/100917250/4fdf2193-cae1-414d-8f76-cba346a328cf)


This project uses OpenCV and a hand tracking module to control LEDs based on the number of fingers raised. 
The camera captures the hand gestures, and based on the number of fingers detected, different LEDs are turned on or off.

This project demonstrates how to use computer vision to control hardware components like LEDs.
The hand tracking is achieved using OpenCV and a custom HandTrackingModule. The number of fingers raised is detected, and corresponding LEDs are controlled via a controller module.

- Python 
- OpenCV
- HandTrackingModule (custom module)
- Arduino
- A camera (built-in or external)
- LEDs connected to your system (via GPIO or similar interface)


1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/led-control-opencv.git
    ```
2. Navigate to the project directory:
    ```bash
    cd led-control-opencv
    ```
3. Install the required Python packages:
    ```bash
    pip install opencv-python
    ```
