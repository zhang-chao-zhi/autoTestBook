import time
import cv2
from selenium import webdriver
from selenium.webdriver import ActionChains
import numpy as np

def matchImg(img_path1,img_path2):
    imgs = []
    # 原始图像，用于展示
    sou_img1 = cv2.imread(img_path1)
    sou_img2 = cv2.imread(img_path2)

    # 原始图像，灰度
    # 最小阈值100,最大阈值500
    img1 = cv2.imread(img_path1, 0)
    blur1 = cv2.GaussianBlur(img1, (3, 3), 0)
    canny1 = cv2.Canny(blur1, 100, 500)
    cv2.imwrite('temp1.png', canny1)

    img2 = cv2.imread(img_path2, 0)
    blur2 = cv2.GaussianBlur(img2, (3, 3), 0)
    canny2 = cv2.Canny(blur2, 100, 500)
    cv2.imwrite('temp2.png', canny2)

    target = cv2.imread('temp1.png')
    template = cv2.imread('temp2.png')

    # 调整显示大小
    target_temp = cv2.resize(sou_img1, (350, 200))
    target_temp = cv2.copyMakeBorder(target_temp, 5, 5, 5, 5, cv2.BORDER_CONSTANT, value=[255, 255, 255])

    template_temp = cv2.resize(sou_img2, (200, 200))
    template_temp = cv2.copyMakeBorder(template_temp, 5, 5, 5, 5, cv2.BORDER_CONSTANT, value=[255, 255, 255])

    imgs.append(target_temp)
    imgs.append(template_temp)

    theight, twidth = template.shape[:2]

    # 匹配拼图
    result = cv2.matchTemplate(target, template, cv2.TM_CCOEFF_NORMED)

    # 归一化
    cv2.normalize( result, result, 0, 1, cv2.NORM_MINMAX, -1 )

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # 匹配后结果画圈
    cv2.rectangle(target,max_loc,(max_loc[0]+twidth,max_loc[1]+theight),(0,0,255),2)


    target_temp_n = cv2.resize(target, (350, 200))
    target_temp_n = cv2.copyMakeBorder(target_temp_n, 5, 5, 5, 5, cv2.BORDER_CONSTANT, value=[255, 255, 255])

    imgs.append(target_temp_n)

    imstack = np.hstack(imgs)

    cv2.imshow('stack'+str(max_loc), imstack)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
# 创建webdriver对象
browser = webdriver.Firefox()

# 登录页面URL
url = 'https://www.om.cn/login'

# 访问登录页面
browser.get(url)

handle = browser.current_window_handle

# 等待3s用于加载脚本文件
browser.implicitly_wait(3)

# 点击登陆按钮，弹出滑动验证码
btn = browser.find_element_by_class_name('login_btn1')
btn.click()

# 获取iframe元素
frame = browser.find_element_by_id('tcaptcha_iframe')
browser.switch_to.frame(frame)
# 延迟一秒
time.sleep(1)

# 获取背景图src
targetUrl = browser.find_element_by_id('slideBg').get_attribute('src')

# 获取拼图src
tempUrl = browser.find_element_by_id('slideBlock').get_attribute('src')


# 新建标签页
browser.execute_script("window.open('');")
# 切换到新标签页
browser.switch_to.window(browser.window_handles[1])

# 访问背景图src
browser.get(targetUrl)
time.sleep(3)
# 截图
browser.save_screenshot('temp_target.png')

w = 680
h = 390

img = cv2.imread('temp_target.png')

size = img.shape

top = int((size[0] - h) / 2)
height = int(h + ((size[0] - h) / 2))
left = int((size[1] - w) / 2)
width = int(w + ((size[1] - w) / 2))

cropped = img[top:height, left:width]

# 裁剪尺寸
cv2.imwrite('temp_target_crop.png', cropped)

# 新建标签页
browser.execute_script("window.open('');")

browser.switch_to.window(browser.window_handles[2])

browser.get(tempUrl)
time.sleep(3)

browser.save_screenshot('temp_temp.png')

w = 136
h = 136

img = cv2.imread('temp_temp.png')

size = img.shape

top = int((size[0] - h) / 2)
height = int(h + ((size[0] - h) / 2))
left = int((size[1] - w) / 2)
width = int(w + ((size[1] - w) / 2))

cropped = img[top:height, left:width]

cv2.imwrite('temp_temp_crop.png', cropped)

browser.switch_to.window(handle)

# 模糊匹配两张图片
move = matchImg('temp_target_crop.png', 'temp_temp_crop.png')

# 计算出拖动距离
distance = int(move / 2 - 27.5) + 2

draggable = browser.find_element_by_id('tcaptcha_drag_thumb')

ActionChains(browser).click_and_hold(draggable).perform()

# 拖动
ActionChains(browser).move_by_offset(xoffset=distance, yoffset=0).perform()

ActionChains(browser).release().perform()

time.sleep(10)