"""
Project 4: Image or Text Recognition (Basic)
DecodeLabs Internship - Industrial Training Kit

Gatekeeper Rule compliance:
1. Library Integration       -> pytesseract (OCR engine wrapper)
2. Pre-Processing Integrity  -> Grayscale + Adaptive Thresholding (OpenCV)
3. Accuracy Benchmarking     -> Minimum validated confidence score of 80%
4. Visual Confirmation       -> Annotated output image with bounding boxes + labels
"""

import cv2
import pytesseract
import os
import sys

# If tesseract is not in PATH, uncomment and set the correct path:
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

INPUT_IMAGE = "sample.jpg"
OUTPUT_IMAGE = "output_annotated.jpg"
CONFIDENCE_THRESHOLD = 80.0


def load_image(path):
    """Step 1: Load the image from disk."""
    if not os.path.exists(path):
        print(f"Error: File not found -> {path}")
        sys.exit(1)
    image = cv2.imread(path)
    if image is None:
        print(f"Error: Could not read image -> {path}")
        sys.exit(1)
    return image


def preprocess_image(image):
    """
    Step 2: Pre-Processing Integrity requirement.
    - Convert to grayscale (removes color noise, simplifies to intensity values)
    - Apply Adaptive Thresholding (separates text/foreground from background/noise,
      works better than a fixed threshold under uneven lighting)
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    thresholded = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        blockSize=31,
        C=15,
    )
    return gray, thresholded


def run_ocr(preprocessed_image):
    """
    Step 3: Library Integration requirement.
    Run pytesseract (pre-trained OCR model) on the pre-processed image,
    returning both the text and per-word confidence/bounding box data.
    """
    data = pytesseract.image_to_data(
        preprocessed_image, output_type=pytesseract.Output.DICT
    )
    return data


def compute_average_confidence(data):
    """
    Step 4: Accuracy Benchmarking requirement.
    Compute the average confidence across all detected words (ignoring -1 = no text).
    """
    confidences = [int(c) for c in data["conf"] if c not in ("-1", -1)]
    if not confidences:
        return 0.0
    return sum(confidences) / len(confidences)


def draw_annotations(original_image, data, min_word_conf=40):
    """
    Step 5: Visual Confirmation requirement.
    Draw bounding boxes + recognized word labels on a copy of the original image.
    Only draws boxes for words above a low per-word confidence floor, so junk/noise
    boxes don't clutter the output.
    """
    annotated = original_image.copy()
    n_boxes = len(data["text"])

    for i in range(n_boxes):
        word = data["text"][i].strip()
        try:
            conf = int(data["conf"][i])
        except ValueError:
            conf = -1

        if word and conf >= min_word_conf:
            (x, y, w, h) = (
                data["left"][i],
                data["top"][i],
                data["width"][i],
                data["height"][i],
            )
            cv2.rectangle(annotated, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(
                annotated,
                word,
                (x, max(y - 5, 10)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 0, 255),
                1,
                cv2.LINE_AA,
            )
    return annotated


def display_output(text, confidence, output_path):
    """Print a clean, readable summary of the run."""
    print("=" * 55)
    print("   TEXT RECOGNITION RESULT")
    print("=" * 55)
    print("\nRecognized Text:\n")
    print(text if text.strip() else "(No text detected)")
    print("\n" + "-" * 55)
    print(f"Average Confidence Score : {confidence:.2f}%")
    status = "PASS (>= 80%)" if confidence >= CONFIDENCE_THRESHOLD else "BELOW THRESHOLD (< 80%)"
    print(f"Accuracy Benchmark       : {status}")
    print(f"Annotated Image Saved To : {output_path}")
    print("=" * 55)


def main():
    print(f"Loading image: {INPUT_IMAGE}")
    original = load_image(INPUT_IMAGE)

    print("Pre-processing (grayscale + adaptive thresholding)...")
    gray, thresholded = preprocess_image(original)

    print("Running OCR model (pytesseract)...")
    data = run_ocr(thresholded)
    recognized_text = " ".join(w for w in data["text"] if w.strip())

    confidence = compute_average_confidence(data)

    print("Drawing bounding boxes for visual confirmation...")
    annotated = draw_annotations(original, data)
    cv2.imwrite(OUTPUT_IMAGE, annotated)

    display_output(recognized_text, confidence, OUTPUT_IMAGE)


if __name__ == "__main__":
    main()
