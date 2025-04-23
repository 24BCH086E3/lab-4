for h in range(0, 24):
    if h == 0:
        print("12 Midnight")
    elif h < 12:
        print(f"{h} AM")
    elif h == 12:
        print("12 Noon")
    else:
        print(f"{h-12} PM")
