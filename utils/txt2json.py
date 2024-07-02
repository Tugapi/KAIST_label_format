def txt2json(txt):
    """
    Convert txt file to coco json format
    Arguments:
        `txt`: Path to annotation file
               Each line contains image id, 4 bbox coordinates and confidence score
    """
    predict_result = []
    f = open(txt, 'r')
    lines = f.readlines()
    for line in lines:
        json_format = {}
        pred_info = [float(ll) for ll in line.split(',')]
        json_format["image_id"] = pred_info[0] - 1  # image id
        json_format["category_id"] = 1  # pedestrian
        json_format["bbox"] = [pred_info[1], pred_info[2], pred_info[3], pred_info[4]]  # bbox
        json_format["score"] = pred_info[5]  # confidence score

        predict_result.append(json_format)
    return predict_result
