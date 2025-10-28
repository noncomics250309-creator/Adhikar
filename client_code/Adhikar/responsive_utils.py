# responsive_utils.py — Responsive utilities for the Adhikar Anvil app
#
# Detects device type (mobile vs desktop) using window size and user agent,
# and provides helper functions to adapt UI elements dynamically.

from anvil import *
import anvil.js


# ---------------------------
# Device Detection
# ---------------------------

def is_mobile():
  """
    Detect if the user is on a mobile device.
    Uses screen width and user agent for robustness.
    """
  try:
    window = anvil.js.window

    # Method 1: Based on viewport width
    width = window.innerWidth if hasattr(window, "innerWidth") else 1024
    if width < 768:  # typical mobile breakpoint
      return True

      # Method 2: Based on user agent
    ua = str(window.navigator.userAgent).lower()
    mobile_keywords = ["iphone", "android", "mobile", "ipad", "ipod"]
    if any(keyword in ua for keyword in mobile_keywords):
      return True

    return False

  except Exception as e:
    print(f"[Responsive Utils] Detection failed: {e}")
    return False  # fallback to desktop


# ---------------------------
# Style Helpers
# ---------------------------

def get_responsive_padding():
  """Return padding value based on device type."""
  return "8px" if is_mobile() else "16px"


def get_responsive_font_size(base=14):
  """Return a scaled font size based on device type."""
  return f"{base - 2}px" if is_mobile() else f"{base}px"


def apply_responsive_style(component, base_font=14, base_padding=12):
  """
    Automatically adjust styles of a component based on device type.
    - Adjusts padding and font size
    - Can be called in form init or after layout load
    """
  try:
    mobile = is_mobile()
    padding = f"{base_padding * 0.6}px" if mobile else f"{base_padding}px"
    font_size = f"{base_font - 2}px" if mobile else f"{base_font}px"

    # Apply to component style dictionary (if exists)
    component.role = component.role or "default"
    component.spacing = padding
    component.font_size = font_size

    # Optionally, apply to content panels
    if hasattr(component, "content_panel"):
      component.content_panel.spacing = padding

  except Exception as e:
    print(f"[Responsive Utils] Failed to apply responsive style: {e}")


# ---------------------------
# Layout Helper
# ---------------------------

def responsive_layout(mobile_layout, desktop_layout):
  """
    Return the appropriate layout based on device type.
    Example:
        layout = responsive_layout(MobileLayout(), DesktopLayout())
        open_form(layout)
    """
  try:
    return mobile_layout if is_mobile() else desktop_layout
  except Exception as e:
    print(f"[Responsive Utils] Layout selection failed: {e}")
    return desktop_layout

