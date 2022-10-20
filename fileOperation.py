import os
import cv2 as cv
import imageOperation as im
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# 查找目录是否存在
def file_find(filePath):
    result = os.path.exists(filePath)
    return result


# 生成目录
def make_dir(dir_pth):
    '''
    自动检查dir_pth是否存在，若存在，返回真，若不存在创建该路径，并返回假
    :param dir_pth: 路径
    :return: bool
    '''
    if os.path.exists(dir_pth):  ##目录存在，返回为真
        return True
    else:
        os.makedirs(dir_pth)
        return False


# 返回filePath下以后缀suffix结尾的文件绝对路径的list对象
def get_fpths_from_dir(filePath):
    result = []
    finalList = []
    for path, dirs, files in os.walk(filePath):  # 利用os.walk函数遍历指定文件目录中的path,dirs,files
        result.append(files)  # 将遍历结果中的文件添加至result列表中方便后续处理
    for item in result[0]:  # 利用循环操作，将result列表中的所有file进行字符处理，若file以.suffix结尾，则添加至finalList列表中
        if item.endswith(".suffix"):
            finalList.append(item)
    return finalList


# 返回filePath下以任意后缀结尾的所有文件，包含子目录的list对象
def get_all_files_pth(filePath, suffix):
    result = []
    finalList = []
    for path, dirs, files in os.walk(filePath):  # 利用os.walk函数遍历指定文件目录中的path,dirs,files
        result.append([path, files])  # 将遍历结果中的文件添加至result列表中方便后续处理
    for item in result:  # 利用双重循环将result列表中的所有文件进行判断是否以指定后缀结尾,并将文件路径和文件名连接添加至结果列表
        for enum in item[1]:
            if enum.endswith('.' + suffix):
                finalList.append(item[0]+'\\'+enum)
    return finalList


# path = "E:/python_test_workplace"  # 给定文件目录
# # result = get_fpths_from_dir(path)  # 调用函数获取path目录下以suffix结尾的文件
# result = get_all_files_pth(path, 'jpg')  # 调用函数获取path目录下所有以jpg结尾的文件
# # print(result)
# for i in result:
#     resultDic = im.cal_mean_std(i)
#     print(resultDic)
