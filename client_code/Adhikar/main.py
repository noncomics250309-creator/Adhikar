
# main.py — Entry point for Adhikar app

import anvil.server
import anvil.users
import anvil.router
from anvil import *
from anvil_extras import routing
from anvil_extras.utils import is_mobile_device

# Import pages
from ..Home import HomePage
from ..Error import ErrorPage
from ..MobileLayout import MobileLayout
from ..DesktopLayout import DesktopLayout


def initialize_app():
  """
    Initialize the Adhikar app with routing, layout, and device detection.
    """
  try:
    # Detect device type (mobile vs desktop)
    mobile = is_mobile_device()

    # Choose layout accordingly
    layout = MobileLayout() if mobile else DesktopLayout()

    # Set up router with default home page
    router = routing.Router()
    router.set_url_hash_prefix('#')
    router.mount_point = layout.content_panel  # Assume layout has a 'content_panel'

    # Register routes
    @router.route('')
    @router.route('home')
    def home_page():
      return HomePage()

    @router.not_found
    def not_found_page(**kw):
      return ErrorPage(message="The page you're looking for doesn’t exist.")

      # Start the router
    routing.set_url_hash('home')
    layout.add_component(router)

    # Display layout
    open_form(layout)

  except Exception as e:
    # Graceful error handling and fallback
    print(f"[ERROR] App initialization failed: {e}")
    open_form(ErrorPage(message="An unexpected error occurred while loading Adhikar."))


# Initialize the app
initialize_app()

