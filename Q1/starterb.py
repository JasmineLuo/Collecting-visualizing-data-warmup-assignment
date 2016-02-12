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

listofpair=[] # to store the result of pairs, incase of delete
textname='/Users/luozhongyi/Desktop/2016Spring/CSE6242/hw1/​movie_ID_name.txt'
text_file=open(textname)

strn=text_file.readlines()
total=len(strn)
text_file.close()

y=1

for x in strn:
	#x=strn[y]
	end=x.index(',')
	curID=int(x[0:end])
	var=str(curID)
	restr='http://api.themoviedb.org/3/movie/'+var+'/similar?api_key=e2d6910f279ae4690be5a7ace2ce08bc&include_all_movies=true&include_adult=true'
	request=Request(restr,headers=headers)
	response_body = urlopen(request).read()
	'''print response_body'''
	data = json.loads(response_body)
	length=len(data['results'])

	for i in range(0,min(5,length)):
		relID=data['results'][i]['id'] # type is int
		test =[relID, curID]
		if test in listofpair:
		   ind=listofpair.index(test)
		   if relID>curID:
		   	  del listofpair[ind]
		   	  listofpair.append([curID,relID]) # change the former one
		   	  print str(ind) + ' ' + str(relID)
		   else:
		   	   pass # do nothing to preserve the former one
		else:
			listofpair.append([curID,relID])

	sleep(0.25)
	print 'Processed ' + str(y) +'th item'
	y=y+1

print listofpair

## write into txt file:

textname2='/Users/luozhongyi/Desktop/2016Spring/CSE6242/hw1/movie_ID_sim_movie_ID.txt'
text_file2=open(textname2,'w')
#total=length(listofpair)

for k in listofpair:
	temp=str(k[0]) + ',' + str(k[1])
	text_file2.write("%s" % temp)
	text_file2.write("\n")
