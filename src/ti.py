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
    self.max = np.max(img)
    if self.max <= 1:
      self.max = 1
    else:
      self.max = 255
    # Create an array of p3d objects with the pixels of the image
    self.arr = []
    for i in range(self.h):
      for j in range(self.w):
        self.arr.append(p3d(*img[i, j], i, j)) # R, G, B, X, Y

  def transfer(self, b, vector=None):
    # Use sliced sliced optimal transport to move the values of the array to the values
    # of the array b in the rgb space
    def get_lambda(p, v): # Get the ratio between distance of the center and the projection and the vector
      return v[0] * p.r + v[1] * p.g + v[2] * p.b
    # If vector is undefined, generate a random vector
    if vector is None:
      vector = [random.random() for _ in range(3)]
    # Project each pixel in the rgb space to the vector and sort the projections
    proj_a = sorted([(get_lambda(p, vector), p) for p in self.arr], key=lambda x: x[0])
    proj_b = sorted([(get_lambda(p, vector), p) for p in b.arr], key=lambda x: x[0])
    # Get the difference of the projections
    diff_proj = [proj_b[i][0] - proj_a[i][0] for i in range(len(proj_a))]
    # Get the average of the projections
    avg_diff_proj = sum(diff_proj) / len(diff_proj)
    # Move each pixel rgb value by the value of the difference of the projections
    for i in range(len(self.arr)):
      self.arr[i].r += avg_diff_proj * vector[0]
      self.arr[i].g += avg_diff_proj * vector[1]
      self.arr[i].b += avg_diff_proj * vector[2]
    # Return the average of the projections
    return avg_diff_proj

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

  def transfer_by_vector_list(self, b, vectors):
    # Both arrays must have the same length and type
    assert len(self.arr) == len(b.arr), "Both arrays must have the same length"
    assert isinstance(b, arr3d), "Both arrays must be of the same type"
    # Use the transfer method with the given vectors
    for vector in vectors:
      self.transfer(b, vector)

  def to_img(self):
    # Create an image with the same shape as the original image
    res = np.zeros((self.h, self.w, 3))
    # Fill the image with the values of the array
    for i in self.arr:
      # Clamp the values to the range [0, max]
      a = i.r
      b = i.g
      c = i.b
      if a < 0:
        a = 0
      if a > self.max:
        a = self.max
      if b < 0:
        b = 0
      if b > self.max:
        b = self.max
      if c < 0:
        c = 0
      if c > self.max:
        c = self.max
      # Set the pixel to the rgb values
      res[i.x, i.y] = a,b,c
    return res



def _3d_dist(a, b, epsilon):
  # Convert a and b to 3d arrays
  arr_a = arr3d(a)
  arr_b = arr3d(b)
  # Exchange the values of the arrays
  arr_a.transfer_by_distance(arr_b, epsilon)
  # Convert the arrays to images
  ra = arr_a.to_img()
  return ra



def _3d_iter(a, b, nb_iter):
  # Convert a and b to 3d arrays
  arr_a = arr3d(a)
  arr_b = arr3d(b)
  # Exchange the values of the arrays
  arr_a.transfer_by_iteration(arr_b, nb_iter)
  # Convert the arrays to images
  ra = arr_a.to_img()
  return ra



def _3d_list(a, b, vectors):
  # Convert a and b to 3d arrays
  arr_a = arr3d(a)
  arr_b = arr3d(b)
  # Exchange the values of the arrays
  arr_a.transfer_by_vector_list(arr_b, vectors)
  # Convert the arrays to images
  ra = arr_a.to_img()
  return ra
