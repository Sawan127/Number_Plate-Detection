# Number_Plate-Detection
This project demonstrates how to detect vehicle number plates from a video using OpenCV and Haar Cascade classifiers. The detected number plates can be saved as images by pressing a specific key during execution.

## Features

- Detects number plates in a video file using Haar Cascade classifiers.
- Displays a bounding box around the detected number plates in real time.
- Allows saving screenshots of detected number plates with unique filenames.
- Supports real-time visualization of detected number plates (region of interest).

## Prerequisites

- Python 3.6 or later
- OpenCV library (`cv2`)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/number-plate-detection.git
   cd number-plate-detection
2. Install Required Libraries: Install the required libraries using pip:

```bash
pip install opencv-python
```
3. Set Up the Video File: Place your input video file in the specified directory (E:\Opencv\Project 1\Videos) or update the file path in the script to match your file's location.

4. Haar Cascade File: Ensure that the Haar Cascade file haarcascade_russian_plate_number.xml is available in the default OpenCV directory or provide the correct path.

## Usage
1. Run the Script: Execute the Python script to start detecting number plates:

```bash
python detect_number_plate.py
```
2. Keyboard Controls
- 1: Save the detected number plate region as an image in the Resources\Numberplate directory.
- q: Quit the application.

3. Output:

- The video will display bounding boxes around detected number plates.
- Detected number plates will be saved in the specified directory with filenames in the format NoPlate_<count>.jpg.



## Code Explanation
1. Video Capture: The video is read frame by frame using cv2.VideoCapture.

2. Preprocessing: Each frame is resized to 640x480 for consistent processing and converted to grayscale.

3. Number Plate Detection: The Haar Cascade classifier detects number plates using detectMultiScale.

4. Region of Interest (ROI): A bounding box highlights the detected number plate, and the region is extracted for saving.

5. Saving Detected Plates: Pressing 1 saves the number plate as an image with a unique name.

## Notes
- Ensure the Haar Cascade file is correctly loaded; otherwise, detection will fail.
- Update the file paths as needed to match your directory structure.
- This script supports .mp4 video files. For other formats, ensure compatibility with OpenCV.
