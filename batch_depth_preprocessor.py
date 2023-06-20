import os
import numpy
import cv2

# Set the input directory path where the depthmaps were saved
input_dir = "/dhc/home/ennio.strohauer/endonerf_sample_datasets/depth_unprocessed/cutting_tissues_twice_HITNet"

#  Set the directory path where the mask is located
mask_dir = "/dhc/home/ennio.strohauer/endonerf_sample_datasets/cutting_tissues_twice_HITNet/masks"

# Set the output directory for preprocessed depthmaps
output_dir = "/dhc/home/ennio.strohauer/endonerf_sample_datasets/cutting_tissues_twice_HITNet/depth"

# Iterate over the HARDCODED range of image numbers
# 156 for cutting_tissues_twice
# 63 for pulling_soft_tissues

for image_num in range(156):
    # Generate the input image file path
    depthmap_path = os.path.join(input_dir, f"frame-{image_num:06d}.depth.png")
    mask_path = os.path.join(mask_dir, f"frame-{image_num:06d}.mask.png")

    depthmap = cv2.imread(depthmap_path, cv2.IMREAD_GRAYSCALE)
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
    masked_image = numpy.where(mask < 1, depthmap, 0)

    # Generate the output image file path
    output_path = os.path.join(output_dir, f"frame-{image_num:06d}.depth.png")
    cv2.imwrite(output_path, masked_image)

    print("Result saved successfully at", output_path)
