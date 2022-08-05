# Tiralabra - University of Helsinki
This repository contains the algorithm project for the course Data Structures Lab (Summer 2022), University of Helsinki. The project contains an artificial solver for the famous puzzle, the Fifteen Puzzle. The solver uses IDA* as the algorithm with two different heuristics: Manhattan-distance and Hamming-distance.

## Documentation
[Project Specification Document](./documentation/project_specification.md)<br>
[Testing Document](./documentation/testing_document.md)<br>

### Weekly Reports
[Week 1 Report](./documentation/weekly_reports/week1_report.md)<br>
[Week 2 Report](./documentation/weekly_reports/week2_report.md)<br>
[Week 3 Report](./documentation/weekly_reports/week3_report.md)<br>

### Test Coverages
[Test Coverages](./documentation/test_coverages.md)

## Commands
To run the program, use the following command when in root of the repository:
```console
python src/main.py
```

To test the program, run the following command when in root of the repository:
```console
pytest src
```

To get the test coverage, run the following command when in root of the repository:
```console
coverage run --branch -m pytest src
```

To get a test coverage report, run the following command after getting the test coverage when in root of the repository:
```console
coverage html
```