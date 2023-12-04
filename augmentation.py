import cv2
import pybboxes as pbx
import os
import albumentations as A

def apply_aug(image, bboxes, out_lab_pth, out_img_pth, transformed_file_name, classes):
    transform = A.Compose([
        A.Resize(640, 640),
        A.RandomCrop(width=300, height=300),
        A.HorizontalFlip(p=0.51),
        A.VerticalFlip(p=0.51),
        A.ShiftScaleRotate(p=0.51),
        A.Transpose(p=0.51),
        A.RandomBrightnessContrast(brightness_limit=(-0.2, 0.2), contrast_limit=(-0.2, 0.2), p=0.51),
        A.CLAHE(clip_limit=(0, 1), tile_grid_size=(8, 8), always_apply=True),
#         A.Resize(640, 640)
    ], bbox_params=A.BboxParams(format='yolo', min_visibility=0.2))
    transformed = transform(image=image, bboxes=bboxes)
    transformed_image = transformed['image']
    transformed_bboxes = transformed['bboxes']
    if transformed_bboxes:
        tot_objs = len(bboxes)
        if tot_objs != 0:
            if tot_objs > 1:
                transformed_bboxes = multi_obj_bb_yolo_conversion(transformed_bboxes, classes)
                if transformed_bboxes:
                    save_aug_lab(transformed_bboxes, out_lab_pth, transformed_file_name + ".txt")
            else:
                transformed_bboxes = [single_obj_bb_yolo_conversion(transformed_bboxes[0], classes)]
                if transformed_bboxes:
                    save_aug_lab(transformed_bboxes, out_lab_pth, transformed_file_name + ".txt")
            save_aug_image(transformed_image, out_img_pth, transformed_file_name + ".png")
            draw_yolo(transformed_image, transformed_bboxes)
        else:
            print("label file is empty")
    else:
        print("No bounding boxes after augmentation")
        
        
        
        
        
# bounding box 증강
def get_album_bb_list(yolo_bbox, class_names):
    album_bb =[]
    str_bbox_list = yolo_bbox.split(' ')
    for index, value in enumerate(str_bbox_list):
        if index == 0:  # class number is placed at index 0
            class_name = class_names[int(value)]
        else:
            album_bb.append(float(value))
    album_bb.append(class_name)  # [x_center, y_center, width, height, class_name]
    return album_bb


def get_album_bb_lists(yolo_str_labels, classes):
    album_bb_lists = []
    yolo_list_labels = yolo_str_labels.split('\n')
    for yolo_str_label in yolo_list_labels:
        if len(yolo_str_label) > 0:
            album_bb_list = get_album_bb_list(yolo_str_label, classes)
            album_bb_lists.append(album_bb_list)
    return album_bb_lists


def get_bboxes_list(inp_lab_pth, classes):
    yolo_str_labels = open(inp_lab_pth, "r").read()
    if yolo_str_labels:
        if "\n" in yolo_str_labels:
#             print("multi-objs")
            album_bb_lists = get_album_bb_lists(yolo_str_labels, classes)
        else:
#             print("single line ")
            album_bb_lists = get_album_bb_list(yolo_str_labels, classes)
            album_bb_lists = [album_bb_lists]  # require 2d list in alumbentation function
    else:
        print("No object")
        album_bb_lists = []
    return album_bb_lists



def single_obj_bb_yolo_conversion(transformed_bboxes, class_names):
    if len(transformed_bboxes):
        class_num = class_names.index(transformed_bboxes[-1])
        bboxes = list(transformed_bboxes)[:-1] # .insert(0, '0')
        bboxes.insert(0, class_num)
    else:
        bboxes = []
    return bboxes


def multi_obj_bb_yolo_conversion(aug_labs, class_names):
    yolo_labels = []
    for aug_lab in aug_labs:
        bbox = single_obj_bb_yolo_conversion(aug_lab, class_names)
        yolo_labels.append(bbox)
    return yolo_labels



def save_aug_lab(transformed_bboxes, lab_pth, lab_name):
    lab_out_pth = os.path.join(lab_pth, lab_name)
    with open(lab_out_pth, 'w') as output:
        for bbox in transformed_bboxes:
            updated_bbox = str(bbox).replace(',', '').replace('[', '').replace(']', '').replace("''",'')
            output.write(updated_bbox + '\n')


def save_aug_image(transformed_image, out_img_pth, img_name):
    out_img_path = os.path.join(out_img_pth,img_name)
    cv2.imwrite(out_img_path, transformed_image)
    

    
    
def draw_yolo(image, labels):
    H, W = image.shape[:2]
    for label in labels:
        yolo_normalized = label[1:]
        box_voc = pbx.convert_bbox(tuple(yolo_normalized), from_type="yolo", to_type="voc", image_size=(W,H))
        cv2.rectangle(image, (box_voc[0], box_voc[1]),
                    (box_voc[2], box_voc[3]), (0, 0, 255), 1)
#     cv2.imwrite("output_vis.png", image)
#     cv2.imshow("output_vis", image)
#     cv2.waitKey(0)