
def belt_rotation(arr):
    counter = 0
    while(counter < len(arr)/2):
        new_len = len(arr) -1 - counter
        if counter % 2 == 0:
            arr = cw_rotate(arr, counter, new_len)
        else:
            arr = ccw_rotate(arr, counter, new_len)
        counter +=1
    return arr

def cw_rotate(arr, counter, new_len):
    print counter, new_len
    ul, ur, dr, dl = arr[counter][counter], arr[counter][new_len], arr[new_len][new_len], arr[new_len ][counter]
    print ul, ur, dr, dl
    arr = l_r(arr, counter, counter, ul, counter, new_len) #(1,4)
    arr = u_d(arr, counter, new_len, ur, counter, new_len) #(1,4)
    arr = r_l(arr, new_len, new_len, dr, counter, new_len) #(1,4)
    arr = d_u(arr, new_len, counter, dl, counter, new_len) #(1,4)
    return arr

def ccw_rotate(arr, counter, new_len):
    print counter, new_len
    ul, ur, dr, dl = arr[counter][counter], arr[counter][new_len], arr[new_len][new_len], arr[new_len ][counter]
    print ul, dl, dr, ur
    arr = u_d(arr, counter, counter, ul, counter, new_len) #(1,4)
    arr = l_r(arr, new_len, counter, dl, counter, new_len) #(1,4)
    arr = d_u(arr, new_len, new_len, dr, counter, new_len) #(1,4)
    arr = r_l(arr, counter, new_len, ur, counter, new_len) #(1,4)
    return arr

def l_r (arr, i, j, ul, counter, new_len):
    temp1 = ul
    while (j < new_len):
        temp2 = arr[i][j+1]
        arr[i][j+1] = temp1
        temp1 = temp2
        j += 1
    return arr

def u_d (arr, i, j, ur, counter, new_len):
    temp1 = ur
    while (i < new_len):
        temp2 = arr[i+1][j]
        arr[i+1][j] = temp1
        temp1 = temp2
        i += 1
    return arr

def r_l (arr, i, j, dr, counter, new_len):
    temp1 = dr
    while (j > counter):
        temp2 = arr[i][j-1]
        arr[i][j-1] = temp1
        temp1 = temp2
        j -= 1
    return arr

def d_u (arr, i, j, dl, counter, new_len):
    temp1 = dl
    while (i > counter):
        temp2 = arr[i-1][j]
        arr[i-1][j] = temp1
        temp1 = temp2
        i -= 1
    return arr

arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
belt_rotation(arr)

#######################################################################################

def all_unique_or_not(line):
    set_=set()
    for i in line:
        if i !='.':
            if int(i) in set_:
                return False
            set_.add(int(i))
    return True

def sudoku2(grid):
    for line in grid:
        if not all_unique_or_not(line):
            return False
    
    for column_num in xrange(9):
        column = [grid[i][column_num] for i in xrange(9)]
        if not all_unique_or_not(column):
            return False
    
    for i in range(0,9,3):
        for j in range(0,9,3):
            if not all_unique_or_not(grid[i][j:j+3]+grid[i+1][j:j+3]+grid[i+2][j:j+3]):
                return False    
    return True

grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
sudoku2(grid)

#######################################################################################

# Failed_over_time_limit version 
def sumInRange(nums, queries):
    nums_count = [0 for i in xrange(len(nums))]
    
    for q in queries:
        for increment_index  in range(q[0],q[1]+1):
            nums_count[increment_index] += 1
    
    sum_ = 0
    for _ in xrange(len(nums)):
        sum_ += nums[_]*nums_count[_]

    return sum_%(1000000007)


# Success!
def sumInRange(nums, queries):
    prefix_sum=[0]
    sum_so_far = 0
    for num in nums:
        sum_so_far += num
        prefix_sum.append(sum_so_far)
        
    total_sum = 0
    for qurie_set in queries:
        start = qurie_set[0]
        end = qurie_set[1] + 1
        total_sum += prefix_sum[end] - prefix_sum[start]
    return total_sum % 1000000007

#######################################################################################

def findLongestSubarrayBySum(s, arr):
    i, j, longest_length, temp_sum = 0,0,0,0
    while (j<len(arr) and i <len(arr)):
        if temp_sum < s:
            temp_sum += arr[j]
            j+=1
        if temp_sum > s:
            temp_sum -= arr[i]
            i+=1
        if temp_sum == s:
            print "i:", i,"j:", j 
            if j - i > longest_length:
                longest_length = j - i 
                longest_set = [i+1,j]
            if j < len(arr):
                temp_sum += arr[j]
                j+=1
    if longest_length == 0:
        return [-1]   
    return longest_set

arr = [0,3,0]
s=3
findLongestSubarrayBySum(s, arr)

#######################################################################################

def findLongestSubarrayBySum(s, arr):
    i, j, longest_length, temp_sum = 0,0,0,0
    while (j<len(arr) and i <len(arr)):
        if temp_sum < s:
            temp_sum += arr[j]
            j+=1
        if temp_sum > s:
            temp_sum -= arr[i]
            i+=1
        if temp_sum == s:
            print "i:", i,"j:", j 
            if j - i > longest_length:
                longest_length = j - i 
                longest_set = [i+1,j]
            if j < len(arr):
                temp_sum += arr[j]
                j+=1
    if longest_length == 0:
        return [-1]   
    return longest_set

arr = [0,3,0]
s=3
findLongestSubarrayBySum(s, arr)

