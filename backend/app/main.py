from fastapi import FastAPI

app = FastAPI(title="SubTrack API")

@app.get("/")
def health_check():
    return {"status": "ok", "message": "SubTrack API is running"}