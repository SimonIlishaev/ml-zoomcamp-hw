import numpy as np
from io import BytesIO
from urllib import request
from PIL import Image
import tflite_runtime.interpreter as tflite

# url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Smaug_par_David_Demaret.jpg/1280px-Smaug_par_David_Demaret.jpg'
# url = 'https://upload.wikimedia.org/wikipedia/en/e/e9/GodzillaEncounterModel.jpg'
# interpreter = tflite.Interpreter(model_path="dino_dragon.tflite")
interpreter = tflite.Interpreter(model_path="dino-vs-dragon-v2.tflite")
interpreter.allocate_tensors()
input_index = interpreter.get_input_details()[0]["index"]
output_index = interpreter.get_output_details()[0]["index"]

def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img


def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img

def predict(url):
    img = download_image(url)
    img = prepare_image(img, (150, 150))
    x = np.array(img, dtype="float32")
    X = np.array([x])/255
    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)

    return preds[0].tolist()

def lambda_handler(event, context): ## in case of yandex cloud functions it's hust "handler"
    url = event["url"]
    prediction = predict(url)

    return {"predicted_proba": prediction}



