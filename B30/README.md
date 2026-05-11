# B30 – AI Image Watermark Survival Test

## Objective
Generate an AI-created image, embed an imperceptible watermark, and test whether the watermark survives image modification.

## Tools Used
- Google Gemini
- Python
- Stegano library
- Pillow (PIL)

## Implementation
An AI-generated image was created using Google Gemini.

A hidden watermark was embedded into the image using the Least Significant Bit (LSB) steganography technique. Initial testing confirmed that the watermark could be successfully extracted from the modified image without affecting visual quality.

## Findings

### Initial Watermark Embedding
- The watermark was successfully embedded into the image.
- Extraction testing confirmed the hidden message could be recovered correctly.
- The image quality remained visually unchanged.

### Strong Transformation Test
- A stronger image modification process was applied.
- The watermark could no longer be extracted successfully.
- An extraction error occurred due to corruption of pixel-level data.

This demonstrates that LSB watermarking is vulnerable to major image transformations and AI-based regeneration.

### Controlled Modification Test
A second test used only minor image edits, including:
- Slight brightness adjustments
- Small overlays

Results:
- The watermark remained detectable after modification.
- The hidden data survived low-impact image processing.

## Conclusion
This activity demonstrates that LSB-based watermarking is effective for embedding hidden information into images, but it is fragile against major transformations. While the watermark failed after stronger modifications, it successfully survived controlled and minimal edits.
