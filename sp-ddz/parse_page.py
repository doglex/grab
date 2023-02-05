from parse_item import parse_item
from get_soup import get_soup
import pandas as pd
from datetime import datetime

url_prefix = "https://www.dandanzan10.top"
column_order = ["title", "url", "keywords", "actor", "director", "release_date",
                "alias", "area", "score", "class_", "otitle", "description"]


def parse_page(url: str) -> None:
    print(datetime.now(), url)
    try:
        soup = get_soup(url)
        # print(soup)
        infos = []
        for item in soup.find_all("a", class_="thumbnail"):
            url_part = item.get("href")
            url_item = f"{url_prefix}/{url_part.lstrip('/')}"
            item_info = parse_item(url_item)
            if not item_info:
                continue
            # print(item_info)
            infos.append(item_info)
        df = pd.DataFrame(infos)
        df = df[column_order]
        df.to_csv(f"store/{url.replace(url_prefix, '').lstrip('/').replace('/', '_')}.csv", index=False, header=False,
                  encoding="UTF-8")
    except Exception as e:
        print(f"Error page {url}: {str(e)[:300]}")


if __name__ == '__main__':
    url0 = "https://www.dandanzan10.top/dongman/index_379.html"
    parse_page(url0)
