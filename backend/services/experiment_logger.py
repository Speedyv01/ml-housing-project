import json
from datetime import datetime, timezone
from pathlib import Path

LOGS_DIR = Path("logs")
LOG_FILE = LOGS_DIR / "ab_predictions.jsonl"


def log_prediction(event: dict) -> None:
    """Append one prediction event as a single JSONL line."""
    LOGS_DIR.mkdir(parents=True, exist_ok=True)

    event["timestamp"] = datetime.now(timezone.utc).isoformat()

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(json.dumps(event, ensure_ascii=False) + "\n")


# Format attendu d’un log
if __name__ == "__main__":
    log_prediction(
        {
            "request_id": "test123",
            "user_id": "alice",
            "variant": "B",
            "model_version": "model_v2",
            "prediction": 2.45,
            "latency_ms": 31.2,
        }
    )
    print("Événement enregistré.")
