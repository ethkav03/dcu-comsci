def swap_keys_values(d):
   e = {}
   for key, value in d.items():
      e[value] = key
   return e
