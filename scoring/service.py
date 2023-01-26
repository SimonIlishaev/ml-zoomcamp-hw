import numpy as np
import bentoml
from bentoml.io import NumpyNdarray

rf_runner = bentoml.sklearn.get("scoring_model:latest").to_runner()

rf = bentoml.Service("scoring_model", runners=[rf_runner])

@rf.api(input=NumpyNdarray(), output=NumpyNdarray())
def predict(sample_data: np.ndarray) -> np.ndarray:
    prediction = rf_runner.predict.run(sample_data)
    print(prediction)

    return prediction