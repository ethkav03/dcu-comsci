def swap_unique_keys_values(d):
   e = {}
   for k, v in d.items():
      if v not in e.keys():
         e[v] = k
      else:
         e[v] = 69
   f = {}
   for k, v in e.items():
      if v != 69:
         f[k] = v
   return f
