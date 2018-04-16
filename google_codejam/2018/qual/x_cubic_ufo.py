# https://codejam.withgoogle.com/2018/challenges/00000000000000cb/dashboard/00000000000079cc

import math

def norm(v):
    return math.sqrt(sum([x ** 2 for x in v]))

def dot(v1, v2):
    return sum([x * y for x, y in zip(v1, v2)])

# xz-plane: horizontal  y ^
# y-axis: vertical        |__> z
#                       x /

nvec_toronto = [0, 1, 0] # xz-plane, y-axis
nvec_planes = [[0.5, 0  , 0  ],
                [0  , 0.5, 0  ],
                [0  , 0  , 0.5]]

def rotate_about_z(a):
    # Only need to rotate about z-axis
    rad = math.asin(a / math.sqrt(2)) - math.pi / 4
    cos, sin = math.cos(rad), math.sin(rad)
    nvec_planes_new = []
    for i in range(2):
        x, y, z = nvec_planes[i]
        nvec_planes_new.append([x * cos - y * sin, x * sin + y * cos, z])
    nvec_planes_new.append(nvec_planes[2][:])
    return nvec_planes_new

def rotate_about_zx(a):
    # A is larger than sqrt(2),
    # so start with planes rotated by 45 deg. about z-axis first
    nvec_planes_sqrt2 = rotate_about_z(math.sqrt(2))
    rad = math.asin(a / math.sqrt(3)) - math.atan(math.sqrt(2))
    cos, sin = math.cos(rad), math.sin(rad)
    nvec_planes_new = []
    nvec_planes_new.append(nvec_planes_sqrt2[0][:])
    for i in range(1, 3):
        x, y, z = nvec_planes[i]
        nvec_planes_new.append([x, y * cos - z * sin, y * sin + z * cos])
    return nvec_planes_new

def rotate(a):
    # print('Toronto:', norm(nvec_toronto))
    if a <= math.sqrt(2):
        return rotate_about_z(a)
    else:
        return rotate_about_zx(a)
    # cos = dot(nvec_plane, nvec_toronto) / norm(nvec_plane) / norm(nvec_toronto)
    # print('Plane:', norm(nvec_plane))
    # print('Dot:', dot(nvec_plane, nvec_toronto))
    # print('cos:', dot(nvec_plane, nvec_toronto) / norm(nvec_plane) / norm(nvec_toronto))

if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        a = float(input())
        print('Case #{0}:'.format(i))
        for row in rotate(a):
            for elem in row:
                print('{0:.7f}'.format(elem), end=' ')
            print('')
