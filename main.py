import random
from fastapi import FastAPI

app = FastAPI()

quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Talk is cheap. Show me the code. - Linus Torvalds",
    "Programs must be written for people to read, and only incidentally for machines to execute. - Harold Abelson",
    "Premature optimization is the root of all evil. - Donald Knuth",
    "First, solve the problem. Then, write the code. - John Johnson"
]

@app.get("/")
def read_root():
    return {"message": "Quote API is running! /quote to get inspired."}

@app.get("/quote")
def get_quote():
    return {"quote": random.choice(quotes)}
