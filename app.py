from flask import Flask, request, jsonify, render_template
from flask_cors import CORS # type: ignore
import os
import cv2 # type: ignore
import numpy as np # type: ignore

app = Flask(__name__, static_folder="static")
CORS(app)

# Sudoku Solver Utilities
def solve_sudoku(grid):
    """Solve a given Sudoku grid."""
    def is_valid(num, row, col):
        """Check if placing num in grid[row][col] is valid."""
        for i in range(9):
            if grid[row][i] == num or grid[i][col] == num:
                return False
            box_row, box_col = 3 * (row // 3), 3 * (col // 3)
            if grid[box_row + i // 3][box_col + i % 3] == num:
                return False
        return True

    def backtrack():
        """Recursive backtracking solver."""
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    for num in range(1, 10):
                        if is_valid(num, i, j):
                            grid[i][j] = num
                            if backtrack():
                                return True
                            grid[i][j] = 0
                    return False
        return True

    return backtrack()


def preprocess_image(image):
    """Preprocess image to improve OCR accuracy."""
    blur = cv2.GaussianBlur(image, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 128, 255, cv2.THRESH_BINARY_INV)
    return thresh


def perform_ocr(image):
    """Dummy OCR function for Sudoku extraction."""
    # Replace this with actual OCR logic or third-party library
    return [[0] * 9 for _ in range(9)]


@app.route("/")
def index():
    """Serve the main application page."""
    return render_template("index.html")


@app.route("/extract", methods=["POST"])
def extract_puzzle():
    """Extract Sudoku grid from uploaded images."""
    if "files" not in request.files:
        return jsonify({"error": "No files provided"}), 400

    files = request.files.getlist("files")
    grids = []

    for file in files:
        try:
            file_path = os.path.join("uploads", file.filename)
            file.save(file_path)

            # Process the image and extract the Sudoku grid
            image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
            preprocessed_image = preprocess_image(image)
            grid = perform_ocr(preprocessed_image)
            grids.append(grid)
        except Exception as e:
            return jsonify({"error": f"Failed to process file {file.filename}: {str(e)}"}), 500

    if not grids:
        return jsonify({"error": "No grids were successfully processed."}), 400

    # Combine the grids into one final grid (dummy logic for now)
    combined_grid = grids[0]

    return jsonify({"grid": combined_grid})


@app.route("/solve", methods=["POST"])
def solve():
    """Solve or provide a hint for the Sudoku puzzle."""
    data = request.json
    grid = data.get("grid")
    mode = data.get("mode")  # "solve" or "hint"
    cell = data.get("cell")  # {"row": int, "col": int} for hint mode

    if not grid:
        return jsonify({"error": "Grid not provided"}), 400

    solved_grid = [row[:] for row in grid]  # Make a copy of the grid

    if not solve_sudoku(solved_grid):
        return jsonify({"error": "Sudoku puzzle could not be solved"}), 400

    if mode == "solve":
        return jsonify({"solved_grid": solved_grid})
    elif mode == "hint":
        if cell and 0 <= cell["row"] < 9 and 0 <= cell["col"] < 9:
            row, col = cell["row"], cell["col"]
            if grid[row][col] == 0:  # Ensure it's an empty cell
                return jsonify({"hint": solved_grid[row][col]})
            else:
                return jsonify({"error": "Cell already filled"}), 400
        else:
            return jsonify({"error": "Invalid cell coordinates"}), 400
    else:
        return jsonify({"error": "Invalid mode specified"}), 400


if __name__ == "__main__":
    os.makedirs("uploads", exist_ok=True)
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))