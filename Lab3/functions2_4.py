def avg_imdb_score(movies):
    sum=0
    total=len(movies)

    for movie in movies:
        sum=sum+movie["imdb"]
        avg_score=sum/total

    return avg_score