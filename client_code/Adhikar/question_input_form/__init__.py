from ._anvil_designer import question_input_formTemplate
from anvil import *
import anvil.server
from anvil import *
from .. import router
from .. import responsive_utils as rutils
from .. import fake_ai_engine

class question_input_form(question_input_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
# question_input.py — Legal Question Input Screen for Adhikar
#
# Lets users enter (or dictate) a legal question.
# Sends query to fake_ai_engine.py and navigates to results_page.py with the response.

  # Fake AI backend module (you can replace later)


class QuestionInput(QuestionInputTemplate):

  def __init__(self, **properties):
    # Initialize the form components
    self.init_components(**properties)

    # Responsive setup
    self.is_mobile = rutils.is_mobile()
    self.build_ui()

    # ---------------------------
    # UI Construction
    # ---------------------------
  def build_ui(self):
    self.clear()

    # Main container
    layout = ColumnPanel(role="card", spacing="medium", align="center")

    title = Label(
      text="Ask Your Legal Question",
      role="headline",
      bold=True,
      align="center",
      font_size=rutils.get_responsive_font_size(22),
    )

    instruction = Label(
      text="Type your legal issue or question in simple language below:",
      align="center",
      font_size=rutils.get_responsive_font_size(14),
    )

    # Text area for user query
    self.question_area = TextArea(
      placeholder="Describe your situation or question here...",
      height=150,
      role="outlined",
    )

    # Submit button
    submit_btn = Button(
      text="Submit",
      role="filled-button",
      background="#2563eb",
      foreground="white",
      bold=True,
      align="center",
    )
    submit_btn.set_event_handler("click", self.submit_click)

    # Voice input button (for mobile)
    self.voice_btn = Button(
      text="🎤 Speak",
      role="outlined-button",
      align="center",
    )
    self.voice_btn.set_event_handler("click", self.start_voice_input)

    # Loading spinner (hidden initially)
    self.spinner = Spinner(visible=False, align="center", role="loader")

    # Add components
    layout.add_component(title)
    layout.add_component(instruction)
    layout.add_component(self.question_area)
    if self.is_mobile:
      layout.add_component(self.voice_btn)
    layout.add_component(submit_btn)
    layout.add_component(self.spinner)

    # Apply responsive spacing
    layout.width = "90%" if self.is_mobile else "50%"
    layout.spacing = rutils.get_responsive_padding()

    self.add_component(layout, full_width_row=True)

    # ---------------------------
    # Voice Input Handler (Mobile Only)
    # ---------------------------
    def start_voice_input(self, **event_args):
      """
        Trigger speech recognition on mobile devices.
        Requires a browser that supports Web Speech API.
        """
      try:
        import anvil.js

        recognition = anvil.js.window.webkitSpeechRecognition.new()
        recognition.lang = "en-IN"

        def on_result(event):
          transcript = event.results[0][0].transcript
          self.question_area.text = transcript

        recognition.onresult = on_result
        recognition.start()

      except Exception as e:
        alert("Voice input not supported on this device or browser.", title="Unavailable")

    # ---------------------------
    # Submission Logic
    # ---------------------------
    def submit_click(self, **event_args):
      """Validate input, show spinner, and fetch answer from fake AI."""
      question = self.question_area.text.strip()

      if not question:
        alert("Please enter your question before submitting.", title="Missing Input")
        return

        # Show loading spinner
      self.spinner.visible = True

      # Call fake AI engine
      try:
        # Simulate async delay using server call or fake backend
        answer = fake_ai_engine.get_legal_answer(question)

        # Save to session
        router.session["user_question"] = question
        router.session["ai_answer"] = answer

        # Hide spinner and navigate
        self.spinner.visible = False
        router.navigate_to("results_page")

      except Exception as e:
        self.spinner.visible = False
        alert(f"Something went wrong while processing your question.\n\n{e}", title="Error")
