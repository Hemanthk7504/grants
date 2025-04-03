from fastapi import FastAPI


app = FastAPI()


@app.post("/akash")
def home():
    return True



