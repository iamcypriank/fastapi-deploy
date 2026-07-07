from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# permision updated
app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Message</title>
        <style>
            body {
                margin: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background: #111;
                color: white;
                font-family: Arial, sans-serif;
            }

            h1 {
                font-size: 4rem;
                color: #ff4d4d;
                text-shadow: 0 0 20px rgba(255, 0, 0, 0.5);
            }
        </style>
    </head>
    <body>
        <h1>Fuck Argentina</h1>
    </body>
    </html>
    """



@app.get("/health")
async def health():
    return {"status": "healthy"}