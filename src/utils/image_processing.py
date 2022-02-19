"""
    Image processing functions.
"""
from io import BytesIO
from numpy import asarray
from numpy import ndarray
from PIL import Image
from skimage.exposure import equalize_adapthist
from skimage.exposure import rescale_intensity
from skimage.filters import threshold_local
# from skimage.restoration import denoise_bilateral

from src.utils.constants import BLOCK_SIZE


class ImageProcessing:
    def execute(self, image) -> ndarray:
        """
        Execute the image processing.

        Args:
            image_path: Path of the image to process.
        """
        image = self.read_imagefile(image)
        image = self.denoise(image)
        image = self.image_to_bytes(image)
        return image

    def read_imagefile(self, file) -> Image.Image:
        """
        Read the image file.

        Args:
            file: Image file to read.

        Returns:
            Image.
        """
        image = Image.open(BytesIO(file))
        image = asarray(image.resize((image.width, image.height)).convert("L"))
        return image

    def denoise(self, image: ndarray) -> ndarray:
        """
        Denoise the image.

        Args:
            image: Image to denoise.

        Returns:
            Denoised image.
        """
        # Apply adaptive histogram equalization to improve the contrast along
        # the image
        proccessed_image = equalize_adapthist(image)
        # Intensity rescaling to improve the contrast
        proccessed_image = rescale_intensity(
            proccessed_image, out_range=(0, 255))
        # Invert the image to white background
        proccessed_image = (proccessed_image - 255) * -1
        # Find the threshold value
        local_thresh = threshold_local(proccessed_image, BLOCK_SIZE, offset=35)
        # Apply local thresholding and obtain the binary image
        proccessed_image = proccessed_image > local_thresh
        # proccessed_image = denoise_bilateral(
        #     proccessed_image,
        #     sigma_color=0.4,
        #     sigma_spatial=5,
        #     multichannel=False,
        #     channel_axis=-1,
        # )
        return proccessed_image

    def image_to_bytes(self, image: ndarray) -> ndarray:
        """
        Convert image to bytes.

        Args:
            image: Image to convert.

        Returns:
            Image as bytes.
        """
        pil_image = Image.fromarray((image * 255).astype("uint8"), mode="L")
        buf = BytesIO()
        pil_image.save(buf, format="JPEG")
        return buf.getvalue()


if __name__ == "__main__":
    processing = ImageProcessing()
    image = processing.execute("data/raw/test.jpg")
    b_image = Image.open(BytesIO(image))
    # from skimage.io import imsave
    # b_image.save("savepath.jpeg")
    # assert type(image) == ndarray
