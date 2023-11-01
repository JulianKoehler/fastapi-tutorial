from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .router import posts, users, auth, votes


# models.Base.metadata.create_all(bind=engine) # NOT NEEDED WITH ALEMBIC
app = FastAPI()

origins = [
    "http://localhost",
    'https://www.google.com'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(votes.router)


@app.get("/")
def root():
    return {"message": "This is the root route. Feel free and use the according endpoints of this API! For instance /posts to retrieve all posts."}
