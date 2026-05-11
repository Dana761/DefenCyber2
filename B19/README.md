# B19 — Find and Fix a Vulnerability from a GitHub Project

## Vulnerability Identified
- **Risk Level:** Medium  
- **Project:** Ustad’s Adventure Game Project  
- **Repository:**  
  https://github.com/Dana761/Game-Project  

## Description
A vulnerability related to uncontrolled resource usage was identified in the shooting system. The player could continuously generate bullets without any cooldown or restriction, causing unlimited object creation.

Each key press immediately created a new bullet object and added it to memory without rate limiting.

## Impact
- Increased memory and CPU usage  
- Potential game lag or freezing  
- Risk of application instability or crashes  
- Resource exhaustion similar to a local denial-of-service condition  

## Recommendation
- Implement input rate limiting for shooting actions  
- Add a cooldown mechanism to restrict bullet generation frequency  
- Control resource creation to improve stability and performance  

## Fix Implemented
A shooting cooldown system was added to the `Player` class.

### Changes Made
- Added timestamp tracking for the last shot fired  
- Implemented cooldown timing between shots  
- Prevented bullet creation before cooldown expiration  

This ensured that shooting actions became rate-limited and resource usage remained controlled.

## Evaluation
After implementing the cooldown mechanism:
- Bullet generation became stable and controlled  
- Excessive object creation was prevented  
- Overall game performance improved  
- The game continued functioning normally after testing  

## Evidence
- Screenshot of original shooting logic without cooldown  
- Screenshot of updated cooldown variables  
- Screenshot of updated `set_shooting()` function  
- Screenshot of successful game execution after fix  
- GitHub repository containing implemented changes
