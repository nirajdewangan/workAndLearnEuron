from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def test():
    return {"message": "Hello , world!"}


@app.get("/again")
def test2():
    return {"message": "Hello again, from test2!"}


@app.get("/test3")
def test3(a:int, b:int):
    return {"message": f"Hello from test3 a={a} and b={b}"}