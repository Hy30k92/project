from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from starlette.requests import Request

from app.routes.gitmusic import templates

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def join(req: Request):
    return templates.TemplateResponse('index.html', {'request': req})



if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', reload=True)