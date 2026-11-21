def calculate_brightness(img):
    # Write your code here
    if not img or not img[0]:   return -1
    row_len = len(img[0])
    t = c = 0
    for r in img:
        if len(r) != row_len: return -1
        for p in r:
            if p < 0 or p >255: return -1
            t +=p
            c +=1
    return round(t/c, 2)
