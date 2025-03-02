import cv2
import numpy as np
from PIL import ImageGrab
from screeninfo import get_monitors

def screen_recorder(output_filename="output.mp4", fps=6.0, record_seconds=50):
    try:
        # Get the dimensions of the entire screen
        monitor = get_monitors()[0]  # Assuming you want to record the primary monitor
        left = monitor.x
        top = monitor.y
        width = monitor.width
        height = monitor.height
        right = left + width
        bottom = top + height

        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_filename, fourcc, fps, (width, height))

        # Calculate the number of frames to record based on fps and duration
        num_frames = int(fps * record_seconds)

        # Create a window for display
        cv2.namedWindow('Screen Recorder', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Screen Recorder', 640, 480)  # Resize window to 640x480 for viewing

        for _ in range(num_frames):
            # Capture screen
            img = ImageGrab.grab(bbox=(left, top, right, bottom))
            img_np = np.array(img)
            frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

            # Write the frame
            out.write(frame)

            # Display the frame in the same window
            cv2.imshow('Screen Recorder', frame)
            if cv2.waitKey(1) == 27:  # Exit on ESC
                break

        # Release everything when job is finished
        out.release()
        cv2.destroyAllWindows()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    screen_recorder()