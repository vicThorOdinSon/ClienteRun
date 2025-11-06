import requests
import pandas as pd

from config import API_BASE_URL

def get_runs(limit=1000, cursor=None, query=None):
    """Obtiene registros desde la API /api/runs con paginación y filtro."""
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    if query:
        params["q"] = query
    r = requests.get(API_BASE_URL, params=params, timeout=20)
    r.raise_for_status()
    data = r.json()
    df = pd.DataFrame(data.get("data", []))
    return df, data.get("nextCursor"), data.get("total")
