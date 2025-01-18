## Sudoku Solver Web App

A web-based Sudoku Solver that allows users to upload images of Sudoku puzzles, extract the grid using OCR, and either solve the puzzle or receive hints for specific cells. Built using Python, Flask, OpenCV, and HTML/CSS.

## Features

- Upload images of Sudoku puzzles.
- Extract Sudoku grids from uploaded images using OCR.
- Solve the entire Sudoku puzzle.
- Provide hints for specific cells in the puzzle.
- Intuitive and user-friendly interface.
- Responsive design for various devices.

## Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Libraries/Tools**: OpenCV, NumPy, Jinja2, Tesseract OCR

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/aryantaffy/sudoku-solver.git
   cd sudoku-solver
   ```

2. **Set up a virtual environment** (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Tesseract OCR**:
   - Install [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) for your operating system.
   - Ensure `tesseract` is added to your system's PATH.

5. **Run the application**:
   ```bash
   python app.py
   ```

6. **Access the web app**:
   Open your browser and go to `http://127.0.0.1:8000`.

## File Structure

```
project/
├── app.py                  # Main Flask app
├── templates/
│   └── index.html          # HTML frontend
├── static/
│   ├── style.css           # CSS styling
│   ├── background.jpg      # Background image
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
```

## Usage

1. **Upload Puzzle**: Upload one or more images of Sudoku puzzles.
2. **Solve Puzzle**: View the solved puzzle or receive a hint for a specific cell.
3. **Manual Input**: In case the puzzle is not detected correctly, you can add numbers manually to the grid.
4. **Instructions**: Follow the on-screen instructions for a smooth experience.

## Dependencies

- Flask
- OpenCV
- NumPy
- Tesseract OCR
- Jinja2 (used for templating)
- Werkzeug (Flask dependency)
- JavaScript (client-side logic)

Install dependencies with:
```bash
pip install -r requirements.txt
```

## Future Enhancements

- Add support for handwritten Sudoku puzzles.
- Improve OCR accuracy with advanced pre-processing techniques.
- Add the ability to download solved puzzles.

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Commit your changes (`git commit -m "Add some feature"`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) for text recognition.
- [OpenCV](https://opencv.org/) for image preprocessing and manipulation.
- [Flask](https://flask.palletsprojects.com/) for building the backend.
- [NumPy](https://numpy.org/) for efficient numerical computation.
- [Render](https://render.com/) for hosting the application.
