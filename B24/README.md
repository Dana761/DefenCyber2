# B24 – Design and Implement Access Control

## Objective
Design and implement an access control system to protect sensitive personal information using Google Drive permissions.

## Platform Used
- Google Drive

## Implementation
A role-based access control system was configured using Google Drive’s sharing and permission settings.

Permissions applied:
- Owner: full administrative access
- Editor: allowed to manage and modify files
- Other users: denied access unless explicitly permitted

The folder’s general access setting was configured to:
Restricted

This prevents unauthorized users from accessing files through public or shared links.

## Findings
- Access control policies were successfully enforced.
- Only authorized accounts could access the folder.
- Unauthorized users were blocked from viewing sensitive documents.
- The implementation demonstrates:
  - Confidentiality
  - Least privilege
  - Access enforcement

## Conclusion
This activity demonstrates how cloud-based access control mechanisms can be used to protect sensitive information. Proper permission management and restricted sharing settings significantly reduce the risk of unauthorized access and accidental data exposure.
