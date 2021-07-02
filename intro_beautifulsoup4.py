# webscraping beginner guide with beautiful soup 4
"""
from bs4 import BeaufifulSoup

with open('home.html', 'r') as html_file:
	content = html_file.read()
	# print(content)

	soup = BeaufifulSoup(content, 'lxml')
	# print(soup.prettify())

	tags = soup.find('h5')   # to search firtst h5 tag content
	course_html_stags = soup.find_all('h5')  # to seach all h5 tag content
	# print(tags)

	for course in course_html_tags:
		print(course.text)

	course_cards = soup.find_all('div', class_='card') # <div class ="card">...</div>
	for course in course_cards:
		course_name = course.h5.text  # <h5>Python for beginners</h5>
		course_price = course.a.text.split()[-1]  # <a> Start for 20$ </a>

		print(f'{course_name} is priced {course_price}')
"""

# webscraping a real website

from bs4 import BeaufifulSoup
import requests
import time

def find_jobs():
	html_text = requests.get("HERE GOES THE URL").text
	soup = BeaufifulSoup(html_text, 'lxml')

	jobs = soup.find_all('li', class_ ='li tag class name')
	for index, job in enumerae(jobs):
		published_date = job.find('span', class_='span class name').span.text
		if 'few' in published_date:   # for only to show few days ago post
			company_name.find('h3', class_='h3 class name').text.replace(' ', '')   # to remove the space
			skills = job.fing('span', class_='span class name').text.replace(' ', '')
			more_info = job.header.h2.a['href']

			with open(f'posts/{index}.txt', 'w') as file:
				file.write(f'Company Name: {company_name.strip()} \n')
				file.write(f'Required Skills: {skills.strip()}\n')
				file.write(f'More Info: {more_info}\n')
			print(f'file saved {index}')

if __name__ == '__main__':   # for import purpose 
	while True:   # to run code every certian minutes
		find_jobs()
		time_wait = 10
		print(f'Waiting {time_wait} minutes...')
		time.sleep(time_wait * 60)



