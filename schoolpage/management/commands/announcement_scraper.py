import requests
from lxml import html
from schoolpage.models import Announcement


url = "http://sfhs.nebo.edu"

announcement_xpath = "///div[@id='page']/section[@id='main']/article"


def get_announcements():
    page = requests.get(url)
    tree = html.fromstring(page.content)
    tree.xpath(announcement_xpath)
    return parse_page(tree)


def parse_page(page):
    announcement_list = []
    announcements = page.xpath(announcement_xpath)
    for announcement in announcements:
        header = ''.join(announcement.xpath('./header/h2/a/text()'))
        content = ''.join(announcement.xpath('.//div[@class="field-items even"]//text()'))
        image = ''.join(announcement.xpath('.//img/@src'))

        announcement_list.append(Announcement(header=header, content=content, image=image))

    return announcement_list
