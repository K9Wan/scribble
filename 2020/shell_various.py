import itertools
import random

intervals_list=[
    reversed((1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 27, 32, 36, 48, 54, 64, 72, 81, 96, 108, 128, 144, 162, 192, 216, 243, 256, 288, 324, 384, 432, 486, 512, 576, 648, 729, 768, 864, 972, 1024, 1152, 1296, 1458, 1536, 1728, 1944, 2048, 2187, 2304, 2592, 2916, 3072, 3456, 3888)),
    reversed((1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096)),
    reversed((1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095)),
    reversed((1, 3, 5, 9, 17, 33, 65, 129, 257, 513, 1025, 2049, 4097)),
    reversed((1, 4, 13, 40, 121, 364, 1093, 3280)),
    reversed((1, 2, 19, 103, 311, 691, 1321, 2309, 3671)),
    reversed((1, 2, 4, 8, 9, 16, 18, 25, 32, 36, 49, 50, 64, 72, 81, 98, 100, 121, 128, 144, 162, 169, 196, 200, 225, 242, 256, 288, 289, 324, 338, 361, 392, 400, 441, 450, 484, 512, 529, 576, 578, 625, 648, 676, 722, 729, 784, 800, 841, 882, 900, 961, 968, 1024, 1058, 1089, 1152, 1156, 1225, 1250, 1296, 1352, 1369, 1444, 1458, 1521, 1568, 1600, 1681, 1682, 1764, 1800, 1849, 1922, 1936, 2025, 2048, 2116, 2178, 2209, 2304, 2312, 2401, 2450, 2500, 2592, 2601, 2704, 2738, 2809, 2888, 2916, 3025, 3042, 3136, 3200, 3249, 3362, 3364, 3481, 3528, 3600, 3698, 3721, 3844, 3872, 3969, 4050, 4096, 4225, 4232, 4356, 4418)),
    reversed((1, 3, 9, 27, 81, 243, 729, 2187)),
    reversed((1, 5, 19, 41, 109, 209, 505, 929, 2161, 3905)),
    reversed((1, 8, 23, 77, 281, 1073, 4193)),
    reversed((1, 3, 7, 21, 48, 112, 336, 861, 1968, 4592)),
    reversed((1, 19, 83, 211, 467, 979, 2003, 4051)),
    reversed((1, 4, 10, 23, 57, 132, 301, 701, 1750)),
    reversed((1, 4, 9, 20, 46, 103, 233, 525, 1182, 2660, 5985)),
    reversed((1, 2, 4, 8, 21, 56, 149, 404, 1098, 2982)),
    reversed((1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, 30, 32, 36, 40, 45, 48, 50, 54, 60, 64, 72, 75, 80, 81, 90, 96, 100, 108, 120, 125, 128, 135, 144, 150, 160, 162, 180, 192, 200, 216, 225, 240, 243, 250, 256, 270, 288, 300, 320, 324, 360, 375, 384, 400, 405, 432, 450, 480, 486, 500, 512, 540, 576, 600, 625, 640, 648, 675, 720, 729, 750, 768, 800, 810, 864, 900, 960, 972, 1000, 1024, 1080, 1125, 1152, 1200, 1215, 1250, 1280, 1296, 1350, 1440, 1458, 1500, 1536, 1600, 1620, 1728, 1800, 1875, 1920, 1944, 2000, 2025, 2048, 2160, 2187, 2250, 2304, 2400, 2430, 2500, 2560, 2592, 2700, 2880, 2916, 3000, 3072, 3125, 3200, 3240, 3375, 3456, 3600, 3645, 3750, 3840, 3888, 4000, 4050, 4096)),
    reversed((1, 2, 3, 8, 23, 53, 107, 221, 365, 611, 1024, 2187, 4096)),
    reversed((1, 2, 3, 8, 27, 64, 243, 1024, 2187, 4096)),
    reversed((1, 2, 3, 4, 6, 9, 16, 24, 36, 54, 81, 128, 192, 288, 432, 648, 972, 1458, 2187, 4096, 6144)),
    #reversed((1, 2, 3, 4, 6, 9, 16, 24, 25, 64, 120, 125, 216, 625, 720, 1296, 2401, 5040))
]

## https://oeis.org/A036561

intervals_list=[*map(list, intervals_list)]

counts = [0]*len(intervals_list)


def shellSort(arr, n):
    
    arrays = [*map(list, itertools.tee(arr, len(intervals_list)))]
    for num, intervals in enumerate(intervals_list):
        array=arrays.pop(0)
        for interval in intervals:
            if interval >= n: continue
            for i in range(interval, n):
                temp = array[i]
                j = i
                while j >= interval and array[j - interval] > temp:
                    array[j] = array[j - interval]
                    j -= interval
                    counts[num] += 1
    
                array[j] = temp
        arrays.append(array)
    return arrays

maxn=1000
size=5000
arr = [random.randint(0,maxn) for i in range(size)]
sorted_arrs=shellSort(arr, size)
#print(*sorted_arrs, sep='\n')
print(counts)
print()
result = [*zip(map(lambda x: [*x][-7:],intervals_list), counts)]
result.sort(key=lambda x:x[1])
print(*result, sep='\n')
print()
for r in result:
    print(*map(lambda x: repr(x).rjust(1+len(str(max(map(lambda x:x[0],[*zip(*result)][0]))))),r[0]), sep=',', end=' ')
    print(r[1])
print()
for r in result:
    print(str(r[1]).ljust(1+len(str(result[-1][1]))),r[0])
