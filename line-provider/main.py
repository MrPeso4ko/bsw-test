import uvicorn

from app import App
from config import settings

app = App()

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=settings.run.port)