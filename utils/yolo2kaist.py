import os
import cv2

def yolo_to_kaist(yolo_result_file, output_file, image_width, image_height):
    with open(yolo_result_file, 'r') as infile, open(output_file, 'w') as outfile:
        # class_id, confidence, x_center, y_center, width, height
        for line in infile:
            parts = line.strip().split()
            frame_id = int(parts[0])
            class_id = int(parts[1])
            confidence = float(parts[2])
            x_center = float(parts[3])
            y_center = float(parts[4])
            width = float(parts[5])
            height = float(parts[6])

            x_min = (x_center - width / 2) * image_width
            y_min = (y_center - height / 2) * image_height
            x_max = (x_center + width / 2) * image_width
            y_max = (y_center + height / 2) * image_height

            # Assuming frame_number is available
            # frame_number = 0  # replace with actual frame number if needed

            outfile.write(f"{frame_id} {float(x_min)} {float(y_min)} {float(x_max)} {float(y_max)} {confidence:.6f}\n")

# Example usage
image_width = 640  # replace with actual image width
image_height = 512  # replace with actual image height
yolo_result_file = 'output_file.txt'
output_file = 'kaist_results.txt'
yolo_to_kaist(yolo_result_file, output_file, image_width, image_height)
