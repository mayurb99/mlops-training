
import pickle
from flask import Flask, request, jsonify
import mlflow
from mlflow.tracking import MlflowClient
import os



RUN_ID = 'f73ca9cde66045499464239e2e71cb98'
MLFLOW_TRACKING_URI = 'http://127.0.0.1:5000'
mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
client = MlflowClient(tracking_uri=MLFLOW_TRACKING_URI)

logged_model = f'runs:/{RUN_ID}/model'

# Load model as a PyFuncModel.
model = mlflow.pyfunc.load_model(logged_model)

path = client.download_artifacts(run_id=RUN_ID, path='dict_vectorizer.bin')

print(f"downloading vectorizer to {path}")

with open(path, 'rb') as f_in:
    dv=pickle.load(f_in)

def prepare_features(ride):
    features = {}
    features['PU_DO'] = '%s_%s' % (ride['PULocationID'], ride['DOLocationID'])
    features['trip_distance'] = ride['trip_distance']
    return features

def predict(features):
    X = dv.transform(features)
    preds=model.predict(X)
    return preds[0]

app = Flask('duration-prediction')


@app.route('/predict', methods=['POST'])
def predict_endpoint():
    ride = request.get_json()

    features = prepare_features(ride)
    pred = predict(features)
    result = {
        'duration': pred,
        'model_version': RUN_ID
    }

    return jsonify(result)
    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
