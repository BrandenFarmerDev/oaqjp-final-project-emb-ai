# PY0222EN Emotion Detector: 16-point evaluator manifest

This manifest maps every one-point AI-graded activity to the corresponding project file and planned evidence artifact. Status describes current local readiness; Cloud IDE outputs/screenshots and public URLs are not invented. See `RUBRIC_MAP.md` for implementation notes and `final_project/evidence/README.md` for the authentic-evidence process.

| Point | Course activity | Source/file requirement | Evidence artifact | Status |
|---:|---|---|---|---|
| 1 | Task 1: repository URL for README containing exact project name | Root `README.md` must say `Final project` | `final_project/evidence/1_readme_url.txt` | Local README ready; public URL pending approved publication |
| 2 | Task 2A: Watson NLP application function | `final_project/EmotionDetection/emotion_detection.py` | `final_project/evidence/2a_emotion_detection.txt` | Implemented; syntax/tests pass |
| 3 | Task 2B: import and test application with “I love this new technology.” | Package import and live Watson prediction | `final_project/evidence/2b_application_creation.txt` | Pending genuine Cloud IDE output/live Watson |
| 4 | Task 3A: format five scores and determine dominant emotion | `emotion_detection.py` result dictionary | `final_project/evidence/3a_output_formatting.txt` | Implemented and unit-tested with mocks |
| 5 | Task 3B: verify joy for “I am so happy I am doing this.” | Live formatted prediction | `final_project/evidence/3b_formatted_output_test.txt` | Pending genuine Cloud IDE output/live Watson |
| 6 | Task 4A: public URL for package import file | `final_project/EmotionDetection/__init__.py` | `final_project/evidence/4a_init_url.txt` | Local package ready; public URL pending approved publication |
| 7 | Task 4B: validate `EmotionDetection` with “I hate working long hours.” | Package import plus live prediction | `final_project/evidence/4b_packaging_test.txt` | Pending genuine Cloud IDE output/live Watson |
| 8 | Task 5A: required five unit tests | `final_project/test_emotion_detection.py` | `final_project/evidence/5a_unit_testing.txt` | Implemented; tests pass locally with mocked service |
| 9 | Task 5B: terminal output showing tests pass | Run test module in Cloud IDE | `final_project/evidence/5b_unit_testing_result.txt` | Local tests pass; genuine course terminal output pending |
| 10 | Task 6A: Flask web deployment | `final_project/server.py` | `final_project/evidence/6a_server.txt` | Implemented; local route tests pass |
| 11 | Task 6B: deployed app tested with “I think I am having fun” | Live deployed Flask app | `final_project/evidence/6b_deployment_test.png` | Pending live Watson and authentic screenshot |
| 12 | Task 7A: HTTP 400 gives all-`None` emotion result | `emotion_detection.py` | `final_project/evidence/7a_error_handling_function.txt` | Implemented and unit-tested |
| 13 | Task 7B: Flask error for blank input | `server.py` | `final_project/evidence/7b_error_handling_server.txt` | Implemented; blank/whitespace UI verified locally |
| 14 | Task 7C: screenshot of invalid-text UI response | Browser UI with blank input | `final_project/evidence/7c_error_handling_interface.png` | Pending genuine Cloud IDE screenshot; local blank route now avoids Watson |
| 15 | Task 8A: server source demonstrating Pylint/static analysis | `final_project/server.py` | `final_project/evidence/8a_server_modified.txt` | Pylint score 10.00/10 locally |
| 16 | Task 8B: terminal output showing perfect static-analysis score | Pylint run on server | `final_project/evidence/8b_static_code_analysis.txt` | Local score 10.00/10; genuine course terminal capture pending |

## Completion gates

- The local test suite, syntax checks, dependency checks, and Pylint must pass.
- Obtain authentic Cloud IDE output for the three Watson sample statements and genuine deployment/error screenshots. Do not substitute mocked responses or generated scores.
- Have independent QA review the local branch, lineage, exact files, manifest, and evidence.
- Keep the repository unpublished until the user gives action-time publication approval. Keep course submission separate until separately authorized.
