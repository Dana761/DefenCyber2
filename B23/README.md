# B23 – Testing an Intrusion Detection System (IDS)

## Objective
Test the effectiveness of the Suricata Intrusion Detection System (IDS) in detecting suspicious network activity on Kali Linux.

## Tools Used
- Kali Linux
- Suricata IDS
- curl
- Suricata default rule set

## Steps Performed
1. Installed and configured Suricata on Kali Linux.
2. Ran Suricata on the eth0 network interface using the default configuration.
3. Generated test traffic using:
curl http://testmyids.com

4. Reviewed alerts generated in:
/var/log/suricata/fast.log

## Findings

### Finding 1 – Successful Deployment of Suricata IDS
- Suricata was successfully installed and executed in IDS mode.
- Real-time traffic monitoring functioned correctly.
- A kernel-related AF_PACKET fanout warning appeared but did not stop detection capabilities.

Risk Level: Low

### Finding 2 – Detection of Suspicious Traffic
- Suricata detected the generated HTTP request and created alerts in fast.log.
- Alert detected:
GPL ATTACK_RESPONSE id check returned root

- The traffic was categorized as “Potentially Bad Traffic” with Priority 2.

Risk Level: Medium

## Conclusion
The testing confirmed that Suricata IDS is effective in monitoring traffic and detecting suspicious activity using its rule-based detection engine. Regular rule updates and integration with centralized monitoring systems can further improve detection and response capabilities.
