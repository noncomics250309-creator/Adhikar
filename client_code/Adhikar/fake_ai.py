import time
import json
import difflib
import random

# ------------------------------------------------------
# Fake AI Engine for Adhikar — AI-powered legal literacy
# ------------------------------------------------------

def load_json(file_path):
  """
    Load JSON data safely from the given file path.
    Returns an empty list if file not found or malformed.
    """
  try:
    with open(file_path, "r", encoding="utf-8") as f:
      return json.load(f)
  except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"[Error] Could not load {file_path}: {e}")
    return []


def fuzzy_match(query, questions, threshold=0.6):
  """
    Perform fuzzy string matching to find the closest question match.
    Returns (best_match_dict, match_score) or (None, 0).
    """
  best_match = None
  best_score = 0

  for q in questions:
    text = q.get("question", "")
    ratio = difflib.SequenceMatcher(None, query.lower(), text.lower()).ratio()

    # Boost if query contains keywords
    if any(k.lower() in query.lower() for k in q.get("keywords", [])):
      ratio += 0.1

    if ratio > best_score:
      best_score = ratio
      best_match = q

  return (best_match, best_score) if best_score >= threshold else (None, 0)


def get_answer_by_question_id(answers, qid):
  """
    Retrieve the answer entry corresponding to the given question_id.
    """
  for ans in answers:
    if str(ans.get("question_id")) == str(qid):
      return ans
  return None


  def simulate_typing_delay(text, min_delay=0.02, max_delay=0.05):
    """
    Simulate an AI 'typing' delay for realism.
    """
    for char in text:
      print(char, end='', flush=True)
      time.sleep(random.uniform(min_delay, max_delay))
    print()  # newline


    def get_ai_response(user_query, questions_file="questions.json", answers_file="answers.json"):
      """
    Main function: Takes a user's query, searches for the best match,
    retrieves the corresponding answer, and returns a structured response.
    """
      questions = load_json(questions_file)
      answers = load_json(answers_file)

      if not questions or not answers:
        return {
          "status": "error",
          "message": "Sorry, I couldn’t load the knowledge base."
        }

      # Fuzzy match the query to a known question
      match, score = fuzzy_match(user_query, questions)

      if not match:
        fallback_message = "Sorry, I don’t have an answer yet, but I’ll keep learning!"
        simulate_typing_delay(fallback_message)
        return {
          "status": "not_found",
          "query": user_query,
          "message": fallback_message,
          "links": [],
          "laws": [],
          "schemes": []
        }

      # Retrieve corresponding answer
      ans = get_answer_by_question_id(answers, match.get("id"))
      if not ans:
        fallback_message = "Sorry, I found a related topic, but no detailed answer yet."
        simulate_typing_delay(fallback_message)
        return {
          "status": "partial",
          "query": user_query,
          "matched_question": match.get("question"),
          "message": fallback_message,
          "links": [],
          "laws": [],
          "schemes": []
        }

      # Combine and simulate AI typing
      response_text = ans.get("answer", "Sorry, no detailed answer available.")
      simulate_typing_delay("🤖 Adhikar is thinking...")
      time.sleep(random.uniform(0.5, 1.5))
      simulate_typing_delay(response_text)

      return {
        "status": "success",
        "query": user_query,
        "matched_question": match.get("question"),
        "category": match.get("category"),
        "answer": response_text,
        "laws": ans.get("related_laws", []),
        "links": ans.get("links", []),
        "schemes": ans.get("schemes", [])
      }


    # ------------------------------------------------------
    # Example CLI usage (for local testing)
    # ------------------------------------------------------
    if __name__ == "__main__":
      print("🔷 Welcome to Adhikar — Your AI Legal Helper\n")
      while True:
        user_input = input("Ask your question (or type 'exit' to quit): ").strip()
        if user_input.lower() in ["exit", "quit"]:
          print("👋 Goodbye! Stay informed with Adhikar.")
          break

        result = get_ai_response(user_input)

        if result["status"] == "success":
          print("\n📘 Related Laws:")
          for law in result["laws"]:
            print(" -", law)

          print("\n🔗 Useful Links:")
          for link in result["links"]:
            print(" -", link)

          if result["schemes"]:
            print("\n🏛️ Schemes:")
            for scheme in result["schemes"]:
              print(" -", scheme)

        print("\n" + "-" * 50 + "\n")