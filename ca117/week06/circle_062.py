def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
   from math import sqrt

   rad = r1 + r2
   distance = sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
   if distance < 0:
      distance = distance * -1
   return distance < rad
