"""
General information about the deployment
"""

title = "Image API for cleaning blackboard pictures"

description = """
# API deployment of service of blackboard image to a clean B/W

## Test the API
* Send the image and receive back a clean image
* Use the API of sending in **JSON as an array** the image to clean
"""
version = "0.0.1"
contact = {
    "name": "Camilo Cáceres",
    "url": "https://camilo-cf.github.io/",
    "email": "camilo.caceresf@gmail.com",
}
license_info = {
    "name": "Apache 2.0",
    "url": "https://www.apache.org/licenses/LICENSE-2.0.html"
}
tags_metadata = [
    {
        "name": "improve_image",
        "description": "Improve the blackboard image after crop its borders",
    }
]
