"""
This script automates the process of generating depth maps for a dataset using the StereoNet model. It iterates over a specified range of image numbers, and for each number, it constructs and executes a command to generate a depth map using a pair of left and right images.

The script performs the following steps:
1. Iterates over a hardcoded range of image numbers (e.g., 156 for the 'cutting_tissues_twice' dataset and 63 for the 'pulling_soft_tissues' dataset).
2. For each image number, it generates the file paths for the left and right input images and the output depth map.
3. Constructs a command to run the 'predict.py' script with the necessary arguments, including the model, checkpoint file, input image paths, and output image path.
4. Executes the command using the subprocess module.

Attributes:
    images_left_dir (str): The directory path where the left input images are stored.
    images_right_dir (str): The directory path where the right input images are stored.
    output_dir (str): The directory path where the generated depth maps will be saved.

Usage:
    The script is executed directly, and processes the images based on the hardcoded range of image numbers. Adjust the range of image numbers based on the dataset being used.

Note:
    The range of image numbers is hardcoded in the script and needs to be adjusted based on the dataset being used. The checkpoint file path and model name are also hardcoded and might need adjustments based on the setup.
"""

import os
import subprocess

# Set the directory path where the input images are located
images_left_dir = "/dhc/home/ennio.strohauer/endonerf_sample_datasets/cutting_tissues_twice/images"
images_right_dir = "/dhc/home/ennio.strohauer/endonerf_sample_datasets/cutting_tissues_twice/images_right"

# Set the output directory path where the generated images will be saved
output_dir = "/dhc/home/ennio.strohauer/endonerf_sample_datasets/HITNet_depth_unprocessed/cutting_tissues_twice_HITNet_m1"

# Iterate over the HARDCODED range of image numbers
# Example:
# 156 for cutting_tissues_twice Dataset
# 63 for pulling_soft_tissues Dataset

for image_num in range(156):
    # Generate the input image file path
    image_left_path = os.path.join(images_left_dir, f"{image_num:06d}.png")
    image_right_path = os.path.join(images_right_dir, f"{image_num:06d}.png")

    # Generate the output image file path
    output_path = os.path.join(output_dir, f"frame-{image_num:06d}.depth.png")

    # Build the bash command
    command = [
        "python",
        "predict.py",
        "--model",
        "StereoNet",
        "--ckpt",
        "ckpt/stereo_net.ckpt",
        "--images",
        image_left_path,
        image_right_path,
        "--output",
        output_path
    ]

    # Run the bash command
    subprocess.run(command)
