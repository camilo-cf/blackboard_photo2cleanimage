from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.responses import Response

from src.utils import info as I
from src.utils import constants as K
from src.utils.image_processing import ImageProcessing
from src.utils.schema import OutputImage

app = FastAPI(
    title=I.TITLE,
    description=I.DESCRIPTION,
    version=I.VERSION,
    contact=I.CONTACT,
    license_info=I.LICENSE_INFO,
    openapi_tags=I.TAGS_METADATA,
)

@app.post(
    "/improve_image",
    response_model=OutputImage,
    tags=["improve_image"],
    description="Improve the blackboard image after crop its borders",
)
async def improve_image(
    file: UploadFile = File(
        ..., media_type="multipart/form-data", description="Image to improve in jpg, jpeg or png format" 
    )
):
    try:
        assert (file.filename.split(".")[-1] in K.IMAGE_FORMATS) == True
        processing = ImageProcessing()
        return Response(
            content=processing.execute(await file.read()), media_type="image/jpeg"
        )

    except BaseException as e:
        raise HTTPException(
            status_code=404, detail="Image must be jpg or png format!"
        ) from e
