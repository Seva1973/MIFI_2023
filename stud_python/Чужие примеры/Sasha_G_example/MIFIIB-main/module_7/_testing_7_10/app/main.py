from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root() :
    return {"Привет" : "От Александра"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None) :
    return {"item_id" : item_id, "q" : q}

# The program is launched this way:
# 1. In PyCharm's terminal navigate to _testing_7_10
# 2. Enter: uvicorn app.main:app (here app is the folder with our script)
# 3. Open the browser from the terminal's output i.e.
# Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
# 4. See the result in the browser
