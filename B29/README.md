# B29 – CVE Analysis Using Generative AI

## Selected CVE
CVE-2026-25049

## Affected System
n8n (workflow automation platform)

## Vulnerability Description
CVE-2026-25049 is a critical sandbox escape vulnerability in n8n that can lead to Remote Code Execution (RCE). Attackers can craft malicious workflow expressions to bypass security protections and execute arbitrary commands on the host system.

## Potential Impact
- Full server compromise
- Arbitrary command execution
- Exposure of sensitive data and credentials
- Possible lateral movement within connected systems

## AI Tool Comparison

### Gemini
Findings:
- Produced an unrelated explanation about JWT algorithm confusion.
- Did not correctly identify the selected CVE.

Accuracy: Low

### Claude
Findings:
- Correctly identified the vulnerability as an n8n sandbox escape.
- Explained AST protection bypass and Remote Code Execution.
- Provided detailed mitigation recommendations.

Accuracy: High

### Perplexity
Findings:
- Correctly explained the sandbox escape vulnerability.
- Provided concise technical details and mitigation advice.
- Included references to external security sources.

Accuracy: High

## Comparison Summary

| Criteria | Gemini | Claude | Perplexity |
|---|---|---|---|
| Accuracy | Low | High | High |
| Relevance | Incorrect CVE | High | High |
| Detail Level | Medium | High | Medium |
| Fix Quality | Generic | Very Good | Good |

## Key Observation
The activity demonstrated that generative AI systems can sometimes produce confident but incorrect cybersecurity explanations. Claude and Perplexity correctly identified the vulnerability, while Gemini generated unrelated information.

This highlights the importance of validating AI-generated cybersecurity content using trusted security sources.

## Conclusion
Claude provided the most detailed and accurate explanation of CVE-2026-25049, while Perplexity also produced reliable results. Gemini failed to correctly identify the vulnerability, showing that AI outputs should always be cross-checked before being trusted in cybersecurity analysis.
