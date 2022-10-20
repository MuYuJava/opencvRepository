import numpy as np
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# sigmoid函数基本计算
def sigmoid_function(input_number):
    # 采取分段函数是为了防止input_number过大导致上溢出
    if input_number >= 0:
        return 1 / (np.exp(-input_number) + 1)
    else:
        return np.exp(input_number)/(1+np.exp(input_number))


# 利用列表存放输入值并循环调用sigmoid计算函数，利用用字典储存结果接收计算函数的返回值
# input_list = [-1000, -100, -10, -1, -0.1, -0.01, 0, 0.01, 0.1, 1, 10, 100, 1000]
# output_list = {}
# for i in input_list:
#     output_list[i] = sigmoid_function(i)
# print(output_list)
