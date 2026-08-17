from fastapi import FastAPI
from app.api import auth, beers, stores, prices, favorites, user

app = FastAPI(
    title="Beer Saver API",
    description="Find the cheapest beer near you — powered by crowdsourced pricing.",
    version="1.0.0"
)

# Register API routes
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(beers.router, prefix="/beers", tags=["beers"])
app.include_router(stores.router, prefix="/stores", tags=["stores"])
app.include_router(prices.router, prefix="/prices", tags=["prices"])
app.include_router(favorites.router, prefix="/favorites", tags=["favorites"])
app.include_router(user.router, prefix="/user", tags=["user"])


@app.get("/")
def root():
    return {"message": "Beer Saver API is running"}
