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
  # Extract each channel from the images
  im_a_r = im_a[...,0]
  im_a_g = im_a[...,1]
  im_a_b = im_a[...,2]
  im_b_r = im_b[...,0]
  im_b_g = im_b[...,1]
  im_b_b = im_b[...,2]
  # Apply the 1chan transformation to each channel
  res_a_r, res_b_r = ti._1chan(im_a_r, im_b_r)
  res_a_g, res_b_g = ti._1chan(im_a_g, im_b_g)
  res_a_b, res_b_b = ti._1chan(im_a_b, im_b_b)
  # Recombine the channels
  w, h, c = im_a.shape
  res_a = np.zeros((w, h, c))
  res_b = np.zeros((w, h, c))
  res_a[:, :, 0] = res_a_r
  res_a[:, :, 1] = res_a_g
  res_a[:, :, 2] = res_a_b
  res_b[:, :, 0] = res_b_r
  res_b[:, :, 1] = res_b_g
  res_b[:, :, 2] = res_b_b
  ma = np.max(res_a)
  mb = np.max(res_b)
  res_a /= ma
  res_b /= mb
  # Display the results
  plt.rcParams["font.size"]=5
  plt.figure("Test on each channel of RGB images")
  # Original images
  plt.subplot(2, 2, 1)
  plt.imshow(im_a)
  plt.title("Original image A")
  plt.subplot(2, 2, 2)
  plt.imshow(im_b)
  plt.title("Original image B")
  # Result images
  plt.subplot(2, 2, 3)
  plt.imshow(res_a)
  plt.title("Result image A (with B color)")
  plt.subplot(2, 2, 4)
  plt.imshow(res_b)
  plt.title("Result image B (with A color)")
  plt.savefig(out, dpi=500)
