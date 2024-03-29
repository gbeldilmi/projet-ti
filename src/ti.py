import numpy as np

class p1d:
  # This class represents a pixel of the image with its value and its coordinates
  # It is used to store the pixels of the image in a 1d array and still be able to restore the image
  def __init__(self, val, x, y):
    self.val = val
    self.x, self.y = x, y

class arr1d:
  def __init__(self, img):
    # Get the shape of the image
    self.h, self.w = img.shape
    # Create an array of p1d objects with the pixels of the image
    self.arr = []
    for i in range(self.h):
      for j in range(self.w):
        self.arr.append(p1d(img[i, j], i, j)) # Value, X, Y
  def mix(self, b):
    # Use a bijection to exchange the values of the arrays but keep the coordinates
    # Both arrays must have the same length, same type and be sorted
    assert len(self.arr) == len(b.arr), "Both arrays must have the same length"
    assert isinstance(b, arr1d), "Both arrays must be of the same type"
    self.arr = sorted(self.arr, key=lambda x: x.val)
    b.arr = sorted(b.arr, key=lambda p: p.val)
    # The value of the n-th element of a will be the value of the n-th element of b and vice versa
    for i in range(len(self.arr)):
      self.arr[i].val, b.arr[i].val = b.arr[i].val, self.arr[i].val
  def to_img(self):
    # Create an image with the same shape as the original image
    res = np.zeros((self.h, self.w))
    # Fill the image with the values of the array
    for i in self.arr:
      res[i.x, i.y] = i.val
    return res

def _1chan(a, b):
  # Convert a and b to 1d arrays
  arr_a = arr1d(a)
  arr_b = arr1d(b)
  # Exchange the values of the arrays
  arr_a.mix(arr_b)
  # Convert the arrays to images
  ra = arr_a.to_img()
  rb = arr_b.to_img()
  return ra, rb


class p3d:
  # This class represents a pixel of the image with its rgb values and its coordinates
  # It is used to store the pixels of the image in a 1d array and still be able to restore the image
  def __init__(self, r, g, b, x, y):
    self.r, self.g, self.b = r, g, b
    self.x, self.y = x, y

class arr3d:
  def __init__(self, img):
    # Get the shape of the image
    self.h, self.w, _ = img.shape
    # Get the center of the cloud of points in the rgb space

    ################################################################
    ################################################################
    self.center = np.mean(img, axis=(0, 1))
    ################################################################
    ################################################################
  
    
    # Create an array of p3d objects with the pixels of the image
    self.arr = []
    for i in range(self.h):
      for j in range(self.w):
        self.arr.append(p3d(*img[i, j], i, j)) # R, G, B, X, Y
  def transfer(self, b, vector=None):
    # Use sliced sliced optimal transport to move the values of the array to the values
    # of the array b in the rgb space
    if vector is None:
      vector = np.random.rand(3)
    # Get the center of the space

    ################################################################
    ################################################################

    
    # Project each pixel in the rgb space to the vector

    ################################################################
    ################################################################
    ################################################################
    ################################################################

    # Get the average of the projections

    ################################################################
    ################################################################
    ################################################################
    ################################################################

    # Move each pixel rgb value to the average of the projections

    ################################################################
    ################################################################
    ################################################################

    # Return the distance by which the pixels have been moved
    



  def transfer_by_iteration(self, b, nb_iter):
    # Both arrays must have the same length and type
    assert len(self.arr) == len(b.arr), "Both arrays must have the same length"
    assert isinstance(b, arr3d), "Both arrays must be of the same type"
    # Use the transfer method nb_iter times using random vectors
    for _ in range(nb_iter):
      self.transfer(b)
  def transfer_by_distance(self, b, epsilon):
    # Both arrays must have the same length and type
    assert len(self.arr) == len(b.arr), "Both arrays must have the same length"
    assert isinstance(b, arr3d), "Both arrays must be of the same type"
    last_distance = epsilon + 1
    # Use the transfer method until the distance is less than epsilon
    while last_distance > epsilon:
      last_distance = self.transfer(b)
  def to_img(self):
    # Create an image with the same shape as the original image
    res = np.zeros((self.h, self.w, 3))
    # Fill the image with the values of the array
    for i in self.arr:
      res[i.x, i.y] = i.r, i.g, i.b
    return res


def _3d(a, b):
  # Convert a and b to 3d arrays
  arr_a = arr3d(a)
  arr_b = arr3d(b)
  # Exchange the values of the arrays
  arr_a.transfer_by_distance(arr_b, )
  # Convert the arrays to images
  ra = arr_a.to_img()
  rb = arr_b.to_img()
  return ra, rb
