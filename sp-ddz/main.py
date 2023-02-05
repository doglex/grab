import gevent
from gevent import monkey

monkey.patch_all()  # patch network and io
from gevent.pool import Pool
from parse_page import parse_page

# name, cate, start, end
tasks = [
    ["电影", "dianying", 1, 2983],
    ["电视剧", "dianshiju", 1, 1106],
    ["综艺", "zongyi", 1, 255],
    ["动漫", "dongman", 1, 379],
]

url_template1 = "https://www.dandanzan10.top/{}/"
url_template2 = "https://www.dandanzan10.top/{}/index_{}.html"

if __name__ == '__main__':
    pool = Pool(100)
    pool.map(
        parse_page,
        [
            url_template1.format(cate) if page == 1
            else url_template2.format(cate, page)
            for _, cate, start, end in tasks for page in range(start, end)
        ]
    )
