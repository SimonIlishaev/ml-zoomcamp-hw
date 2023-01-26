# Simple scoring deployment
## [MLZoomcamp](https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp) project

Simple example of training scoring model with service deployment.

Create conda environment with dependencies by

```zsh
conda env create -n ENVNAME --file environment.yml
```

train the best model with 

```zsh
python train.py
```

Model was deployed with bentoml

run service locally with

```zsh
bentoml serve service.py:rf --production
```

and test it with a 

```zsh
python test.py
```

(run it in another terminal, while log of test will be shown in terminal with running service)

It will return class label "1".

Containerization also completed with bentoml.

Run 

```zsh
bentoml build
```

Check model tag

```zsh
bentoml list
```

Create container (assumed that docker installed):

```zsh
bentoml containerize <scoring_model>:<YOUR TAG>
```

Run container locally:

```zsh
docker run -it --rm -p 3000:3000 scoring_model:<YOUR TAG>
```