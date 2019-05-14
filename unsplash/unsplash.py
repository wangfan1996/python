import requests, json, time, sys

class get_photos(object):

    def __init__(self):
        self.photos_id = []
        self.download_server = 'https://unsplash.com/photos/xxx/download?force=trues'
        self.target = 'https://unsplash.com/napi/photos?page=3&per_page=5'

    def get_ids(self):
        req = requests.get(url=self.target)
        html = json.loads(req.text)
        for each in html:
            self.photos_id.append(each['id'])

    def download(self):
        for each in self.photos_id:
            target = self.download_server.replace('xxx', each)
            print(target)
            req = requests.get(url=target)
            with open(each+".jpg","wb") as code:
                code.write(req.content)
            print('图片:' + each + '下载成功')
            time.sleep(5)

if __name__ == '__main__':
    gp = get_photos()
    print('获取图片连接中:')
    gp.get_ids()
    gp.download()
    print('图片下载成功')


