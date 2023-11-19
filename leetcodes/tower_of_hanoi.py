import sys
def show_directions(start, end, amount):
    if amount == 1:
        print(start, end)
        return

    other = 6 - (start+end)
    
    show_directions(start, other, amount - 1)
    print(start, end)
    show_directions(other, end, amount - 1)


show_directions(1, 3, int(sys.argv[-1]) if len(sys.argv) > 1 else 3)