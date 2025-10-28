from ._anvil_designer import demographic_formTemplate
from anvil import *
import anvil.server
from anvil import *
from .. import router
from .. import responsive_utils as rutils

class demographic_form(demographic_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
# demographic_form.py — User demographic data collection for Adhikar
#
# Collects user info such as name, age, gender, state, occupation, and language.
# Validates inputs, stores them in session, and navigates to the Question Input page.



class DemographicForm(DemographicFormTemplate):

  def __init__(self, **properties):
    # Initialize form components
    self.init_components(**properties)

    # Responsive styling
    self.is_mobile = rutils.is_mobile()
    self.build_ui()

    # ---------------------------
    # UI Construction
    # ---------------------------
  def build_ui(self):
    self.clear()

    # Main container
    layout = ColumnPanel(role="card", spacing="medium")
    layout.align = "center"
    layout.background = "#ffffff"
    layout.border = "1px solid #ddd"
    layout.role = "outlined-card"

    title = Label(
      text="Tell us about yourself",
      role="headline",
      bold=True,
      align="center",
      font_size=rutils.get_responsive_font_size(24),
    )

    # Input fields
    self.name_box = TextBox(placeholder="Enter your full name", role="outlined")
    self.age_box = TextBox(type="number", placeholder="Enter your age", role="outlined")
    self.gender_drop = DropDown(items=["Male", "Female", "Non-binary", "Prefer not to say"])
    self.state_box = TextBox(placeholder="Enter your state", role="outlined")
    self.occupation_box = TextBox(placeholder="Enter your occupation", role="outlined")
    self.language_drop = DropDown(items=["English", "Hindi", "Bengali", "Tamil", "Telugu", "Marathi", "Other"])

    # Button
    continue_btn = Button(
      text="Continue",
      role="filled-button",
      background="#2563eb",
      foreground="white",
      bold=True,
      align="center",
    )
    continue_btn.set_event_handler("click", self.continue_click)

    # Add components
    layout.add_component(title)
    layout.add_component(Label(text="Name:"))
    layout.add_component(self.name_box)
    layout.add_component(Label(text="Age:"))
    layout.add_component(self.age_box)
    layout.add_component(Label(text="Gender:"))
    layout.add_component(self.gender_drop)
    layout.add_component(Label(text="State:"))
    layout.add_component(self.state_box)
    layout.add_component(Label(text="Occupation:"))
    layout.add_component(self.occupation_box)
    layout.add_component(Label(text="Language Preference:"))
    layout.add_component(self.language_drop)
    layout.add_component(continue_btn)

    # Responsive adjustments
    padding = rutils.get_responsive_padding()
    layout.spacing = padding
    layout.width = "90%" if self.is_mobile else "50%"

    self.add_component(layout, full_width_row=True)

    # ---------------------------
    # Validation Logic
    # ---------------------------
    def validate_inputs(self):
      """
        Check that all required fields are filled and valid.
        Returns a dict of user data if valid, else raises an Exception.
        """
      name = self.name_box.text.strip()
      age = self.age_box.text.strip()
      gender = self.gender_drop.selected_value
      state = self.state_box.text.strip()
      occupation = self.occupation_box.text.strip()
      language = self.language_drop.selected_value

      if not name:
        raise ValueError("Please enter your name.")
      if not age or not age.isdigit() or int(age) <= 0:
        raise ValueError("Please enter a valid age.")
      if not gender:
        raise ValueError("Please select your gender.")
      if not state:
        raise ValueError("Please enter your state.")
      if not occupation:
        raise ValueError("Please enter your occupation.")
      if not language:
        raise ValueError("Please select a language preference.")

      return {
        "name": name,
        "age": int(age),
        "gender": gender,
        "state": state,
        "occupation": occupation,
        "language": language,
      }

    # ---------------------------
    # Event Handler
    # ---------------------------
    def continue_click(self, **event_args):
      """Validate and store data, then navigate to Question Input page."""
      try:
        user_data = self.validate_inputs()

        # Save in session
        router.session["user_details"] = user_data
        print("[Session] User details saved:", user_data)

        # Navigate to next page
        router.navigate_to("question_input")

      except ValueError as ve:
        alert(str(ve), title="Invalid Input", large=True)
      except Exception as e:
        alert(f"An unexpected error occurred: {e}", title="Error", large=True)
