# End-To-End-Chest-Cancer-Classification-With-MLFLOW-DVC





## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml





## MLflow

- [Documentation](https://mlflow.org/docs/latest/index.html)

- [MLflow tutorial](https://youtube.com/playlist?list=PLkz_y24mlSJZrqiZ4_cLUiP0CBN5wFmTb&si=zEp_C8zLHt1DzWKK)

##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/poudelsagar725/End-To-End-Chest-Cancer-Classification.mlflow \
MLFLOW_TRACKING_USERNAME=poudelsagar725 \
MLFLOW_TRACKING_PASSWORD=79f162a063eb628389f24d126c5fceabd5ac4cf5 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/poudelsagar725/End-To-End-Chest-Cancer-Classification.mlflow

export MLFLOW_TRACKING_USERNAME= poudelsagar725

export MLFLOW_TRACKING_PASSWORD=79f162a063eb628389f24d126c5fceabd5ac4cf5

```



### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag


## About MLflow & DVC

MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & taging your model


DVC 

 - Its very lite weight for POC only
 - lite weight expriements tracker
 - It can perform Orchestration (Creating Pipelines)



# CANCERR    
