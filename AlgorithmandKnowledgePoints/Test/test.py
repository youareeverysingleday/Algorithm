# def calc(m, values, loc, count):
#     print(m, values, loc, count)
#     if loc >= len(values):
#         return count
#     temp = m%values[loc]
#     amount = int(m/values[loc])
#     print(temp, amount)
#     if temp == 0:
#         count += amount
#         return count
#     count += amount
#     return calc(m=temp, values=values[loc+1:], loc=0, count=count)

# temp = input().split(' ')
# n = int(temp[0])
# m = int(temp[1])
# values = [int(x) for x in list(input().split(' '))]
# values.sort(reverse=True)
# methodCount = calc(m, values, 0, 0)
# print(methodCount)


# def calc(n):
#     dp = [1, 2, 4]
#     method_amount = 0
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     elif n == 3:
#         return 4
#     else:
#         i = 3 
#         while i <= n:
#             print(i, dp)
#             method_amount = dp[2] + dp[1] + dp[0]
#             temp = dp
#             dp[0] = temp[1]
#             dp[1] = temp[2]
#             dp[2] = method_amount
#             i += 1
        
#         return method_amount%2021

# n = int(input())
# result = calc(n)
# print(result)

# def calculation(k):
#     y0 = [1]
#     y1 = [1,1]
    
#     for i in range(3, k+1):
#         y0 = [0 for _ in range(i)]
#         # print('y0 = {}'.format(y0))
#         # print(len(y0), len(y1))
#         # 对应层中每个元素的位置。
#         for j in range(i):
#             # print(i, j)
#             if j == 0:
#                 y0[j] = 1
#                 # print('j=0 j={}, y0={}'.format(j, y0))
#             elif j == i-1:
#                 y0[j] = 1
#                 # print('j=i-1 j={}, y0={}'.format(j, y0))
#             else:
#                 # print(j)
#                 y0[j] = y1[j-1] + y1[j]
#                 # print('else j={}, y0={}'.format(j, y0))
#         # 交换内容。
#         y1 = y0
#         # print(y0)

#     y0str = ','.join([str(x) for x in y0])
#     return y0str

# k = int(input())
# result = calculation(k)   
# print(result)


# def calculation(triangle):
#     row = len(triangle)
#     column = len(triangle[0])
    
#     # dp = np.zeros((4, 4), dtype=int)
#     dp = [[0 for _ in range(column)] for _ in range(row)]
#     print(dp)
    
#     for i in range(row):
#         temp = []
#         for j in range(column):
#             if j > i:
#                 continue
#             if i == 0 and j == 0:
#                 dp[i][j] = triangle[i][j]
#             else:
#                 if j - 1 < 0:
#                     dp[i][j] = triangle[i][j] + dp[i-1][j]
#                 elif i == j:
#                     dp[i][j] = triangle[i][j] + dp[i-1][j-1]
#                 else:
#                     dp[i][j] = max(triangle[i][j] + dp[i-1][j], triangle[i][j] + dp[i-1][j-1])

#     return max(dp[-1])


# n = int(input())
# triangle = []
# for i in range(n):
#     templist = [int(x) for x in list(input().split(' '))]
#     # 补齐0 。
#     if len(templist) < n:
#         for i in range(n-len(templist)):
#             templist.append(0)
#     triangle.append(templist)

# result = calculation(triangle)
# print(result)



# def calc(length, nums):
#     numsset = set(nums)
#     numsdict = {key:0 for key in numsset}
#     # print(numsdict)

#     for element in nums:
#         # print(element)
#         numsdict[element] +=  1
#         print(numsdict)
#         # numsset = set()
    
#     sorted_by_value_desc = sorted(numsdict.items(), key=lambda x: x[1], reverse=True)
#     # sorted_by_value_desc = sorted(numsdict.items(), key=lambda x: x[1])
#     print(sorted_by_value_desc)
#     # print(list(sorted_by_value_desc.keys()).sort()[0])
#     return sorted_by_value_desc[0][0]

# length = int(input())
# nums = [int(x) for x in list(input().split(' '))]

# result = calc(length, nums)
# print(result)



# nw = [int(x) for x in list(input().split(' '))]
# n = nw[0]
# W = nw[1]

# weight = [int(x) for x in list(input().split(' '))]
# values = [int(x) for x in list(input().split(' '))]

# def calc(n, W, weight, values):
#     # itemcount = len(values)

#     dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

#     for i in range(1, n + 1):
#         for j in range(1, W + 1):
#             if weight[i-1] > j:
#                 dp[i][j] = dp[i-1][j]
#             else:
#                 dp[i][j] = max(dp[i-1][j], values[i-1] + dp[i-1][j-weight[i-1]])

#     return dp[-1][-1]

# result = calc(n, W, weight, values)
# print(result)



# tm = [int(x) for x in list(input().split(' '))]
# t = tm[0]
# m = tm[1]

# times = []
# values = []

# for i in range(m):
#     temp = [int(x) for x in list(input().split(' '))]
#     times.append(temp[0])
#     values.append(temp[1])

# def calc(t, times, values):
#     dp = [[0 for _ in range(t+1)] for _ in range(len(values) + 1)]

#     for i in range(1, len(values) + 1):
#         for j in range(1, t+1):
#             if times[i-1] > j:
#                 dp[i][j] = dp[i-1][j]
#             else:
#                 dp[i][j] = max(dp[i][j-times[i-1]] + values[i-1], dp[i-1][j])
#     print('helloworld')
#     return dp[-1][-1]

# # print(times, values)
# result = calc(t, times, values)
# print(result)





# 完全背包。
import sys
n_amount = [int(x) for x in list(input().split(' '))]
n = n_amount[0]
amount = n_amount[1]

coins = [int(x) for x in list(input().split(' '))]

def calc(n, amount, coins):
    dp = [float('inf')] * (amount + 1)  # 创建动态规划数组，初始值为正无穷大
    dp[0] = 0  # 初始化背包容量为0时的最小硬币数量为0

    for coin in coins:  # 遍历硬币列表，相当于遍历物品
        for i in range(coin, amount + 1):  # 遍历背包容量
            if dp[i - coin] != float('inf'):  # 如果dp[i - coin]不是初始值，则进行状态转移
                dp[i] = min(dp[i - coin] + 1, dp[i])  # 更新最小硬币数量

    if dp[amount] == float('inf'):  # 如果最终背包容量的最小硬币数量仍为正无穷大，表示无解
        return -1
    return dp[amount] 


result = calc(n, amount, coins)
print(result)