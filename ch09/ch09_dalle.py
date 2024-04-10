import io
from PIL import Image
import base64

# 이미지 프롬프트를 입력받으면 이미지를 생성하여 전달.
def get_image_by_dalle(client, img_prompt):    
    response = client.images.generate(
    model="dall-e-3",
    prompt=img_prompt,
    size="1024x1024",
    quality="standard",
    n=1,
    response_format='b64_json'
    )

    image_data = base64.b64decode(response.data[0].b64_json)
    image = Image.open(io.BytesIO(image_data))
    return image