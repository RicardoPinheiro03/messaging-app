from fastapi import FastAPI
from app.routers import user, message, session
from app.database import Base, engine

# Initialize the database
Base.metadata.create_all(bind=engine)

# Create the FastAPI instance
app = FastAPI()

# Include the routers
app.include_router(user.router, prefix="/user", tags=["user"])
app.include_router(message.router, prefix="/message", tags=["message"])
app.include_router(session.router, prefix="/session", tags=["session"])