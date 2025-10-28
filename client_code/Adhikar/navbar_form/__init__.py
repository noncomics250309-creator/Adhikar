from ._anvil_designer import navbar_formTemplate
from anvil import *
import anvil.server


class navbar_form(navbar_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
# navbar.py — Responsive Navigation Bar for Adhikar
#
# Contains logo, page links, and a mobile menu toggle.
# Automatically adjusts for desktop and mobile using responsive_utils.

from anvil import *
from .. import router
from .. import responsive_utils as rutils


class NavBar(NavBarTemplate):

  def __init__(self, **properties):
    # Initialize UI components
    self.init_components(**properties)

    self.is_mobile = rutils.is_mobile()
    self.menu_open = False
    self.build_ui()

    # ---------------------------
    # UI Builder
    # ---------------------------
  def build_ui(self):
    self.clear()

    # Container for the entire navbar
    nav_container = FlowPanel(role="navbar", align="center", spacing="medium", full_width_row=True)
    nav_container.background = "#1e3a8a"
    nav_container.foreground = "white"
    nav_container.padding = "10px 15px"

    # --- Left: Logo ---
    logo_label = Label(
      text="⚖️ Adhikar",
      bold=True,
      font_size=rutils.get_responsive_font_size(20),
      align="left"
    )
    logo_label.set_event_handler("click", lambda **e: router.navigate_to("home_page"))

    nav_container.add_component(logo_label)

    # --- Right: Navigation Links ---
    if self.is_mobile:
      # Mobile: Show menu toggle button
      toggle_btn = Button(
        text="☰",
        role="filled-button",
        background="#1e3a8a",
        foreground="white",
        bold=True,
        align="right"
      )
      toggle_btn.set_event_handler("click", self.toggle_menu)
      nav_container.add_component(toggle_btn)

      # Collapsible mobile menu panel
      self.menu_panel = ColumnPanel(
        visible=False,
        background="#1e40af",
        spacing="small",
        role="mobile-menu"
      )

      for page_name, label in self.get_nav_links():
        btn = Button(
          text=label,
          role="text-button",
          foreground="white",
          bold=True,
          align="center"
        )
        btn.set_event_handler("click", lambda e=None, p=page_name: self.navigate(p))
        self.menu_panel.add_component(btn)

      self.add_component(nav_container)
      self.add_component(self.menu_panel)

    else:
      # Desktop: Inline links
      links_panel = FlowPanel(role="nav-links", align="right", spacing="large")
      for page_name, label in self.get_nav_links():
        link_btn = Button(
          text=label,
          role="text-button",
          foreground="white",
          bold=True
        )
        link_btn.set_event_handler("click", lambda e=None, p=page_name: self.navigate(p))
        links_panel.add_component(link_btn)

      nav_container.add_component(links_panel)
      self.add_component(nav_container)

    # ---------------------------
    # Navigation Helpers
    # ---------------------------
  def get_nav_links(self):
    """Return list of (page_name, label) tuples for navigation."""
    return [
      ("home_page", "Home"),
      ("demographic_form", "Start"),
      ("question_input", "Ask"),
      ("results_page", "Results"),
      ("about_page", "About"),
    ]

  def navigate(self, page_name):
    """Navigate to a given page and close menu if mobile."""
    router.navigate_to(page_name)
    if self.is_mobile:
      self.menu_panel.visible = False
      self.menu_open = False

    # ---------------------------
    # Mobile Menu Toggle
    # ---------------------------
  def toggle_menu(self, **event_args):
    """Show or hide the mobile dropdown menu."""
    self.menu_open = not self.menu_open
    self.menu_panel.visible = self.menu_open
