#we need to ensure this test can run in order to determine the upload compoenent will accept all the different file types

import numpy as np
from PIL import Image
from paddleocr import PaddleOCR

filename = "/Users/matthewsimon/Downloads/21.jpg"
img = np.array(Image.open(filename))
ocr = PaddleOCR(lang="en", use_gpu=False, show_log=False)
result = ocr.ocr(img=img)
