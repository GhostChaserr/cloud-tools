import random

def generate_random_treshhold():

  tresh_ranges = [ [50, 255], [100, 255] ]
  tresh_values = []

  for tresh_arr in tresh_ranges:
    tresh_value = random.randint(tresh_arr[0], tresh_arr[1])
    tresh_values.append(tresh_value)
    
  return tresh_values
