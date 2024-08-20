from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates


gitmusic_router = APIRouter()
templates = Jinja2Templates(directory='views/templates')

@gitmusic_router.get('/', response_class=HTMLResponse)
async def musicmain(req: Request):
    return templates.TemplateResponse('index.html', {'request': req})



