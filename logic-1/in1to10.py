def in1to10(n, outside_mode):
  if not outside_mode:
    if 1 <= n <= 10:
      return True
    else:
      return False
  if outside_mode:
    if n<=1 or n >=10:
      return True
    else: return False
 