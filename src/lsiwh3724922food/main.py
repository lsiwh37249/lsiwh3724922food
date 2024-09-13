from typing import Union
from fastapi import FastAPI
import pickle
import time
import os
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

app =FastAPI()

origins = [
#    "http://localhost.tiangolo.com",
#    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8899",
    "http://ec2-43-203-204-195.ap-northeast-2.compute.amazonaws.com",
    "http://ec2-43-203-204-195.ap-northeast-2.compute.amazonaws.com/n22/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_path():
    file_dir = __file__
    dir = os.path.dirname(file_dir)
    return dir

@app.get("/")
def read_root():
    print()
    return {"Hello": "world"}

@app.get("/food")
def food(name : str):
    # 시간을 구함
    # 음식 이름과 시간을 csv로 저장 -> /code/data/food.csv
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S")
    new_data = f"food : {name}, time : {formatted_time}"
    
    f_csv = os.path.join(get_path(), "code", "data")

    if not os.path.exists(f_csv):
        os.makedirs(f_csv)
    #csv 파일 경로 설정
    csv_file_path = os.path.join(f_csv, "food.csv")

    # f_csv 폴더에 food.csv 파일이 없다면 생성 있다면 데이터를 추가
    if not os.path.exists(csv_file_path):
        df = pd.DataFrame(columns=["food", "time"])
    else:
        df = pd.read_csv(csv_file_path)

    # 새 데이터 추가
    new_data = pd.DataFrame([[name, formatted_time]], columns=["food", "time"])
    df = pd.concat([df, new_data], ignore_index=True)

    # CSV 파일 저장
    df.to_csv(csv_file_path, index=False)

    
    return {"food" : name, "time" : f"{formatted_time}"}
