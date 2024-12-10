import cv2
import pyzed.sl as sl

# Initialize the ZED camera
zed = sl.Camera()
init_params = sl.InitParameters()
init_params.camera_resolution = sl.RESOLUTION.HD720  # Set resolution to 720p
init_params.coordinate_units = sl.UNIT.METER         # Use meter units

# Open the ZED camera
if zed.open(init_params) != sl.ERROR_CODE.SUCCESS:
    print("Unable to open ZED camera")
    exit()

runtime_params = sl.RuntimeParameters()
image = sl.Mat()

print("Press 'q' to exit.")

while True:
    # Capture frames from the ZED camera
    if zed.grab(runtime_params) == sl.ERROR_CODE.SUCCESS:
        zed.retrieve_image(image, sl.VIEW.LEFT)  # Get the left image
        frame = image.get_data()  # Convert to numpy array (BGRA format)

        # Display the frame
        cv2.imshow("ZED Camera Feed", frame)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close OpenCV windows
zed.close()
cv2.destroyAllWindows()
