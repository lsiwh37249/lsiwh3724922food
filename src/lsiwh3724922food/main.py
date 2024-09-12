from typing import Union
from fastapi import FastAPI
import pickle
import time

app =FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "world"}

@app.get("/food")
def food(name : str):
    # 시간을 구함
    # 음식 이름과 시간을 csv로 저장 -> /code/data/food.csv
    my_time = time.strftime("%Y-%m-%d %H:%M:%S")
    #"2024-09-14 11:12:13" 
    return {"food" : name, "time" : f"{my_time}"}
