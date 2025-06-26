from bs4 import BeautifulSoup

with open("/Users/rmn7591/Documents/Repositories/-30DaysOfPython/season3/WebScraping/read_file.html", "r") as file:
    content = file.read()

    soup = BeautifulSoup(content, 'lxml')
    course_cards = soup.find_all('div', class_ = 'card')
    for courses in course_cards:
       course_name = courses.h5.text
       courses_price = courses.a.text.split()[-1]
       print(f'{course_name} costs {courses_price}')
