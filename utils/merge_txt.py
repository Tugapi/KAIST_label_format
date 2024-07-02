import os

def merge_txt_files_with_ids(input_folder, output_file):
    # 获取所有txt文件名，并按名称排序
    txt_files = sorted([f for f in os.listdir(input_folder) if f.endswith('.txt')])
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for file_id, filename in enumerate(txt_files, start=0):
            file_path = os.path.join(input_folder, filename)
            with open(file_path, 'r', encoding='utf-8') as infile:
                for line in infile:
                    outfile.write(f'{file_id} {line}')
                # outfile.write('\n')  # 添加换行符以分隔文件内容

# 示例使用
input_folder = './detect/predict2/labels'  # 替换为你的文件夹路径
output_file = './output_file.txt'  # 替换为你想输出的文件路径
merge_txt_files_with_ids(input_folder, output_file)




'''
def merge_txt_files_sorted(input_folder, output_file):
    # 获取所有txt文件名，并按名称排序
    txt_files = sorted([f for f in os.listdir(input_folder) if f.endswith('.txt')])
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for filename in txt_files:
            file_path = os.path.join(input_folder, filename)
            with open(file_path, 'r', encoding='utf-8') as infile:
                outfile.write(f'Contents of {filename}:\n')
                outfile.write(infile.read())
                outfile.write('\n\n')  # 添加换行符以分隔文件内容

# 示例使用
input_folder = 'path/to/your/txt_files_folder'  # 替换为你的文件夹路径
output_file = 'path/to/your/output_file.txt'  # 替换为你想输出的文件路径
merge_txt_files_sorted(input_folder, output_file)


import os
import cv2

def yolo_to_kaist(yolo_result_file, output_file, image_width, image_height):
    with open(yolo_result_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            parts = line.strip().split()
            class_id = int(parts[0])
            confidence = float(parts[1])
            x_center = float(parts[2])
            y_center = float(parts[3])
            width = float(parts[4])
            height = float(parts[5])

            x_min = (x_center - width / 2) * image_width
            y_min = (y_center - height / 2) * image_height
            x_max = (x_center + width / 2) * image_width
            y_max = (y_center + height / 2) * image_height

            # Assuming frame_number is available
            frame_number = 0  # replace with actual frame number if needed

            outfile.write(f"{frame_number} {int(x_min)} {int(y_min)} {int(x_max)} {int(y_max)} {confidence:.6f}\n")

# Example usage
image_width = 640  # replace with actual image width
image_height = 480  # replace with actual image height
yolo_result_file = 'yolo_results.txt'
output_file = 'kaist_results.txt'
yolo_to_kaist(yolo_result_file, output_file, image_width, image_height)





'''