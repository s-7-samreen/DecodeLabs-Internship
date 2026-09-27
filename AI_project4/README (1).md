# Project 4: Image / Text Recognition (Basic)

**DecodeLabs Internship — Industrial Training Kit (AI Track)**

## Description

This project implements a basic **text recognition (OCR)** system using a pre-trained OCR engine. The script takes a sample image containing text, pre-processes it, extracts the text using the OCR model, benchmarks the recognition accuracy, and generates a visual output showing exactly which words were detected and where.

**What it does, step by step:**

1. **Loads** a sample image (`sample.jpg`) from the project folder.
2. **Pre-processes** the image using OpenCV:
   - Converts it to **grayscale**
   - Applies **Adaptive Thresholding** to separate the text (foreground) from background noise
3. **Runs OCR** on the pre-processed image using **pytesseract** (a Python wrapper for the Tesseract OCR engine) to extract all recognizable text.
4. **Benchmarks accuracy** by calculating the average confidence score across all detected words, and checks whether it meets the minimum required threshold of **80%**.
5. **Generates a visual output** (`output_annotated.jpg`) — a copy of the original image with a green bounding box and red text label drawn around every recognized word, so the recognition can be visually verified.

## Libraries Used

- `pytesseract` — pre-trained OCR engine wrapper (Library Integration)
- `opencv-python (cv2)` — image loading, grayscale conversion, adaptive thresholding, and drawing bounding boxes
- Tesseract OCR engine (installed separately on the system)

## Project Files

| File                     | Purpose                                             |
|--------------------------|------------------------------------------------------|
| `text_recognizer.py`     | Main script — runs the full recognition pipeline     |
| `sample.jpg`             | Input image containing text to be recognized         |
| `output_annotated.jpg`   | Output image with bounding boxes (generated on run)   |

## How to Run

**Requirements (one-time setup):**

```
python -m pip install pytesseract pillow opencv-python
```

Also install the Tesseract OCR engine itself (not a Python package) from:
https://github.com/UB-Mannheim/tesseract/wiki

**Steps to run:**

1. Place `sample.jpg` (any image containing readable text) in the same folder as `text_recognizer.py`.
2. Open Command Prompt in that folder.
3. Run:
   ```
   python text_recognizer.py
   ```
4. The terminal will display:
   - The recognized text
   - The average confidence score
   - Whether the accuracy benchmark passed (≥ 80%)
5. Check the newly generated `output_annotated.jpg` in the same folder to see the visual bounding-box confirmation.

## Result

- **Average Confidence Score:** 82.91%
- **Accuracy Benchmark:** PASS (≥ 80%)
- **Visual Confirmation:** Generated successfully (`output_annotated.jpg`)
