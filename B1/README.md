# B1 — Weak / Vulnerable Security Implementations

## Finding 1 — Unauthorized Access to Course Content
- **Target:** Etarnus Learning Platform  
- **Category:** Access Control Weakness  
- **Risk Level:** High  

### Description
Certain courses could be accessed without requiring an enrollment key, showing weak access control enforcement.

### Impact
- Unauthorized access to restricted content  
- Possible exposure of internal educational materials  
- Weak authorization management  

### Recommendation
- Enforce enrollment key validation  
- Implement proper authentication and authorization checks  

---

## Finding 2 — Access Retention After Role Change
- **Target:** Etarnus Learning Platform  
- **Category:** Access Control Weakness  
- **Risk Level:** High  

### Description
Inactive or alumni accounts still retained access to the platform and course resources.

### Impact
- Unauthorized continued access  
- Increased risk of data exposure  
- Poor account lifecycle management  

### Recommendation
- Apply role-based access control (RBAC)  
- Automatically revoke inactive accounts  

---

## Finding 3 — Improper TLS/SSL Configuration
- **Target:** Film Streaming Website  
- **Category:** Network and Transport Security  
- **Risk Level:** High  

### Description
The website used an invalid/self-signed SSL certificate and displayed a “Not Secure” warning.

### Impact
- Risk of Man-in-the-Middle (MITM) attacks  
- Untrusted server identity  
- Insecure communication channel  

### Recommendation
- Use a trusted Certificate Authority (CA)  
- Configure HTTPS correctly  
- Ensure certificate matches the domain  

---

## Finding 4 — CAPTCHA Reuse After Failed Authentication
- **Target:** PoliceTube Login System  
- **Category:** Authentication Security  
- **Risk Level:** Medium  

### Description
The CAPTCHA remained unchanged after failed username/password attempts, allowing reuse across multiple login attempts.

### Impact
- Reduced CAPTCHA effectiveness  
- Easier brute force attempts  
- Weak anti-bot protection  

### Recommendation
- Regenerate CAPTCHA after every login attempt  
- Add rate limiting and temporary lockout mechanisms  

---

## Finding 5 — Information Disclosure via Response Headers
- **Target:** SMPN 1 Probolinggo Website  
- **Category:** Information Disclosure  
- **Risk Level:** Medium  

### Description
HTTP response headers exposed backend technology information.

### Impact
- Easier reconnaissance for attackers  
- Increased exposure to known vulnerabilities  

### Recommendation
- Remove sensitive headers  
- Disable `X-Powered-By`  
- Hide server version information  
