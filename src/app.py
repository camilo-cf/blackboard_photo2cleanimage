from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.responses import Response

from src.utils import info as I
from src.utils import constants as K
from src.utils.image_processing import ImageProcessing

# TODO: Schema from libs.schema import Iris, IrisPredictionResponse


app = FastAPI(
    title=I.title,
    description=I.description,
    version=I.version,
    contact=I.contact,
    license_info=I.license_info,
    openapi_tags=I.tags_metadata,
)


@app.post(
    "/improve_image",
    #   TODO: Define response_model=IrisPredictionResponse,
    tags=["improve_image"],
    description="Improve the blackboard image after crop its borders",
)
async def improve_image(file: UploadFile = File(...)):
    try:
        assert (file.filename.split(".")[-1] in K.IMAGE_FORMATS) == True
        processing = ImageProcessing()
        return Response(
            content=processing.execute(await file.read()), media_type="image/jpeg"
        )

    except BaseException:
        raise HTTPException(status_code=404,
                            detail="Image must be jpg or png format!")
