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

if __name__ == '__main__':
    input_folder = './detect/predict2/labels'  # 替换为你的文件夹路径
    output_file = './output_file.txt'  # 替换为你想输出的文件路径
    merge_txt_files_with_ids(input_folder, output_file)