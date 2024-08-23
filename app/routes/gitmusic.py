from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates


gitmusic_router = APIRouter()
templates = Jinja2Templates(directory='views/templates')

@gitmusic_router.get('/', response_class=HTMLResponse)
async def musicmain(req: Request):
    return templates.TemplateResponse('/gitmusic/musicmain.html', {'request': req})


@gitmusic_router.get('/test', response_class=HTMLResponse)
async def test(req: Request):
    return templates.TemplateResponse('/gitmusic/test.html', {'request': req})



