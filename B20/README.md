# B20 — Enhance the Security of a GitHub Project

## Project
- **Repository:**  
  https://github.com/Dana761/Game-Project  

- **Risk Level:** Medium  

## Description
The original game project loaded image and sound assets directly from file paths without validating the file type or checking whether the file existed.

This introduced several security and stability risks:
- Loading unsupported or unintended file types  
- Application crashes caused by invalid paths  
- Reduced reliability when handling external resources  

To improve security, a secure asset validation system was implemented using a helper function named `safe_asset_path()`.

## Security Enhancement Implemented

### Features Added
- Validation of allowed file extensions  
- File existence checking before loading  
- Controlled asset access through helper functions  

### Allowed Asset Types
Examples:
- `.png`  
- `.mp3`  
- `.wav`  

## Impact
Before enhancement:
- Invalid or missing files could crash the game  
- Any filename could be processed without restriction  
- Asset handling lacked robustness  

After enhancement:
- Only approved file types are accepted  
- Missing files are detected early  
- Clear error handling improves debugging  
- Overall application stability is improved  

## Recommendation
- Always validate external inputs and file paths  
- Restrict accepted file extensions  
- Verify file existence before processing  
- Use centralized helper functions for asset loading  
- Add exception handling and logging for future improvements  

## Evidence
- Implementation of `safe_asset_path()` validation function  
- Updated `load_sound()` using validated asset paths  
- GitHub repository update containing security improvements  
- Screenshots showing:
  - Code before enhancement  
  - Code after enhancement  
  - Successful game execution after implementation
