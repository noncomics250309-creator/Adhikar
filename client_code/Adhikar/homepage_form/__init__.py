from ._anvil_designer import homepage_formTemplate
from anvil import *
import anvil.server
from anvil import *
from .. import router
from .. import responsive_utils as rutils

class homepage_form(homepage_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
# home_page.py — Home Page UI for the Adhikar app
#
# Displays app title, tagline, and a "Get Started" button.
# Automatically adapts to mobile and desktop layouts using responsive_utils.

class HomePage(HomePageTemplate):

  def __init__(self, **properties):
    # Initialize UI components
    self.init_components(**properties)

    # Apply responsive design
    self.is_mobile = rutils.is_mobile()
    self.build_ui()

    # ---------------------------
    # UI Construction
    # ---------------------------
  def build_ui(self):
    # Clear default content
    self.clear()

    # Create main card for centered content
    card = ColumnPanel(role="card", spacing="medium")
    card.align = "center"
    card.spacing = "medium"
    card.background = "#ffffff"
    card.border = "1px solid #ddd"
    card.role = "outlined-card"

    # Add app title
    title = Label(
      text="Adhikar",
      role="headline",
      bold=True,
      align="center",
      font_size=rutils.get_responsive_font_size(32),
    )

    # Add tagline
    tagline = Label(
      text="Personalized Justice for Every Citizen",
      align="center",
      font_size=rutils.get_responsive_font_size(16),
      italic=True,
      foreground="#555",
    )

    # Add "Get Started" button
    get_started_btn = Button(
      text="Get Started",
      role="filled-button",
      align="center",
      background="#2563eb",
      foreground="white",
      bold=True,
    )
    get_started_btn.set_event_handler("click", self.get_started_click)

    # Layout container
    layout = FlowPanel(role="container", align="center", spacing="large")
    layout.add_component(card)

    # Add elements to card
    card.add_component(title)
    card.add_component(tagline)
    card.add_component(get_started_btn)

    # Adjust padding for mobile vs desktop
    padding = rutils.get_responsive_padding()
    layout.spacing = padding
    card.spacing = padding

    # Differentiate by device
    if self.is_mobile:
      layout.role = "mobile-container"
      card.role = "mobile-card"
      card.width = "90%"
    else:
      layout.role = "desktop-container"
      card.role = "desktop-card"
      card.width = "50%"

      # Add final layout to the page
    self.add_component(layout, full_width_row=True)

    # ---------------------------
    # Button Event Handler
    # ---------------------------
  def get_started_click(self, **event_args):
    """Navigate to the Demographic Form when the user clicks 'Get Started'."""
    router.navigate_to("demographic_form")
