# B3 — Proactive Security Implementations in Practice

## 1. Device Verification — GitHub

### Description
GitHub uses device verification when a login attempt is detected from a new or unknown device.

### How It Works
- User enters username and password  
- GitHub detects a new device/login attempt  
- Verification code is sent to the registered email  
- Access is granted only after verification  

### Why It Is Proactive
Prevents unauthorized access before the attacker can enter the account, even if the password is compromised.

### Threats Prevented
- Account takeover  
- Credential theft  
- Unauthorized device access  

### Type of Security
Authentication Security (Multi-Factor Authentication)

---

## 2. Bot Prevention — reCAPTCHA in Call of Duty: Mobile

### Description
Call of Duty: Mobile uses reCAPTCHA to verify that login attempts are performed by humans instead of automated bots.

### How It Works
- User completes “I’m not a robot” verification  
- System analyzes user behavior  
- Additional verification may appear if suspicious activity is detected  

### Why It Is Proactive
Stops automated attacks before they can interact with the system.

### Threats Prevented
- Brute-force attacks  
- Bot abuse  
- Automated account farming  

### Type of Security
Bot Prevention / Abuse Prevention

---

## 3. Security Headers — Komdigi Website

### Description
The Komdigi website implements security headers such as CSP, HSTS, X-Frame-Options, and X-Content-Type-Options.

### How It Works
- CSP restricts malicious scripts/resources  
- HSTS forces secure HTTPS connections  
- X-Frame-Options prevents clickjacking  
- X-Content-Type-Options prevents MIME sniffing  

### Why It Is Proactive
The browser blocks malicious behavior before attacks can execute.

### Threats Prevented
- Cross-site scripting (XSS)  
- Clickjacking  
- Man-in-the-Middle attacks  
- Content-type spoofing  

### Type of Security
Browser / Network Security
