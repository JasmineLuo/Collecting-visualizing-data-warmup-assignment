#!/usr/bin/python
# coding: UTF-8

from urllib2 import Request, urlopen
from time import sleep
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

headers = {
  'Accept': 'application/json'
}

pagenum=1
count=1

textdir='/Users/luozhongyi/Desktop/2016Spring/CSE6242/hw1/​movie_ID_name.txt'
text_file = open(textdir, 'w')

while count<=300:
	var=str(pagenum)
	restr = 'http://api.themoviedb.org/3/genre/878/movies?api_key=e2d6910f279ae4690be5a7ace2ce08bc&page='+var+'&include_all_movies=true&include_adult=true'

	request=Request(restr,headers=headers)
	response_body = urlopen(request).read()
	'''print response_body'''
	data = json.loads(response_body)

	length=len(data['results'])

	for i in range(0,length):
		result1=data['results'][i]
		ID=result1['id']
		name=result1['original_title']
		if count>300:
			break

		if result1['release_date']>='2000-01-01':
			temp=str(ID) + ', ' + name
			text_file.write("%s" % temp)
			text_file.write("\n")
			count=count+1
		else:
			print 'excluded'
			print result1['release_date']
	pagenum=pagenum+1
	sleep(0.25)
	print 'nextpage:'

text_file.close()