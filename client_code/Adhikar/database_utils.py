import json
import difflib

# -------------------------------
# Utility functions for Adhikar app
# -------------------------------

def load_json(file_path):
  """
    Load and return JSON data from a given file path.
    Returns an empty list if file not found or invalid.
    """
  try:
    with open(file_path, "r", encoding="utf-8") as f:
      return json.load(f)
  except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"[Error] Failed to load {file_path}: {e}")
    return []


def load_data(questions_file="questions.json", answers_file="answers.json"):
  """
    Load both questions and answers JSON files.
    Returns (questions_list, answers_list)
    """
  questions = load_json(questions_file)
  answers = load_json(answers_file)
  return questions, answers


def get_answer_by_question_id(answers, question_id):
  """
    Retrieve the answer corresponding to a given question_id.
    Returns None if no match is found.
    """
  for ans in answers:
    if str(ans.get("id")) == str(question_id) or str(ans.get("question_id")) == str(question_id):
      return ans
  return None


def search_question(user_query, questions, threshold=0.6):
  """
    Perform fuzzy matching to find the closest matching question
    to the user's input. Returns the best match (dict) or None.
    
    Parameters:
        - user_query: string input from user
        - questions: list of question dicts
        - threshold: minimum similarity ratio (0 to 1)
    """
  best_match = None
  best_score = 0

  for q in questions:
    question_text = q.get("question", "")
    ratio = difflib.SequenceMatcher(None, user_query.lower(), question_text.lower()).ratio()

    # Give small boost for keyword overlap
    keywords = " ".join(q.get("keywords", []))
    if any(k.lower() in user_query.lower() for k in q.get("keywords", [])):
      ratio += 0.1

    if ratio > best_score:
      best_score = ratio
      best_match = q

    return best_match if best_score >= threshold else None


def find_answer(user_query, questions, answers):
    """
    End-to-end utility: takes a user’s query, performs fuzzy matching,
    and returns the best-matched question and its corresponding answer.
    """
    matched_question = search_question(user_query, questions)

    if matched_question:
        q_id = matched_question.get("id")
        answer_data = get_answer_by_question_id(answers, q_id)
        return {
            "question": matched_question,
            "answer": answer_data
        } if answer_data else None
    else:
        return None


def pretty_print_result(result):
    """
    Display a matched Q&A result in a user-friendly format.
    Useful for debugging or console testing.
    """
    if not result:
        print("❌ No close match found for your question.")
        return

    q = result["question"]
    a = result["answer"]

    print("\n🔹 Matched Question:")
    print(f"   {q.get('question')} ({q.get('category')})")
    print("\n💬 Answer:")
    print(f"   {a.get('answer')}")
    print("\n📘 Related Laws:")
    for law in a.get("related_laws", []):
        print(f"   - {law}")
    print("\n🔗 Useful Links:")
    for link in a.get("links", []):
        print(f"   - {link}")
    print("\n🏛️ Schemes:")
    for scheme in a.get("schemes", []):
        print(f"   - {scheme}")


# -------------------------------
# Example usage (for testing)
# -------------------------------
if __name__ == "__main__":
    questions, answers = load_data("questions.json", "answers.json")

    user_query = input("Ask your legal question: ")
    result = find_answer(user_query, questions, answers)
    pretty_print_result(result)

