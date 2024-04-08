import numpy as np
import matplotlib.pyplot as plt
import sys
import ti

def d(n): # Define a list of vectors by the normal vectors of the faces of a n faces dice
  assert n in [4, 6, 8, 12, 20], "n must be in [4, 6, 8, 12, 20]"
  v = []
  if n == 4: # 4 faces dice
    v.append((0, 0, -1))
  elif n == 6: # 6 faces dice
    v.append((1, 0, 0))
    v.append((0, 1, 0))
    v.append((0, 0, 1))
    v.append((-1, 0, 0))
    v.append((0, -1, 0))
    v.append((0, 0, -1))
  elif n == 8: # 8 faces dice
    return []
  elif n == 12: # 12 faces dice
    return []
  elif n == 20: # 20 faces dice
    return []
  return v

if __name__ == '__main__':
  ##################################################################################################
  # Parameters (change these values to adjust the behavior of the program)                         #
  ##################################################################################################
  NB_ITER = 10      # Number of iterations
  EPSILON = 25      # Acceptable distance between the two images
  VEC_LIST = d(6)   # List of vectors as normal vectors of the faces of a n faces dice 
  ##################################################################################################
  # Get the images paths
  a = sys.argv[1]
  b = sys.argv[2]
  # Load images
  im_a = plt.imread(a)
  im_b = plt.imread(b)
  im_a_norm = (im_a-np.min(im_a))/(np.max(im_a)-np.min(im_a)) * 255
  im_b_norm = (im_b-np.min(im_b))/(np.max(im_b)-np.min(im_b)) * 255
  # Apply the 3d transformation to the images
  print("0/6")
  res_a = ti._3d_dist(im_a_norm, im_b_norm, EPSILON)
  print("1/6")
  res_b = ti._3d_iter(im_a_norm, im_b_norm, NB_ITER)
  print("2/6")
  res_c = ti._3d_list(im_a_norm, im_b_norm, VEC_LIST)
  print("3/6")
  res_d = ti._3d_dist(im_b_norm, im_a_norm, EPSILON)
  print("4/6")
  res_e = ti._3d_iter(im_b_norm, im_a_norm, NB_ITER)
  print("5/6")
  res_f = ti._3d_list(im_b_norm, im_a_norm, VEC_LIST)
  print("6/6")
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
