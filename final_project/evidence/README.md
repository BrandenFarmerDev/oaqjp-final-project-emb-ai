# Blank-input interface evidence

The course requires `7c_error_handling_interface.png` to show the app's invalid-text response. No screenshot has been saved yet. Blank and whitespace values were submitted through the local Flask UI and the required message appeared, but the screenshot evidence must be captured from the official Cloud IDE/browser workflow.

## Reproduce

1. From the repository root, start the app: `.venv\Scripts\python.exe final_project\server.py`.
2. Open `http://127.0.0.1:5000/` in Chrome.
3. Leave the text field empty and click **Run Sentiment Analysis**; verify `Invalid text! Please try again!` appears.
4. Enter three spaces and click the same button; verify the same message appears.
5. Clear the field and leave the message displayed for the clean screenshot.

Capture the screenshot directly from the official Cloud IDE/browser after verifying the empty-input response. The local Watson endpoint timed out; valid-input screenshots and genuine emotion scores remain pending a successful live service call.
