import requests
from urllib import parse


def doubantest(name):
    url = 'https://search.douban.com/movie/subject_search'
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": 'bid=5Tlfm0C3t5g; _pk_ref.100001.2939=%5B%22%22%2C%22%22%2C1613802918%2C%22https%3A%2F%2Fmovie.douban.com%2Fexplore%22%5D; _pk_ses.100001.2939=*; ll="108288"; __utmc=30149280; __utma=30149280.1549413386.1613802960.1613802960.1613802960.1; __utmz=30149280.1613802960.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; dbcl2="233581190:Y+kBgzIaWmE"; ck=8siy; push_noty_num=0; push_doumail_num=0; __utmv=30149280.23358; _vwo_uuid_v2=D2813C9931BE7444E88AF888C012646D5|88f6e966d5c44c6a742643f8652c89fa; _pk_id.100001.2939=527ff31490b2bea8.1613802918.1.1613803735.1613802918.; __utmt=1; __utmb=30149280.6.10.1613802960; __yadk_uid=jbNsyHVl1kwV9jEawkufhrucc2zv3OMz',
        "Host": "search.douban.com",
        "Referer": "https: // movie.douban.com/",
        "sec-ch-ua": '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
    }
    params = {
        "search_text": name,
        "cat": 1002
    }
    response = requests.get(url=url, params=params, headers=headers)
    page_source = response.content
    with open(file="%s.html" % name, mode="wb") as f:
        f.write(page_source)


if __name__ == '__main__':
    name = "斗罗大陆"
    doubantest(name)
