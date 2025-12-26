# Handwriting_Calculator

A handwriting-based engineering calculator that converts handwritten math into LaTeX and evaluates it automatically.
Users can write equations on a tablet canvas or upload a photo of handwritten formulas from paper.

## Why this project?
Engineering courses often require expressions that are unrealistic to compute mentally or by manual calculation.
Since tablets are widely used for lectures, note-taking, and assignments, integrating a handwriting-to-math calculator into a familiar IT device can significantly reduce the time spent rewriting equations with buttons or keyboard-only input.

### Social value
- Faster problem solving by writing formulas naturally (as you would on paper)
- Works with both:
  - Tablet handwriting input
  - Photo upload (paper → camera → image)

### Technical / industrial value
Traditional scientific calculators require strict input order and familiarity with many function keys.
Handwriting is more natural for:
- fractions, parentheses, roots, exponents
- editing expressions without deleting everything (common in basic calculator UIs)

This project aims to make engineering calculations more intuitive by accepting “human-style” math writing.

## Project Goals
### Core pipeline
1. Extract text from a handwritten equation image using **Mathpix API**
2. Convert the extracted result into **LaTeX**
3. Parse LaTeX into a computable form using **latex2sympy2**
4. Evaluate the expression using **SymPy** and return the result

> **Mathpix API**: OCR service specialized for math recognition  
> **latex2sympy2**: Converts LaTeX into SymPy expressions  
> **LaTeX**: Typesetting system widely used to represent mathematical expressions

### Qualitative goals
- Build a user-friendly GUI
- Keep the codebase maintainable and extensible

### Quantitative goals
- Achieve **≥ 80% character recognition accuracy**
- Support recognition & calculation for:
  - calculus (derivatives/integrals), series, limits
  - trigonometric functions
  - square roots, exponents
- Provide multiple input methods:
  - image upload
  - handwriting drawing canvas
  - keyboard input
- Display the converted LaTeX expression before evaluation

## Features
- Handwriting input (draw on canvas)
- Image upload (photo of handwritten formulas)
- LaTeX output preview
- One-click evaluation
- Error handling with user-friendly messages
- Developed and tested on Ubuntu

## Tech Stack
- **Python**
- **Ubuntu**
- **Mathpix API**
- **SymPy**
- **latex2sympy2**
- GUI: (fill in your GUI framework, e.g., PyQt5 / Tkinter / etc.)

## Setup
### 1) Environment
- Install **Ubuntu**
- Install **VS Code**
- Set up Python environment (recommended: virtual environment)

### 2) Dependencies
Install required libraries:
- `sympy`
- `latex2sympy2`
- (your GUI libs)
- (http libs like `requests` if used for API calls)

### 3) Mathpix API Key
Create a Mathpix account and issue an API key.
Set it as an environment variable or configure it in a local config file (do not commit keys to GitHub).

Example (recommended):
- `MATHPIX_APP_ID`
- `MATHPIX_APP_KEY`

## Usage
1. Choose one input method:
   - Upload an image
   - Write on the canvas
   - Type using keyboard
2. Submit the input
3. Check the generated LaTeX expression
4. Click **Calculate** to get the final result

## Problems Encountered & Fixes
- **Mathpix output format mismatch**:
  - Added a conversion function to translate Mathpix-style LaTeX into a format suitable for evaluation.
- **Ubuntu disk space issue (boot failure)**:
  - Entered recovery mode and removed unnecessary files to restore the system.

## Results / Achievements
- Implemented an end-to-end pipeline:
  - handwriting input → OCR → LaTeX → parsing → evaluation
- Improved usability through a simple and intuitive UI
- Integrated external API (Mathpix) and math libraries (SymPy ecosystem)
- Added exception handling for stability
- Built and tested in Ubuntu-based development environment

## Future Work
- Add advanced features:
  - matrices
  - Laplace transforms
- Improve keyboard input:
  - provide math symbol buttons (sin/cos, integral, derivative, limit, etc.) instead of forcing LaTeX typing
- Add more input options:
  - camera capture
  - screenshot / clipboard image paste
  - direct import from drawing apps
- Optimize recognition and evaluation speed
- Refine UI based on user feedback

## Acknowledgements
- Mathpix for OCR API
- SymPy and latex2sympy2 communities
