import subprocess
from fastapi import FastAPI, Request, HTTPException
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

origins = ["*"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/favicon.ico")
async def favicon(request: Request):
    raise HTTPException(status_code=204, detail=None)


@app.get("/")
async def root():
    return {"message": "Hello, World!"}


@app.post("/confluence-webhook")
async def confluence_webhook_handler(request: Request):

    payload = await request.json()

    print(f"Получено уведомление: {payload}")

    if 'repository' not in payload:
        return JSONResponse({"message": "Отсутствует ключ 'repository' в уведомлении"}, status_code=400)

    repo_url = payload["repository"]["cloneUrl"]

    result = subprocess.run(["git", "clone", repo_url], capture_output=True, text=True)

    if result.returncode != 0:
        return JSONResponse({"message": f"Ошибка копирования репозитория: {result.stderr}"}, status_code=500)

    print(f"Пуш успешно обработан: {repo_url}")

    return JSONResponse({"message": "Пуш успешно обработан"}, status_code=200)
