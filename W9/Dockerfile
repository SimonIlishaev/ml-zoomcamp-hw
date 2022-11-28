FROM svizor42/zoomcamp-dino-dragon-lambda:v2

RUN pip install https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.7.0-cp39-cp39-linux_x86_64.whl
RUN pip install Pillow

COPY my_function.py .

CMD ["my_function.lambda_handler"]