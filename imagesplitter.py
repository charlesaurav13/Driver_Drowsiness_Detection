import os
import shutil
import random

innerfold = ['Closed_eyes','Open_eyes']
dataset_folder = ['Train_dataset','Test_dataset']
for newfolder in dataset_folder:
    os.mkdir(newfolder)
    os.chdir(os.path.join(os.getcwd(),newfolder))
    for f in innerfold:
        os.mkdir(f)
    os.chdir('..')
for fold in innerfold:
    folder_path = os.path.join(os.getcwd(),fold)
    train_path = os.path.join(os.getcwd(),'Train_dataset',fold)
    test_path = os.path.join(os.getcwd(),'Test_dataset',fold)
    split_ratio = 0.76
    image_list = os.listdir(folder_path)
    random.shuffle(image_list)
    split_index = int(len(image_list) * split_ratio)
    train_list = image_list[:split_index]
    test_list = image_list[split_index:]
    for image_name in train_list:
        image_path = os.path.join(folder_path, image_name)
        destination_path = os.path.join(train_path, image_name)
        shutil.copyfile(image_path, destination_path)
    for image_name in test_list:
        image_path = os.path.join(folder_path, image_name)
        destination_path = os.path.join(test_path, image_name)
        shutil.copyfile(image_path, destination_path)

