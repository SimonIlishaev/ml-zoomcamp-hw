import numpy as np
import bentoml
from bentoml.io import NumpyNdarray

model_ref = bentoml.sklearn.get("sentiment_model:latest")
vectorizer = model_ref.custom_objects["vectorizer"]

model_runner = model_ref.to_runner()
xgbc = bentoml.Service("sentiment_classifier", runners=[model_runner])

@xgbc.api(input=NumpyNdarray(), output=NumpyNdarray())
async def predict(text):
    vector = vectorizer.transform(text)
    prediction = await model_runner.predict.async_run(vector)
    print(prediction)

    return prediction
