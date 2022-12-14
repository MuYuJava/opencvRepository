import cv2
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# 返回指定文件夹下（含子目录）返回所有图片整体的均值与标准差
def cal_mean_std(image_dir):
    resultDic = {}
    image = cv2.imread(image_dir, cv.IMREAD_COLOR)
    mean, dev = cv2.meanStdDev(image)
    # 格式化均值与方差结果并存入resultDic字典中
    meanList = [mean[0][0], mean[1][0], mean[2][0]]
    devList = [dev[0][0], dev[1][0], dev[2][0]]
    resultDic['image_dir'] = image_dir
    resultDic['mean'] = meanList
    resultDic['dev'] = devList
    return resultDic
