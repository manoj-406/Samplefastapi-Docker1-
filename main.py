"""This module contains main files
"""
from fastapi import FastAPI
from datetime import date
from api.model import Movierequest, Movieresponse

app = FastAPI()

@app.get("/movie", response_model=list[Movieresponse])
def get_movies():
    """This Function Gets the Movieresponse
    """
    movies = []
    movies.append(
        Movieresponse(
            id="01",
            movie_title= "RRR",
            Director= "SS.Rajamouli",
            Release_date= date.today()
        )
    )
    return movies

@app.post("/movie", response_model=Movieresponse)
def requested_movie(request: Movierequest):
    """This Function Returns Movierequest
    """
    return Movieresponse(
        id="01",
        movie_title=request.movie_title,
        Director=request.Director,
        Release_date=request.Release_date

    )