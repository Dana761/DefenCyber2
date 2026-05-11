# B17 — Implement One State-of-the-Art Solution and Evaluate It

## Chosen Solution
Multi-Factor Authentication (MFA) and Passkey-Based Authentication using Google Account Security

## Implementation
I implemented a modern authentication system by enabling:
- Google 2-Step Verification (MFA)  
- Authenticator app verification codes  
- Passkey-based passwordless authentication  
- Google prompts and backup codes  

The system also included recovery methods such as recovery email and phone verification.

## Evaluation
The implementation significantly improved account security by requiring multiple forms of authentication before access is granted.

### Strengths
- Strong protection against unauthorized access  
- Resistant to phishing and credential theft  
- Passkeys reduce reliance on traditional passwords  
- Multiple backup methods improve account recovery  
- Easy to configure and integrate with Google services  

### Limitations
- Users may lose access if authentication devices are unavailable  
- Backup methods must be managed carefully  
- Some users may find MFA less convenient during login  

## Key Findings
- MFA greatly improves account protection even if passwords are compromised  
- Passkeys represent a modern and secure authentication approach  
- Passwordless authentication reduces phishing risks  
- Backup and recovery mechanisms are essential for usability and reliability  

## Evidence
- Screenshot showing 2-Step Verification enabled  
- Screenshot showing authenticator setup  
- Screenshot showing passkeys enabled  
- Screenshot of security settings with multiple authentication methods
