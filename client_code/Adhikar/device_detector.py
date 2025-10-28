# ------------------------------------------------------
# Adhikar App — device_detector.py
# Detects whether the user is on mobile or desktop
# ------------------------------------------------------

import anvil.js

def get_device_type():
  """
    Detects if the app is being accessed from a mobile or desktop device.
    Uses the browser's userAgent string and screen width as fallback.
    Returns: "mobile" or "desktop"
    """
  try:
    # Access browser information
    user_agent = anvil.js.window.navigator.userAgent.lower()
    width = anvil.js.window.innerWidth

    # Heuristic list of common mobile identifiers
    mobile_indicators = [
      "iphone", "android", "ipad", "mobile", "blackberry", "nokia", "windows phone"
    ]

    # Check for known mobile keywords
    if any(keyword in user_agent for keyword in mobile_indicators):
      return "mobile"

      # Fallback check based on screen width
    if width < 768:
      return "mobile"

    return "desktop"

  except Exception as e:
    print(f"[Warning] Could not detect device type: {e}")
    # Default to desktop if detection fails
    return "desktop"


def is_mobile():
  """Convenience helper function."""
  return get_device_type() == "mobile"


def is_desktop():
  """Convenience helper function."""
  return get_device_type() == "desktop"


# ------------------------------------------------------
# Example usage (for local or Anvil testing)
# ------------------------------------------------------
if __name__ == "__main__":
  device = get_device_type()
  print(f"Detected device type: {device}")
