"""
This module provides a pipeline for processing image files and generating annotated images.

The pipeline consists of the following steps:
1. Extract the grid from the input image
2. Generate a matrix representation of the grid
3. Solve the grid problem using an external algorithm
4. Visualize the solution on the input image

The module can be executed from the command line, and it expects the path to the input image file as an argument.
"""

import os
from typing import Tuple

from data_preprocessing import GridExtractor, MatrixGenerator
from image_annotation import Visualizer


def process_image(image_path: str) -> None:
    """
    Process the given image file and generate an annotated image with the solution.

    Args:
        image_path (str): The path to the input image file.

    Raises:
        Exception: If an error occurs during the processing pipeline.
    """
    try:
        print(f"Processing {image_path}")
        image_name, image_ext = os.path.splitext(os.path.basename(image_path))
        # Extract the grid from the input image
        grid_extractor = GridExtractor(image_path)
        extracted_grid = grid_extractor.extract_grid()
        grid_extractor.save_grid(extracted_grid)

        # Generate the matrix representation of the grid
        matrix_generator = MatrixGenerator(image_path)
        color_dataset, num_rows, num_cols, output_path = matrix_generator.save_matrix(
            extracted_grid
        )
        backtracking_cmd = "./operations/solution_algorithm/a.out " + output_path
        # Solve the grid problem using an external algorithm
        print(f"Running backtracking {backtracking_cmd}")
        os.system(backtracking_cmd)
        print("Completed solution")
        # Visualize the solution on the input image
        visualizer = Visualizer(
            color_dataset, extracted_grid, num_rows, num_cols, image_path
        )
        visualizer.display_output()
        updated_image_path = os.path.join(
            os.path.dirname(image_path), f"output{image_ext}"
        )
        visualizer.save_image(updated_image_path)

    except Exception as e:
        print(f"Error faced: {e}")


if __name__ == "__main__":
    path = os.path.join(os.getcwd(), "images")
    imgPath = os.path.join(path, "input.jpg")
    process_image(imgPath)
