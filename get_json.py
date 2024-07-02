import utils

if __name__ == '__main__':
    utils.merge_txt_files_with_ids('./detect/predict2/labels', './output_file.txt')
    utils.yolo_to_kaist('./output_file.txt', 'kaist_results.txt', 640, 512)
    utils.txt2json('kaist_results.txt', 'kaist_results.json')