import threading # 导入threading模块
from queue import Queue #导入queue模块
import time  #导入time模块

# 爬取文章详情页
def get_detail_html(detail_url_list, id):
    while True:
        url = detail_url_list.get() #Queue队列的get方法用于从队列中提取元素
        time.sleep(2)  # 延时2s 模拟请求的耗时
        print("thread {id}: get {url} detail finished".format(id=id,url=url))
# 爬取文章列表页
def get_detail_url(queue):
    for i in range(10000):
        time.sleep(1) # 延迟一秒
        queue.put("http://testedu.com/{id}".format(id=i))# 从队列中获取URL
        print("get detail url {id} end".format(id=i))#打印出得到了哪些文章的url

#主函数
if __name__ == "__main__":
    exit(-1)
    detail_url_queue = Queue(maxsize=1000) #用Queue构造一个大小为1000的线程队列
    # 先创造四个线程
    thread = threading.Thread(target=get_detail_url, args=(detail_url_queue,)) #A线程负责抓取列表url
    html_thread= []
    for i in range(3):
        thread2 = threading.Thread(target=get_detail_html, args=(detail_url_queue,i))
        html_thread.append(thread2)#B C D 线程抓取文章详情
    start_time = time.time()
    # 启动四个线程
    thread.start()
    for i in range(3):
        html_thread[i].start()
    # 其父进程一直处于阻塞状态。
    thread.join()
    for i in range(3):
        html_thread[i].join()

print("last time: {} s".format(time.time()-start_time))# 计算总共耗时