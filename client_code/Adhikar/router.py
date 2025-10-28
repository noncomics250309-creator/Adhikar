# router.py — Routing manager for the Adhikar Anvil app
#
# Handles page switching, session state, and navigation history.
# Works with both desktop and mobile layouts.

from anvil import *
import anvil.server
import anvil.users

# Import your page Forms
from ..Home import HomePage
from ..DemographicForm import DemographicForm
from ..QuestionInput import QuestionInput
from ..ResultsPage import ResultsPage
from ..About import AboutPage
from ..Error import ErrorPage


# ---------------------------
# Global session + navigation
# ---------------------------
session = {
  "user": None,
  "current_page": None,
  "page_stack": [],  # for back navigation
}


# ---------------------------
# Page map
# ---------------------------
PAGE_MAP = {
  "home_page": HomePage,
  "demographic_form": DemographicForm,
  "question_input": QuestionInput,
  "results_page": ResultsPage,
  "about_page": AboutPage,
}


# ---------------------------
# Core Navigation Functions
# ---------------------------
def navigate_to(page_name, data=None):
  """
    Navigate to a page by name.
    Pushes current page onto stack for back navigation.
    """
  try:
    if page_name not in PAGE_MAP:
      raise ValueError(f"Unknown page: {page_name}")

      # Get the page class and instantiate it
    page_class = PAGE_MAP[page_name]
    new_page = page_class(data=data) if data else page_class()

    # Save current page before switching
    current = session.get("current_page")
    if current:
      session["page_stack"].append(current)

      # Open the new page
    open_form(new_page)
    session["current_page"] = new_page

  except Exception as e:
    print(f"[Router Error] Failed to navigate to {page_name}: {e}")
    open_form(ErrorPage(message=f"Could not load {page_name}. Please try again."))


def go_back():
  """
    Navigate back to the previous page, if available.
    """
  try:
    if session["page_stack"]:
      previous_page = session["page_stack"].pop()
      open_form(previous_page)
      session["current_page"] = previous_page
    else:
      # No previous page — go to home
      navigate_to("home_page")

  except Exception as e:
    print(f"[Router Error] Back navigation failed: {e}")
    open_form(ErrorPage(message="Navigation error. Returning to home."))
    navigate_to("home_page")


# ---------------------------
# Session Helpers
# ---------------------------
def set_user(user_obj):
  """Store the current logged-in user."""
  session["user"] = user_obj


def get_user():
  """Retrieve the current logged-in user."""
  return session.get("user")


def reset_session():
  """Reset all navigation and session state."""
  session.update({
    "user": None,
    "current_page": None,
    "page_stack": [],
  })


# ---------------------------
# Initialization
# ---------------------------
def init_router(start_page="home_page"):
  """
    Initialize router and start the app at a given page.
    """
  reset_session()
  navigate_to(start_page)

