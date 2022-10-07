def caught_speeding(speed, is_birthday):
  if is_birthday:
    if 0 <= speed < 66:
      return 0
    elif  66 <= speed <= 86:
      return 1
    elif speed > 86:
      return 2
  elif not is_birthday:
    if 0 <= speed < 61:
      return 0
    elif 61 <= speed <= 80:
      return 1
    elif speed >= 81:
      return 2