from ._anvil_designer import card_component_formTemplate
from anvil import *
import anvil.server
from anvil import *
from .. import responsive_utils as rutils

class card_component_form(card_component_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
# card_component.py — Reusable Card Component for Adhikar
#
# Displays a title, short description, and a link button.
# Automatically adapts size and layout for mobile vs desktop.

class CardComponent(CardComponentTemplate):

  def __init__(self, title="", description="", link_text="Learn More", link_url=None, **properties):
    # Initialize UI components
    self.init_components(**properties)

    self.is_mobile = rutils.is_mobile()

    # Assign properties
    self.title_label.text = title
    self.desc_label.text = description
    self.link_button.text = link_text
    self.link_url = link_url

    # Responsive adjustments
    self.set_responsive_styles()

    # ---------------------------
    # Responsive Styling
    # ---------------------------
  def set_responsive_styles(self):
    """Adjust layout, font, and spacing for mobile vs desktop."""
    self.role = "card"
    self.background = "#f9fafb"
    self.border = "1px solid #ddd"
    self.spacing = rutils.get_responsive_padding()
    self.width = "100%" if self.is_mobile else "30%"
    self.title_label.font_size = rutils.get_responsive_font_size(16)
    self.desc_label.font_size = rutils.get_responsive_font_size(13)
    self.link_button.font_size = rutils.get_responsive_font_size(12)

    # ---------------------------
    # Event Handlers
    # ---------------------------
  def link_button_click(self, **event_args):
    """Open the external URL when button is clicked."""
    if self.link_url:
      open_form(Link(url=self.link_url))
    else:
      alert("No link available.")
