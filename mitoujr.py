import time

def animation(sts, times=3, interval=0.25):
  for n in range(times):
    for st in sts:
      print(st, end="")
      time.sleep(interval)
      print("\r", end="")
  print()

sts = [
    "（・∀・）ﾐ       ",
    " （・∀・）ﾐﾄ     ",
    "  （・∀・）ﾐﾄｳ   ",
    "   （・∀・）ﾐﾄｳｼﾞ    ",
    "    （・∀・）ﾐﾄｳｼﾞｭﾆ   ",
    "     （・∀・）ﾐﾄｳｼﾞｭﾆｱ  ",
]

times = 3
interval = 0.25
animation(sts, times, interval)