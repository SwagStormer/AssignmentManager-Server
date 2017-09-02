import requests
import json
from lxml import html


# WARNING: Do not use the ':' character in SMTP messages
url = "https://sisweb.nebo.edu/Login.aspx"


class Grade:
    def __init__(self, grade, course_name):
        self.grade = grade
        self.course_name = course_name


# Request the sis page


def request_page(username, password):
    data = {"username": username, "password": password}
    s = requests.Session()
    r = s.post(url, data=data)
    tree = html.fromstring(r.text)
    return tree


# Parse all of the data from the html


def get_class(tree):
    grades = tree.xpath(
        '//span[@class="academicMark" or not(normalize-space(.))]/text()')
    # TODO add query to student object to find the users student account
    # TODO pull grades for the specific user
    for indx, element in enumerate(grades):
        if element == "\r\n\t\t\t\t":
            grades[indx] = "No grade"
    course_names = tree.xpath(
        '//div[@class="tab-pane active"]//strong[@class="linkBlack"]/text()')
    return [Grade(grades[i], course_names[i]) for i in range(0, len(course_names))]


# Format the output into a long string


def is_valid(sis_username, sis_password):
    tree = request_page(sis_username, sis_password)
    teachers = tree.xpath(
        '//div[@class="tab-pane active"]//strong[@class="linkBlack"]/text()')
    return len(teachers) is not 0


def request_grades(username, password, form):
    page = request_page(username, password)
    grade_tuple = get_class(page)
    return grade_tuple


def get_terms(username, password):
    data = {"username": username, "password": password}
    tree = request_page(username, password)
    s = requests.Session()
    r = s.post(url, data=data)
    s.headers = {
        "Accept": "text / html, * / * q = 0.01",
        "Accept-Encoding": "gzip, deflate, sdch, br",
        "Accept-Language": "en - US, en q = 0.8",
        "Connection": "keep-alive",
        "Host": "sisweb.nebo.edu",
        "DNT": "1",
        "Referer": "https://sisweb.nebo.edu/Students/55317",
        'X-Requested-With': 'XMLHttpRequest'
    }
    print(s.options('http://sisweb.nebo.edu/Students/55317/AcademicSummary/ByTerm?trackID=795&termNumber=2').text)
    # print(test.text)
    # print(test.cookies)
    terms = tree.xpath('//div[@class="tab-pane" or @class="tab-pane active"]')
    for term in terms:
        # print(term.xpath('./@data-academic-summary'))
        grades = term.xpath('.//span[@class="academicMark" or not(normalize-space(.))]/text()')
        # grades = term.xpath('.//span[@class="academicMark"]/text()')
        teachers = tree.xpath('.//strong[@class="linkBlack"]/text()')
        # print(grades)
