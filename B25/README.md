# B25 – Design and Implement a Threat Intelligence Module

## Objective
Design and implement a threat intelligence module that analyses IP reputation using real-world threat intelligence data.

## Tools Used
- Python
- requests library
- AbuseIPDB API
- Python virtual environment (venv)

## Implementation
A Python-based module was developed to query the AbuseIPDB API and analyse IP reputation data.

The system:
- Accepts an IP address as input
- Retrieves threat intelligence information from AbuseIPDB
- Displays:
  - Abuse confidence score
  - Number of reports
  - ISP
  - Country
- Classifies the IP as:
  - Safe
  - Suspicious
  - Malicious

A virtual environment was used to isolate dependencies and follow secure development practices.

## Findings
- The module successfully communicated with the AbuseIPDB API.
- Testing was performed using the IP address:
130.95.40.100

- Results showed:
  - ISP: University of Western Australia
  - Abuse Score: 0
  - Verdict: Safe

- The system correctly interpreted the threat intelligence data and generated an accurate verdict.

## Conclusion
This activity demonstrates how threat intelligence platforms can be integrated into security tools to automate risk analysis and support cybersecurity decision-making. The module successfully converts raw threat intelligence data into meaningful security information.
