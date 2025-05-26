# Kidney-Disease-Classification

## Workflows

1. Update `config.yaml`
2. Update `secrets.yaml` [Optional]
3. Update `params.yaml`
4. Update the entity
5. Update the configuration manager in `src/config`
6. Update the components
7. Update the pipeline 
8. Update `main.py`
9. Update `dvc.yaml`
10. `app.py`

---

## How to run?

### STEPS:

**STEP 01 - Create a conda environment after opening the repository**

```bash
conda create -n env_name python=3.12 -y
conda activate env_name
```

**STEP 02 - Install the requirements**

```bash
pip install -r requirements.txt
```

**Run the application**

```bash
python app.py
```

Now, open up your localhost and port in your browser.

---

## MLflow

- [Documentation](https://mlflow.org/docs/latest/index.html)
- [MLflow tutorial](https://youtu.be/qdcHHrsXA48?si=bD5vDS60akNphkem)

**Command to start MLflow UI:**

```bash
mlflow ui
```

### Dagshub

[Dagshub](https://dagshub.com/)

These are the environment variables you need to setup in your .env file:

```bash
MLFLOW_TRACKING_URI=
MLFLOW_TRACKING_USERNAME=
MLFLOW_TRACKING_PASSWORD=
python script.py
```

To export as environment variables:

```bash
export MLFLOW_TRACKING_URI=
export MLFLOW_TRACKING_USERNAME=
export MLFLOW_TRACKING_PASSWORD=
```

---

### DVC Commands

1. `dvc init`
2. `dvc repro`
3. `dvc dag`

---

## About MLflow & DVC

**MLflow**
- Production grade
- Trace all of your experiments
- Logging & tagging your model

**DVC**
- Lightweight, suitable for POC only
- Lightweight experiments tracker
- Can perform orchestration (creating pipelines)

---
