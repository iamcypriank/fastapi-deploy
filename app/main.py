from fastapi import FastAPI


# permision updated
app = FastAPI()


@app.get("/")
async def root():
    return {
        "message" : "Hello from FastAPI! elastic beanstalk"
    }

@app.get("/health")
async def health():
    return {"status": "healthy"}