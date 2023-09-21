import cv2
import os

def capture_images(student_rollno, num_images=20):
    # Create a directory for the student if it doesn't exist
    student_dir = f'student_images/{student_rollno}'
    os.makedirs(student_dir, exist_ok=True)

    vid = cv2.VideoCapture(0)

    for i in range(num_images):
        print(f'Capturing image {i + 1}/{num_images}')
        success, frame = vid.read()
        if success:
            img_path = f'{student_dir}/{student_rollno}_{i + 1}.jpg'
            cv2.imwrite(img_path, frame)
            print(f'Image saved as {img_path}')
        else:
            print('Error capturing image')

    vid.release()

student_rollno = input('Enter student roll number: ')
capture_images(student_rollno)
