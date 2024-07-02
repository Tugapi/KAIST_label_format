import json

def txt2json(txt_file_path, json_file_path):
    """
    Convert txt file to coco json format
    Arguments:
        `txt`: Path to annotation file
               Each line contains image id, 4 bbox coordinates and confidence score
    """
    predict_result = []
    f = open(txt_file_path, 'r')
    lines = f.readlines()
    for line in lines:
        json_format = {}
        pred_info = [float(ll) for ll in line.split(' ')]
        json_format["image_id"] = int(pred_info[0] - 1)  # image id
        json_format["category_id"] = 1.0  # pedestrian
        json_format["bbox"] = [pred_info[1], pred_info[2], pred_info[3], pred_info[4]]  # bbox
        json_format["score"] = pred_info[5]  # confidence score

        predict_result.append(json_format)
        with open(json_file_path, 'w') as json_data:
            json.dump(predict_result, json_data, indent=4)

if __name__ == '__main__':
    txt2json("../kaist_results.txt", "kaist_results.json")