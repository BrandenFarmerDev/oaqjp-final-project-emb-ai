# PY0222EN Emotion Detector rubric map

This local implementation preserves the official IBM starter repository and upstream history. The official IBM Cloud IDE was used to obtain live Watson results and screenshots. No fork, push, upload, or course submission has been performed. Raw terminal/UI captures and rubric-named PNG screenshots are in `final_project/evidence/live/`; no simulated Watson output is represented as live evidence.

| Rubric points | Requirement | Local implementation / proof | State |
|---|---|---|---|
| 1 | Public README URL containing exact project name | Root `README.md` begins with `Final project` | Local README ready; public URL awaits separate authorization |
| 2 | Watson NLP `emotion_detector` function | `final_project/EmotionDetection/emotion_detection.py` posts the specified request/header and formats decoded response | Implemented; live Watson calls succeed in the official lab |
| 3 | Terminal output showing import and first test | `final_project/evidence/live/2b_application_creation.txt` and `.jpg` | Captured from Cloud IDE; genuine Watson results for “I love this new technology.” |
| 4 | Output dictionary with five emotion scores and dominant emotion | `emotion_detection.py` returns anger, disgust, fear, joy, sadness, and dominant_emotion | Implemented; live outputs verify the format |
| 5 | Terminal output verifying formatted output and joy for specified text | `final_project/evidence/live/3b_formatted_output_test.txt` and `.jpg` | Captured; Watson returned joy as dominant for “I am so happy I am doing this.” |
| 6 | Public `EmotionDetection/__init__.py` URL and valid-package test output | `final_project/EmotionDetection/__init__.py` exports `emotion_detector`; package test in `4b_packaging_test` evidence | Package verified; public URL awaits separate authorization |
| 7 | Terminal output validating `EmotionDetection` package | `final_project/evidence/live/4b_packaging_test.txt` and `.jpg` | Captured; genuine Watson output for “I hate working long hours.” |
| 8 | Test code for all five required statements | `final_project/test_emotion_detection.py` covers the required emotion examples using subtests, response schema, HTTP 400, and other HTTP errors | Implemented; 9 total project tests pass |
| 9 | Terminal output showing tests pass | `final_project/evidence/live/5b_unit_testing_result.txt` and `.jpg`; `expanded-tests.txt` and `.jpg` | Course module: 4 tests OK; expanded detector + Flask suite: 9 tests OK |
| 10 | Flask `server.py` implementation | `final_project/server.py`, route `/emotionDetector`, formatted emotion summary | Implemented and served in the Cloud IDE |
| 11 | Deployment screenshot for “I think I am having fun” | `final_project/evidence/live/6b_deployment_test.png` plus original `.jpg` | Captured from live Cloud IDE app; shows genuine Watson joy result |
| 12 | HTTP 400 returns same result keys with all `None` values | `emotion_detection.py` returns all five score keys and dominant_emotion as `None` | Implemented and unit-tested |
| 13 | Flask handles blank-input error | `server.py` returns `Invalid text! Please try again!` before calling Watson for blank/whitespace input | Implemented and verified in route tests and live UI |
| 14 | Screenshot showing blank-input message | `final_project/evidence/live/7c_error_handling_interface.png` plus original `.jpg`; whitespace screenshot also included | Captured from official Cloud IDE; exact required invalid-text response visible |
| 15 | `server.py` demonstrating Pylint execution | `final_project/server.py` | Source checked in Cloud IDE |
| 16 | Terminal output showing perfect Pylint score | `final_project/evidence/live/8b_static_code_analysis.txt` and `.jpg` | Cloud IDE Pylint result: 10.00/10 |

The point-by-point instructions are in `C:\Users\BrandenFarmer\Documents\Codex\python-development-project-evidence\final-project-instructions.txt`; the separately captured course rubric is `...\final-project-rubric.txt`.

## Local verification

From the repository root:

```powershell
.venv\Scripts\python.exe -m unittest discover -s final_project -p "test_*.py" -v
.venv\Scripts\python.exe -m pylint final_project\server.py
```

For package shell checks, change to `final_project` first so `EmotionDetection` is importable. The README and provided `templates/index.html` / `static/mywebscript.js` starter assets are present. Local and official Cloud IDE validations are documented separately in `FINAL_PROJECT_MANIFEST.md` and `final_project/evidence/README.md`.
