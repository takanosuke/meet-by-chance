import json
from typing import Optional
from fastapi import FastAPI, Query
from fastapi.staticfiles import StaticFiles
from image import Image

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/image/create")
async def read_items(
    q: Optional[str] = Query(
        None,
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/image/create")
def create_image(
    density: int = 50,
    visibility: int = 50,
    color: int = 50,
    blurry: int = 50,
    shift: int = 50,
    frame: str = 50,
):
    params = {
        "density": density,
        "visibility": visibility,
        "color": color,
        "blurry": blurry,
        "shift": shift,
        "frame": frame,
    }
    img_name = Image().create(params)
    img_url = request._current_scheme_host + settings.MEDIA_URL + "results/" + img_name
    return json.dumps({"url": img_url, "name": img_name})
