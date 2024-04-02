import numpy as np
import matplotlib.pyplot as plt
import ti

if __name__ == '__main__':
  # Load images
  im_a = plt.imread('res/a.JPG')
  im_b = plt.imread('res/b.JPG')
  # Apply the 3d transformation to the images
  res_a = ti._3d_dist(im_a, im_b, 0.1)
  res_b = ti._3d_iter(im_a, im_b, 100)
  res_c = ti._3d_list(im_a, im_b, [(1, 0, 0), (0, 1, 0), (0, 0, 1)])
  res_d = ti._3d_dist(im_b, im_a, 0.1)
  res_e = ti._3d_iter(im_b, im_a, 100)
  res_f = ti._3d_list(im_b, im_a, [(1, 0, 0), (0, 1, 0), (0, 0, 1)])
  # Display the results
  plt.figure("Test 3d on RGB images")
  # Original images
  plt.subplot(2, 4, 1)
  plt.imshow(im_a)
  plt.title("Original image A")
  plt.subplot(2, 4, 2)
  plt.imshow(im_b)
  plt.title("Original image B")
  # Result images
  plt.subplot(2, 4, 3)
  plt.imshow(res_a)
  plt.title("Result image A (with B color) (dist)")
  plt.subplot(2, 4, 5)
  plt.imshow(res_b)
  plt.title("Result image A (with B color) (iter)")
  plt.subplot(2, 4, 7)
  plt.imshow(res_c)
  plt.title("Result image A (with B color) (list)")
  plt.subplot(2, 4, 4)
  plt.imshow(res_d)
  plt.title("Result image B (with A color) (dist)")
  plt.subplot(2, 4, 6)
  plt.imshow(res_e)
  plt.title("Result image B (with A color) (iter)")
  plt.subplot(2, 4, 8)
  plt.imshow(res_f)
  plt.title("Result image B (with A color) (list)")
  plt.show()
