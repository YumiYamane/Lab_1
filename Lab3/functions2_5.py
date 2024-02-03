def cat_avg_imdb(movies, category):
    sublist=[]

    for movie in movies:
        if movie["category"]==category:
            sublist.append(movie)

    sum=0
    total=len(sublist)

    for movie in sublist:
        sum=sum+movie["imdb"]
        avg_score=sum/total

    return avg_score