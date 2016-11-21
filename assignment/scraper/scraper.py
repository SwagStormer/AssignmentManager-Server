import requests
from lxml import html

# WARNING: Do not use the ':' character in SMTP messages
url = "https://sisweb.nebo.edu/Login.aspx"


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
    print(grades)
    # TODO add query to student object to find the users student account
    # TODO pull grades for the specific user
    for indx, element in enumerate(grades):
        if element == "\r\n\t\t\t\t":
            grades[indx] = "No grade"
    teachers = tree.xpath(
        '//div[@class="tab-pane active"]//strong[@class="linkBlack"]/text()')
    return teachers, grades


# Format the output into a long string


def format_grades(t):
    formatted_grades = []
    grade_string = ""
    for index, element in enumerate(t[0]):
        formatted_grades.append(t[0][index] + "- " + t[1][index] + "\n")
    for element in formatted_grades:
        grade_string += element

    return grade_string


def request_grades(username, password, form):
    page = request_page(username, password)
    grade_tuple = get_class(page)
    if form:
        return format_grades(grade_tuple)
    else:
        return grade_tuple
