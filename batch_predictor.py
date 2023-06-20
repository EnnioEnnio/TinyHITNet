import os
import subprocess

# Set the directory path where the input images are located
images_left_dir = "/dhc/home/ennio.strohauer/endonerf_sample_datasets/cutting_tissues_twice_HITNet/images"
images_right_dir = "/dhc/home/ennio.strohauer/endonerf_sample_datasets/cutting_tissues_twice_HITNet/images_right"

# Set the output directory path where the generated images will be saved
output_dir = "/dhc/home/ennio.strohauer/endonerf_sample_datasets/depth_unprocessed/cutting_tissues_twice_HITNet"

# Iterate over the HARDCODED range of image numbers
# 156 for cutting_tissues_twice
# 63 for pulling_soft_tissues

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
