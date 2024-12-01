def calculate_paper(l, w, h):
    side1 = l * w
    side2 = w * h
    side3 = h * l
    surface_area = 2 * (side1 + side2 + side3)
    slack = min(side1, side2, side3)
    return surface_area + slack

def calculate_ribbon(l, w, h):
    dims = sorted([l, w, h])
    wrap_ribbon = 2 * dims[0] + 2 * dims[1]
    bow_ribbon = l * w * h
    return wrap_ribbon + bow_ribbon

def main():
    total_paper = 0
    total_ribbon = 0
    
    with open('input.txt', 'r') as file:
        for line in file:
            l, w, h = map(int, line.strip().split('x'))
            total_paper += calculate_paper(l, w, h)
            total_ribbon += calculate_ribbon(l, w, h)
    
    print(f"square feet of wrapping paper needed: {total_paper}")
    print(f"feet of ribbon needed: {total_ribbon}")

if __name__ == "__main__":
    main()
