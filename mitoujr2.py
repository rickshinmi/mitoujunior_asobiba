import time
import math

def animation(sts, times=3, interval=0.25):
  d = 0
  dd = 0
  for n in range(times):
      for st in sts:
        m = [[" "]*40 for i in range(40)]
        for d in range(0, 360, 60):
          cossy = math.cos(math.radians(d+dd))
          sinny = math.sin(math.radians(d+dd))
          for c in range(20):
            m[math.floor(19+sinny*c)][math.floor(19+cossy*c)] = st[c]
        print('\n'.join([''.join(l) for l in m])+'\n')
        time.sleep(interval)
        dd+=10

sts = [
    "（・∀・）ﾐ       ",
    " （・∀・）ﾐﾄ     ",
    "  （・∀・）ﾐﾄｳ   ",
    "   （・∀・）ﾐﾄｳｼﾞ    ",
    "    （・∀・）ﾐﾄｳｼﾞｭﾆ   ",
    "     （・∀・）ﾐﾄｳｼﾞｭﾆｱ  ",
]

sts = [s+" "*(20-len(s)) for s in sts]

times = 3
interval = 0.25
animation(sts, times, interval)
