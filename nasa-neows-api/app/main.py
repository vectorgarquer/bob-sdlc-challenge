from fastapi import FastAPI

from app.routers import asteroids, watchlist

app = FastAPI(
    title="NASA NeoWs API",
    description=(
        "REST API to query Near-Earth Objects using the NASA NeoWs feed. "
        "Supports date-range queries, sorting, danger ranking, and an in-memory watchlist."
    ),
    version="1.0.0",
)

app.include_router(asteroids.router)
app.include_router(watchlist.router)


@app.get("/health", tags=["Health"])
def health():
    return {"status": "ok"}
