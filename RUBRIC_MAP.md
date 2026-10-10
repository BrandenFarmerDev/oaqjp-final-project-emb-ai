# PY0222EN Emotion Detector rubric map

This is a local implementation based on the official IBM starter repository. No fork, push, upload, course deployment, or submission has been performed. Mock-based tests verify local code paths only; genuine course terminal outputs and screenshots remain pending in the IBM Cloud IDE with live Watson service access. No simulated results are presented as course evidence.

| Rubric points | Requirement | Local implementation / proof | State |
|---|---|---|---|
| 1 | Public README URL containing exact project name | Root `README.md` begins with `Final project` | Local file ready; public URL awaits separate authorization |
| 2 | Watson NLP `emotion_detector` function | `final_project/EmotionDetection/emotion_detection.py` posts the specified request/header and returns response text decoded as JSON | Implemented; live endpoint timed out from this environment |
| 3 | Terminal output showing import and first test | Run from `final_project`: `python -c "from EmotionDetection import emotion_detector; print(emotion_detector('I love this new technology.'))"` | Genuine terminal output pending Cloud IDE/live Watson access; local call timed out |
| 4 | Output dictionary with five emotion scores and dominant emotion | `emotion_detection.py` returns anger, disgust, fear, joy, sadness, and dominant_emotion | Implemented and tested with mocked service responses |
| 5 | Terminal output verifying formatted output and joy for specified text | Run from `final_project`: `python -c "from EmotionDetection import emotion_detector; print(emotion_detector('I am so happy I am doing this.'))"` | Genuine terminal output pending Cloud IDE/live Watson access |
| 6 | Public `EmotionDetection/__init__.py` URL and valid-package test output | `final_project/EmotionDetection/__init__.py` exports `emotion_detector`; package import is exercised by tests | Local package verified; public URL awaits separate authorization |
| 7 | Terminal output validating `EmotionDetection` package | Package import and `I hate working long hours.` call described in Task 4 | Genuine terminal output pending Cloud IDE/live Watson access |
| 8 | Test code for all five required statements | `final_project/test_emotion_detection.py` tests joy, anger, disgust, sadness, fear, output schema, HTTP 400, and other HTTP failures | Implemented; 9 project tests pass |
| 9 | Terminal output showing tests pass | `.venv/Scripts/python.exe -m unittest discover -s final_project -p 'test_*.py' -v` | Local mock-based tests pass; genuine course evidence pending Cloud IDE |
| 10 | Flask `server.py` implementation | `final_project/server.py`, route `/emotionDetector`, formatted emotion summary | Implemented; Flask client tests pass |
| 11 | Deployment screenshot for “I think I am having fun” | Course-required `final_project/6b_deployment_test.png` | Genuine screenshot pending Cloud IDE/live Watson access |
| 12 | HTTP 400 returns same result keys with all `None` values | `emotion_detection.py` returns all five score keys and dominant_emotion as `None` | Implemented and tested |
| 13 | Flask handles blank-input error | `server.py` returns `Invalid text! Please try again!` when dominant emotion is `None` | Implemented and tested |
| 14 | Screenshot showing blank-input message | Course-required `final_project/7c_error_handling_interface.png` | Can be captured locally without Watson because blank input short-circuits the service call; screenshot not yet captured. Valid-input/deployment evidence remains pending Cloud IDE/live Watson access. |
| 15 | `server.py` demonstrating Pylint execution | `final_project/server.py`; run `.venv/Scripts/python.exe -m pylint final_project/server.py` | 10.00/10 locally |
| 16 | Terminal output showing perfect Pylint score | Pylint result for `final_project/server.py` | Pass: 10.00/10 |

The 16-point breakdown above follows the one-point activities in Tasks 1–8 and the saved course rubric at `C:\Users\BrandenFarmer\Documents\Codex\python-development-project-evidence\final-project-rubric.txt`; detailed instructions are in `...\final-project-instructions.txt`. A direct local Watson call timed out at `sn-watson-emotion.labs.skills.network`; genuine live-service outputs and interface screenshots must be captured in the IBM Cloud IDE where the course service is available.

## Local verification

From the repository root:

```powershell
.venv\Scripts\python.exe -m unittest discover -s final_project -p "test_*.py" -v
.venv\Scripts\python.exe -m pylint final_project\server.py
```

For the Python package shell checks, change to `final_project` first so `EmotionDetection` is importable. The README and provided `templates/index.html` / `static/mywebscript.js` starter assets are present; only local behavior has been verified. Course submission evidence must be captured in the course environment after a live Watson service is reachable.
