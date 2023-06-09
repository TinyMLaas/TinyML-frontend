import json
import requests

from config import BACKEND_URL


def compile_model(data: dict):
    """Sends request to backend for compilation. The request uses the model id.
    """
    model_id = data["model_id"]

    response = requests.post(
        f"{BACKEND_URL}/compiled_models/models/{model_id}",
        json=data,
        timeout=(5, None)
        )

    if response.status_code == 201:
        return json.loads(response.text)

    return None


def get_compiled_models():
    """Receives a list of all compiled models.
    """
    response = requests.get(f"{BACKEND_URL}/compiled_models/", timeout=5)

    if response.status_code == 200:
        return json.loads(response.text)

    return None
