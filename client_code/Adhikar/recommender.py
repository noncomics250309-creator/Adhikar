import json
import difflib

# ------------------------------------------------------
# Adhikar App — Recommender System for Schemes & Laws
# ------------------------------------------------------

def load_json(file_path):
  """
    Safely load and return JSON data from file.
    Returns an empty list if file not found or malformed.
    """
  try:
    with open(file_path, "r", encoding="utf-8") as f:
      return json.load(f)
  except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"[Error] Could not load {file_path}: {e}")
    return []


def fuzzy_match_score(a, b):
  """Return fuzzy match ratio between two strings."""
  return difflib.SequenceMatcher(None, a.lower(), b.lower()).ratio()


def match_relevance(demographics, item):
  """
    Compute a simple relevance score based on demographic data
    (gender, occupation, state, age) and keywords in the scheme/law.
    """
  score = 0
  user_keywords = []

  # Collect demographic keywords
  for key, val in demographics.items():
    if isinstance(val, str):
      user_keywords.append(val.lower())

    # Match categories, target groups, or keywords
  for kw in item.get("keywords", []):
    for user_kw in user_keywords:
      if user_kw in kw.lower() or kw.lower() in user_kw:
        score += 1

    # Boost score if gender- or occupation-specific
  if demographics.get("gender", "").lower() in str(item.get("target_group", "")).lower():
    score += 2
  if demographics.get("occupation", "").lower() in str(item.get("target_group", "")).lower():
    score += 2

    # Slightly boost if the state matches
  if demographics.get("state", "").lower() in str(item.get("applicable_states", [])).lower():
    score += 1

  return score


def recommend_items(user_data, topic, schemes_file="schemes.json", laws_file="laws.json", top_n=5):
  """
    Main function: Suggest relevant welfare schemes and laws
    based on user demographics and the topic of the query.
    """
  schemes = load_json(schemes_file)
  laws = load_json(laws_file)

  if not schemes or not laws:
    return {
      "status": "error",
      "message": "Unable to load schemes or laws data."
    }

    # Step 1: Calculate scheme relevance
  scheme_scores = []
  for s in schemes:
    score = match_relevance(user_data, s)
    score += fuzzy_match_score(topic, s.get("category", "")) * 2  # boost category relevance
    score += fuzzy_match_score(topic, s.get("description", ""))   # partial text match
    if score > 0:
      scheme_scores.append((s, score))

    # Step 2: Calculate law relevance
  law_scores = []
  for l in laws:
    score = fuzzy_match_score(topic, l.get("category", "")) * 2
    score += fuzzy_match_score(topic, l.get("summary", ""))
    if score > 0:
      law_scores.append((l, score))

    # Step 3: Sort and select top results
  scheme_scores.sort(key=lambda x: x[1], reverse=True)
  law_scores.sort(key=lambda x: x[1], reverse=True)

  top_schemes = [s[0] for s in scheme_scores[:top_n]]
  top_laws = [l[0] for l in law_scores[:top_n]]

  return {
    "status": "success",
    "topic": topic,
    "recommended_schemes": top_schemes,
    "recommended_laws": top_laws
  }


  # ------------------------------------------------------
  # Example CLI usage (for local testing)
  # ------------------------------------------------------
  if __name__ == "__main__":
    # Example demographic profile
    user_demo = {
      "name": "Priya Sharma",
      "age": 29,
      "gender": "Female",
      "state": "Maharashtra",
      "occupation": "Teacher",
      "language": "Hindi"
    }

    topic = "women safety and domestic violence"

result = recommend_items(user_demo, topic)

if result["status"] == "success":
  print("\n🏛️ Recommended Welfare Schemes:")
  for s in result["recommended_schemes"]:
    print(f" - {s.get('name')} ({s.get('category')})")
    print(f"   👉 {s.get('url', 'N/A')}")

  print("\n📘 Relevant Laws:")
  for l in result["recommended_laws"]:
    print(f" - {l.get('name')}")
    print(f"   ⚖️ {l.get('category')} | {l.get('url', 'N/A')}")
else:
  print("Error:", result["message"])
