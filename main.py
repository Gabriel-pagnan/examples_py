import uvicorn 
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

#cors aplication
origins = [
    '*',
    'http://127.0.0.1:8000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(routes)

if __name__ == '__main__':
    uvicorn.run('main:app', hostname='127.0.0.1', port=8080)