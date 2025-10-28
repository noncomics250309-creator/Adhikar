from ._anvil_designer import about_page_formTemplate
from anvil import *
import anvil.server
from anvil import *
from .. import router
from .. import responsive_utils as rutils

class about_page_form(about_page_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
# about_page.py — Informational About Page for the Adhikar App
#
# Displays project overview, mission, team, disclaimer, and contact information.




class AboutPage(AboutPageTemplate):

  def __init__(self, **properties):
    # Initialize the form
    self.init_components(**properties)

    self.is_mobile = rutils.is_mobile()
    self.build_ui()

    # ---------------------------
    # UI Builder
    # ---------------------------
  def build_ui(self):
    self.clear()

    layout = ColumnPanel(role="card", spacing="medium", align="center")
    layout.width = "95%" if self.is_mobile else "70%"
    layout.spacing = rutils.get_responsive_padding()

    # --- Title ---
    title = Label(
      text="About Adhikar",
      role="headline",
      bold=True,
      font_size=rutils.get_responsive_font_size(26),
      align="center",
    )

    tagline = Label(
      text="Empowering Citizens with Accessible Legal Awareness",
      italic=True,
      font_size=rutils.get_responsive_font_size(16),
      align="center",
    )

    # --- Mission Section ---
    mission_card = ColumnPanel(role="card", background="#f0f9ff", spacing="small")
    mission_card.add_component(Label(text="Our Mission", bold=True, font_size=rutils.get_responsive_font_size(18)))
    mission_card.add_component(Label(
      text=(
        "Adhikar is a civic technology initiative designed to make legal information "
        "accessible, understandable, and personalized for every Indian citizen. "
        "We aim to bridge the gap between complex legal frameworks and ordinary people, "
        "using AI-assisted explanations in regional languages."
      ),
      font_size=rutils.get_responsive_font_size(14)
    ))

    # --- Team Section ---
    team_card = ColumnPanel(role="card", background="#eef2ff", spacing="small")
    team_card.add_component(Label(text="Our Team", bold=True, font_size=rutils.get_responsive_font_size(18)))
    team_card.add_component(Label(
      text=(
        "The Adhikar project was developed by a multidisciplinary team of students and mentors "
        "participating in the National Legal Tech Buildathon. Our collective expertise in law, "
        "AI, and civic design drives this initiative."
      ),
      font_size=rutils.get_responsive_font_size(14)
    ))

    # --- Disclaimer Section ---
    disclaimer_card = ColumnPanel(role="card", background="#fff7ed", spacing="small")
    disclaimer_card.add_component(Label(text="Disclaimer", bold=True, font_size=rutils.get_responsive_font_size(18)))
    disclaimer_card.add_component(Label(
      text=(
        "Adhikar provides AI-generated legal information for general awareness only. "
        "It is not a substitute for professional legal advice, and users should consult "
        "qualified legal professionals for specific cases."
      ),
      font_size=rutils.get_responsive_font_size(14)
    ))

    # --- Contact Section ---
    contact_card = ColumnPanel(role="card", background="#f9fafb", spacing="small")
    contact_card.add_component(Label(text="Contact Us", bold=True, font_size=rutils.get_responsive_font_size(18)))
    contact_card.add_component(Label(text="📧 Email: contact@adhikar.build", font_size=rutils.get_responsive_font_size(14)))
    contact_card.add_component(Link(text="Visit Buildathon Page", url="https://buildathon.legaltechindia.org", align="center"))

    # --- Back / Home Button ---
    home_btn = Button(
      text="Back to Home",
      role="filled-button",
      background="#2563eb",
      foreground="white",
      bold=True,
      align="center",
    )
    home_btn.set_event_handler("click", self.back_to_home)

    # Add everything to the layout
    layout.add_component(title)
    layout.add_component(tagline)
    layout.add_component(mission_card)
    layout.add_component(team_card)
    layout.add_component(disclaimer_card)
    layout.add_component(contact_card)
    layout.add_component(home_btn)

    self.add_component(layout, full_width_row=True)

    # ---------------------------
    # Event Handler
    # ---------------------------
  def back_to_home(self, **event_args):
        """Navigate back to the Home Page."""
        router.navigate_to("home_page")
