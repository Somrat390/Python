import math
def print_cal(height, width, cover):
    can = (height * width) / cover
    print(f"You will need {math.ceil(can)} to paint")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
print_cal(height=test_h, width=test_w, cover=coverage)



