from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from starlette.requests import Request

from app.routes.gitmusic import templates

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def musicmain(req: Request):
    return templates.TemplateResponse('gitmusic/musicmain.html', {'request': req})

@app.get("/test", response_class=HTMLResponse)
def musicmain(req: Request):
    return templates.TemplateResponse('gitmusic/test.html', {'request': req})



if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', reload=True)