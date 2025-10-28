from ._anvil_designer import result_page_formTemplate
from anvil import *
import anvil.server
from anvil import *
from .. import router
from .. import responsive_utils as rutils

class result_page_form(result_page_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
# results_page.py — Results Page for Adhikar
#
# Displays the AI-generated legal answer, relevant laws/schemes,
# and links to official sources. Includes localization and a "Ask Another Question" button.


class ResultsPage(ResultsPageTemplate):

  def __init__(self, **properties):
    # Initialize components
    self.init_components(**properties)

    self.is_mobile = rutils.is_mobile()
    self.build_ui()

    # ---------------------------
    # UI Construction
    # ---------------------------
  def build_ui(self):
    self.clear()

    # Retrieve data from session
    user_question = router.session.get("user_question", "Your question")
    ai_answer = router.session.get("ai_answer", "No answer found.")
    user_details = router.session.get("user_details", {})
    language = user_details.get("language", "English")

    # Localize content if possible (simple example)
    localized_answer = self.localize_text(ai_answer, language)

    # Main layout
    layout = ColumnPanel(role="card", spacing="medium", align="center")
    layout.background = "#ffffff"
    layout.border = "1px solid #ddd"

    # Title
    title = Label(
      text="Your Legal Guidance",
      role="headline",
      bold=True,
      align="center",
      font_size=rutils.get_responsive_font_size(22),
    )

    # User’s Question
    q_card = ColumnPanel(role="card", background="#f9fafb", spacing="small")
    q_card.add_component(Label(text="Your Question:", bold=True))
    q_card.add_component(Label(text=user_question, italic=True))

    # AI Answer
    a_card = ColumnPanel(role="card", background="#f0f9ff", spacing="small")
    a_card.add_component(Label(text="Our Guidance:", bold=True))
    a_card.add_component(Label(text=localized_answer, font_size=rutils.get_responsive_font_size(14)))

    # Relevant Laws & Schemes (Mock data for now)
    law_cards_container = FlowPanel(role="container", spacing="medium", align="center")
    laws = [
      {"title": "Right to Information Act, 2005", "link": "https://rti.gov.in"},
      {"title": "Legal Services Authorities Act, 1987", "link": "https://nalsa.gov.in"},
      {"title": "Public Grievances Portal", "link": "https://pgportal.gov.in"},
    ]

    for law in laws:
      card = ColumnPanel(role="card", background="#eef2ff", spacing="small", width="100%" if self.is_mobile else "30%")
      card.add_component(Label(text=law["title"], bold=True))
      card.add_component(Link(text="View official source", url=law["link"], align="center"))
      law_cards_container.add_component(card)

      # Ask Another Question button
    another_btn = Button(
      text="Ask Another Question",
      role="filled-button",
      background="#2563eb",
      foreground="white",
      bold=True,
      align="center",
    )
    another_btn.set_event_handler("click", self.ask_another_click)

    # Add all components
    layout.add_component(title)
    layout.add_component(q_card)
    layout.add_component(a_card)
    layout.add_component(Label(text="Relevant Laws & Schemes:", bold=True, align="center"))
    layout.add_component(law_cards_container)
    layout.add_component(another_btn)

    # Responsive sizing
    layout.width = "95%" if self.is_mobile else "70%"
    layout.spacing = rutils.get_responsive_padding()
    self.add_component(layout, full_width_row=True)

    # ---------------------------
    # Localization Helper
    # ---------------------------
  def localize_text(self, text, language):
    """
        Simple localization placeholder.
        Later, you can integrate a translation API or pre-stored language maps.
        """
    translations = {
      "Hindi": "यह एक सरल व्याख्या है: " + text,
      "Bengali": "এটি একটি সরল ব্যাখ্যা: " + text,
      "Tamil": "இது ஒரு எளிய விளக்கம்: " + text,
      "Telugu": "ఇది సులభమైన వివరణ: " + text,
      "Marathi": "ही एक सोपी स्पष्टीकरण आहे: " + text,
    }
    return translations.get(language, text)

    # ---------------------------
    # Navigation Event
    # ---------------------------
  def ask_another_click(self, **event_args):
    """Clear current Q&A and navigate back to the question input page."""
    router.session["user_question"] = None
    router.session["ai_answer"] = None
    router.navigate_to("question_input")
