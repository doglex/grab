from get_soup import get_soup


def parse_item(url: str) -> dict:
    try:
        soup = get_soup(url)
        # print(soup)
        return {
            "title": soup.find("meta", attrs={"property": "og:title"}).get("content"),
            "url": url,
            "keywords": soup.find("meta", attrs={"name": "keywords"}).get("content"),
            "description": soup.find("meta", attrs={"name": "description"}).get("content"),
            "actor": soup.find("meta", attrs={"property": "og:video:actor"}).get("content"),
            "director": soup.find("meta", attrs={"property": "og:video:director"}).get("content"),
            "release_date": soup.find("meta", attrs={"property": "og:video:release_date"}).get("content"),
            "alias": soup.find("meta", attrs={"property": "og:video:alias"}).get("content"),
            "area": soup.find("meta", attrs={"property": "og:video:area"}).get("content"),
            "score": soup.find("meta", attrs={"property": "og:video:score"}).get("content"),
            "class_": soup.find("meta", attrs={"property": "og:video:class"}).get("content"),
            "otitle": soup.find("meta", attrs={"property": "og:video:otitle"}).get("content"),
        }
    except Exception as e:
        print(f"Error parse {url}: {str(e)[:300]}")
        return {}


if __name__ == '__main__':
    url0 = "https://www.dandanzan10.top/dianying/16.html"
    ans = parse_item(url0)
    print(ans)
