import time

import numpy as np
import openai

openai.api_key = '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'

def Image_Genrate(Text):
  response = openai.Image.create(
    prompt=Text,
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  print(image_url)

  from PIL import Image
  import requests
  from io import BytesIO

  # Download the image
  response = requests.get(image_url)
  image = Image.open(BytesIO(response.content))

  # save the image
  image.save('temp.png')

  import cv2
  cv2_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)



0
  initial_time = time.time()
  cv2.imshow("Image", cv2_image)
  cv2.waitKey(3000)



while True:
  Text = input("Text: ")
  if(Text == ""):
    Image_Genrate("Arts")
  else:
    Image_Genrate(Text)