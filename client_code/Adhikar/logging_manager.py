# ------------------------------------------------------
# Adhikar App — interaction_logger.py
# Lightweight logger for user interactions and usage tracking
# ------------------------------------------------------

import json
import datetime
import os

LOG_FILE = "usage_log.json"


def _load_logs():
  """Load existing logs from file, or return an empty list."""
  if not os.path.exists(LOG_FILE):
    return []

  try:
    with open(LOG_FILE, "r", encoding="utf-8") as f:
      return json.load(f)
  except (json.JSONDecodeError, IOError):
    # Corrupt or empty file — start fresh
    return []


def _save_logs(logs):
  """Save the logs list to the JSON file."""
  try:
    with open(LOG_FILE, "w", encoding="utf-8") as f:
      json.dump(logs, f, ensure_ascii=False, indent=2)
  except Exception as e:
    print(f"[Logger] Error writing to {LOG_FILE}: {e}")


def _timestamp():
  """Return current timestamp in ISO format."""
  return datetime.datetime.now().isoformat()


# ------------------------------------------------------
# Public Logging Functions
# ------------------------------------------------------

def log_page_view(page_name, user_info=None):
  """
    Log when a user views a page in the app.
    Example: log_page_view("home_page", {"state": "Maharashtra"})
    """
  logs = _load_logs()
  logs.append({
    "type": "page_view",
    "page": page_name,
    "timestamp": _timestamp(),
    "user": user_info or {}
  })
  _save_logs(logs)


def log_question(question_text, matched_question=None, user_info=None):
  """
    Log a user-submitted legal question and matched topic (if any).
    Example:
        log_question("What can I do if my salary is delayed?", matched_question="labor rights")
    """
  logs = _load_logs()
  logs.append({
    "type": "question",
    "query": question_text,
    "matched_topic": matched_question,
    "timestamp": _timestamp(),
    "user": user_info or {}
  })
  _save_logs(logs)


def log_answer_served(question_text, answer_text, related_laws=None, schemes=None):
  """
    Log when the AI serves an answer to a user question.
    Example:
        log_answer_served("salary delayed", "You can complain to...", ["Payment of Wages Act"], [])
    """
  logs = _load_logs()
  logs.append({
    "type": "answer",
    "question": question_text,
    "answer": answer_text[:300] + ("..." if len(answer_text) > 300 else ""),  # truncate for brevity
    "related_laws": related_laws or [],
    "schemes": schemes or [],
    "timestamp": _timestamp()
  })
  _save_logs(logs)


def log_event(event_type, data=None):
  """
    Generic logger for custom events.
    Example:
        log_event("language_change", {"from": "en", "to": "hi"})
    """
  logs = _load_logs()
  logs.append({
    "type": event_type,
    "data": data or {},
    "timestamp": _timestamp()
  })
  _save_logs(logs)


# ------------------------------------------------------
# Example usage (for local testing)
# ------------------------------------------------------
if __name__ == "__main__":
  # Simulated user
  user = {"name": "Asha", "state": "Delhi", "language": "hi"}

  log_page_view("home_page", user)
  log_question("What should I do if my employer doesn’t pay my salary?", matched_question="labor")
  log_answer_served(
    "What should I do if my employer doesn’t pay my salary?",
    "You can file a complaint to the Labour Commissioner under the Payment of Wages Act.",
    ["Payment of Wages Act, 1936"],
    ["National Legal Services Authority"]
  )
  print("✅ Logs updated successfully!")
