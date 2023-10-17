import os
import tensorflow as tf
from tensorflow import keras
from keras import layers
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, GlobalAveragePooling2D
from keras.layers import Conv2D, MaxPooling2D
from keras.utils import load_img
from keras.utils import img_to_array
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
import pathlib
import shutil

import matplotlib.pyplot as plt

count_replicas = 15
diretorio = 'dataset/valid'

count = 0
for root_dir, cur_dir, files in os.walk(diretorio):
    count += len(files)

if count > 150:
  print('Dataset de validação já expandido')
else:
  for subdir in ['M', 'G', 'GG', 'JB']:
    subdir_path = os.path.join(diretorio, subdir)

    # List all image files in the current subdirectory
    image_paths = [os.path.join(subdir_path, filename) for filename in os.listdir(subdir_path) if filename.endswith((".jpg", ".jpeg", ".png"))]
    for image_path in image_paths:
        try:
            print('Processing: ', image_path)
            image = load_img(image_path)
            image = img_to_array(image)
            image = np.expand_dims(image, axis=0)
            # criar um gerador (generator) com as imagens do data augmentation
            imgAug = ImageDataGenerator(rotation_range=45, width_shift_range=0.2,
                                        height_shift_range=0.1, zoom_range=0.25,
                                        brightness_range=(0.1, 0.5), shear_range=0.25,
                                        fill_mode='nearest', horizontal_flip=True)

            imgGen = imgAug.flow(image, save_to_dir=subdir_path,
                                save_format='jpg', save_prefix='i_')

            # gerar 20 imagens por data augmentation
            counter = 0

            for (i, newImage) in enumerate(imgGen):
                #print('Generating the image number: ', counter, '/',25)
                counter += 1
                # ao gerar 20 imagens, parar o loop
                if counter == count_replicas:
                    break
        except Exception as e:
            print(f"Error loading image {image_path}: {e}")



diretorio = 'dataset/train'
count = 0
for root_dir, cur_dir, files in os.walk(diretorio):
    count += len(files)

if count > 100:
  print('Dataset de treinamento já expandido')
else:
  for subdir in ['M', 'G', 'GG', 'JB']:
    subdir_path = os.path.join(diretorio, subdir)

    # List all image files in the current subdirectory
    image_paths = [os.path.join(subdir_path, filename) for filename in os.listdir(subdir_path) if filename.endswith((".jpg", ".jpeg", ".png"))]
    for image_path in image_paths:
        try:
            print('Processing: ', image_path)
            image = load_img(image_path)
            image = img_to_array(image)
            image = np.expand_dims(image, axis=0)
            # criar um gerador (generator) com as imagens do data augmentation
            imgAug = ImageDataGenerator(rotation_range=45, width_shift_range=0.2,
                                        height_shift_range=0.1, zoom_range=0.25,
                                        brightness_range=(0.1, 0.5), shear_range=0.25,
                                        fill_mode='nearest', horizontal_flip=True)

            imgGen = imgAug.flow(image, save_to_dir=subdir_path,
                                save_format='jpg', save_prefix='i_')

            # gerar 5 imagens por data augmentation
            counter = 0

            for (i, newImage) in enumerate(imgGen):
                #print('Generating the image number: ', counter, '/',25)
                counter += 1
                # ao gerar 5 imagens, parar o loop
                if counter == count_replicas:
                    break
        except Exception as e:
            print(f"Error loading image {image_path}: {e}")


diretorio = 'dataset/test'
count = 0
for root_dir, cur_dir, files in os.walk(diretorio):
    count += len(files)

if count > 200:
  print('Dataset de testes já expandido')
else:
  for subdir in ['M', 'G', 'GG', 'JB']:
    subdir_path = os.path.join(diretorio, subdir)

    # List all image files in the current subdirectory
    image_paths = [os.path.join(subdir_path, filename) for filename in os.listdir(subdir_path) if filename.endswith((".jpg", ".jpeg", ".png"))]
    for image_path in image_paths:
        try:
            print('Processing: ', image_path)
            image = load_img(image_path)
            image = img_to_array(image)
            image = np.expand_dims(image, axis=0)
            # criar um gerador (generator) com as imagens do data augmentation
            imgAug = ImageDataGenerator(rotation_range=45, width_shift_range=0.2,
                                        height_shift_range=0.1, zoom_range=0.25,
                                        brightness_range=(0.1, 0.5), shear_range=0.25,
                                        fill_mode='nearest', horizontal_flip=True)

            imgGen = imgAug.flow(image, save_to_dir=subdir_path,
                                save_format='jpg', save_prefix='i_')

            # gerar 5 imagens por data augmentation
            counter = 0

            for (i, newImage) in enumerate(imgGen):
                #print('Generating the image number: ', counter, '/',25)
                counter += 1
                # ao gerar 5 imagens, parar o loop
                if counter == count_replicas:
                    break
        except Exception as e:
            print(f"Error loading image {image_path}: {e}")            