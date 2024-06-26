import numpy as np
import matplotlib.pyplot as plt
import sys
import ti

if __name__ == '__main__':
  a = sys.argv[1]
  b = sys.argv[2]
  out = sys.argv[3]
  # Load images
  im_a = plt.imread(a)
  im_b = plt.imread(b)
  # Convert rgb to grayscale
  im_a = np.dot(im_a[...,:3], [0.299, 0.587, 0.114])
  im_b = np.dot(im_b[...,:3], [0.299, 0.587, 0.114])
  # Apply the 1chan transformation
  res_a, res_b = ti._1chan(im_a, im_b)
  # Display the results
  plt.rcParams["font.size"]=5
  plt.figure("Test on grayscale images")
  # Original images
  plt.subplot(2, 2, 1)
  plt.imshow(im_a, cmap='gray', vmin=0, vmax=255)
  plt.title("Original image A")
  plt.subplot(2, 2, 2)
  plt.imshow(im_b, cmap='gray', vmin=0, vmax=255)
  plt.title("Original image B")
  # Result images
  plt.subplot(2, 2, 3)
  plt.imshow(res_a, cmap='gray', vmin=0, vmax=255)
  plt.title("Result image A (with B color)")
  plt.subplot(2, 2, 4)
  plt.imshow(res_b, cmap='gray', vmin=0, vmax=255)
  plt.title("Result image B (with A color)")
  plt.savefig(out, dpi=500)
