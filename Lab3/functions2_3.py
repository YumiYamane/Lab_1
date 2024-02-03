def category_movies(movies, category):
    sublist=[]

    for movie in movies:
        if movie["category"]==category:
            sublist.append(movie)
    
    return sublist