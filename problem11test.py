# Problem 11 Testing

from problem11 import get_product, grid_function

test_grid_1 = [[8,1,2,3,4],
[49,2,3,4,5],
[81,3,4,5,6],
[52,4,5,6,7],
[22,5,6,7,8]]

# # DOWN:
# down = str(get_product([8,49,81,52])) + ', ' + str(get_product([49,81,52,22])) + ', ' + str(get_product([1,2,3,4])) + ', ' + str(get_product([2,3,4,5])) + ', ' + str(get_product([3,4,5,6])) + ', ' + str(get_product([4,5,6,7])) + ', ' + str(get_product([5,6,7,8]))
# # 1651104, 4540536

# # RIGHT:
# right = str(get_product([8,1,2,3])) + ', ' + str(get_product([1,2,3,4])) + ', ' + str(get_product([49,2,3,4])) + ', ' + str(get_product([2,3,4,5])) + ', ' + str(get_product([81,3,4,5])) + ', ' + str(get_product([3,4,5,6])) + ', ' + str(get_product([52,4,5,6])) + ', ' + str(get_product([4,5,6,7])) + ', ' + str(get_product([22,5,6,7])) + ', ' + str(get_product([5,6,7,8]))
# 48, 24, 1176, 120, 4860, 360, 6240, 840, 4620, 1680

# # DIAG DOWN RIGHT:
# print get_product([8,2,4,6])
# print get_product([1,3,5,7])
# print get_product([49,3,5,7])
# print get_product([2,4,6,8])

# DIAG DOWN LEFT
print get_product([4,4,4,4])
print get_product([3,3,3,52])
print get_product([5,5,5,5])
print get_product([4,4,4,22])

# With diagonal 
expecting = sorted([1651104, 4540536, 840, 48, 24, 1176, 120, 4860, 360, 6240, 4620, 1680, 384, 105, 5145, 256, 1404, 625, 1408])
# print expecting

print 'Expecting \n' + str(expecting)
print grid_function(test_grid_1, 4)