# PY0222EN Emotion Detector: 16-point evaluator manifest

This manifest maps every one-point activity to implementation and evidence. Authentic course Cloud IDE outputs/screenshots are stored under `final_project/evidence/live/`. The local work remains unpublished and unsubmitted; the public-URL points therefore remain pending.

| Point | Course activity | Source/file requirement | Evidence artifact | Status |
|---:|---|---|---|---|
| 1 | Task 1: repository URL for README containing exact project name | Root `README.md` says `Final project` | `README.md` | Local file ready; public URL pending publication approval |
| 2 | Task 2A: Watson NLP application function | `final_project/EmotionDetection/emotion_detection.py` | `final_project/EmotionDetection/emotion_detection.py` | Implemented; requests and response formatting verified |
| 3 | Task 2B: import and test application with “I love this new technology.” | Package import and live Watson prediction | `final_project/evidence/live/2b_application_creation.txt` and `.jpg` | PASS; genuine Cloud IDE Watson output captured |
| 4 | Task 3A: format five scores and determine dominant emotion | `emotion_detection.py` result dictionary | `final_project/EmotionDetection/emotion_detection.py` | PASS; all five scores and dominant key implemented |
| 5 | Task 3B: verify joy for “I am so happy I am doing this.” | Live formatted prediction | `final_project/evidence/live/3b_formatted_output_test.txt` and `.jpg` | PASS; live Watson returned joy as dominant emotion |
| 6 | Task 4A: public URL for package import file | `final_project/EmotionDetection/__init__.py` | `final_project/EmotionDetection/__init__.py` | Local package ready; public URL pending publication approval |
| 7 | Task 4B: validate `EmotionDetection` with “I hate working long hours.” | Package import plus live prediction | `final_project/evidence/live/4b_packaging_test.txt` and `.jpg` | PASS; genuine live Watson output captured |
| 8 | Task 5A: required five unit-test inputs | `final_project/test_emotion_detection.py` | `final_project/test_emotion_detection.py` | PASS; required emotion examples are covered by subtests, along with response/error cases |
| 9 | Task 5B: terminal output showing tests pass | Run test module in Cloud IDE | `final_project/evidence/live/5b_unit_testing_result.txt` and `.jpg`; `expanded-tests.txt` and `.jpg` | PASS; course test module reports 4 tests OK; expanded course suite reports 9 tests OK |
| 10 | Task 6A: Flask web deployment | `final_project/server.py` | `final_project/server.py` | PASS; live app started in Cloud IDE and served the browser UI |
| 11 | Task 6B: deployed app tested with “I think I am having fun” | Live Watson-backed Flask app | `final_project/evidence/live/6b_deployment_test.png` (PNG) and original `.jpg`, `.txt` | PASS; captured UI shows live Watson scores and joy as dominant |
| 12 | Task 7A: HTTP 400 gives all-`None` emotion result | `emotion_detection.py` | `final_project/EmotionDetection/emotion_detection.py` and unit tests | PASS; all result fields are `None` on HTTP 400 |
| 13 | Task 7B: Flask error for blank input | `server.py` | `final_project/server.py` and `test_server.py` | PASS; blank and whitespace are handled without a Watson request |
| 14 | Task 7C: screenshot of invalid-text UI response | Browser UI with blank input | `final_project/evidence/live/7c_error_handling_interface.png` (PNG) and original `.jpg`, `.txt`; whitespace capture also included | PASS; authentic Cloud IDE UI screenshot shows exact required message |
| 15 | Task 8A: `server.py` demonstrating Pylint execution | `final_project/server.py` | `final_project/server.py` | PASS; source checked in Cloud IDE |
| 16 | Task 8B: terminal output showing perfect static-analysis score | Pylint run on server | `final_project/evidence/live/8b_static_code_analysis.txt` and `.jpg` | PASS; Pylint reports 10.00/10 |

## Completion gates

- Local unit tests, syntax checks, dependency checks, and Pylint pass.
- Genuine Watson responses, course test output, Pylint output, and app screenshots have been captured from the official Cloud IDE.
- Independent QA must review the local branch, upstream lineage, exact files, manifest, and evidence.
- Keep the repository unpublished until separately authorized; course submission requires separate authorization.
