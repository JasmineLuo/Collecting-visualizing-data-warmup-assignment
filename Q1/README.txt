Programming language is python;
Platform: Mac OS X 10.10.5

The starter.py is for question b:  In which textdir should be changed to your text own txt file.
The starterb.py is for question c: In which textname should be changed to your movie_ID_name.txt
									and textname2 should be changed to your destination txt file.
									
The api key is:  e2d6910f279ae4690be5a7ace2ce08bc
Other parameter include: 
		page (to turn pages in order to fetch 300 items);
		include_all_movies=true;
		include_adult=true;

		For question b, query is:
		http://api.themoviedb.org/3/genre/878/movies?api_key=e2d6910f279ae4690be5a7ace2ce08bc&page='+XXX+'&include_all_movies=true&include_adult=true
		For question c, query is:
		http://api.themoviedb.org/3/movie/'+XXX+'/similar?api_key=e2d6910f279ae4690be5a7ace2ce08bc&include_all_movies=true&include_adult=true
