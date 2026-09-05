# Sketch-to-3D Reconstruction

A PyTorch-based deep learning project that converts a 2D image or sketch into a 3D voxel representation.

## Project Overview

This project uses a CNN encoder-decoder architecture.

The input image is converted into an edge map, then passed through a 2D CNN encoder to extract important features.

These features are compressed into a 512-dimensional latent vector.

A 3D decoder then reconstructs the object as a 32×32×32 voxel grid.

## Pipeline

2D Image  
↓  
Grayscale Conversion  
↓  
Gaussian Blur  
↓  
Canny Edge Detection  
↓  
64×64 Edge Map  
↓  
2D CNN Encoder  
↓  
512-D Latent Vector  
↓  
3D Transposed CNN Decoder  
↓  
32×32×32 Voxel Reconstruction

## Supported Object Categories

The model was trained using ShapeNet objects from these categories:

- Chair
- Sofa
- Table
- Lamp
- Car
- Bench

## Model Architecture

### Encoder

The encoder uses multiple `Conv2d` layers to extract features from the 2D sketch.

Input:

```text
1 × 64 × 64

Feature extraction:

64×64
↓
32×32
↓
16×16
↓
8×8
↓
4×4

The extracted features are flattened and converted into a:

512-dimensional latent vector
Decoder

The decoder converts the latent vector into a 3D voxel representation using ConvTranspose3d layers.

512-D latent vector
↓
256 × 2 × 2 × 2
↓
4×4×4
↓
8×8×8
↓
16×16×16
↓
32×32×32

The final Sigmoid layer produces voxel occupancy probabilities between 0 and 1.

Technologies Used:
Python
PyTorch
OpenCV
NumPy
Matplotlib
SciPy
Google Colab
ShapeNet Dataset
Project Structure

Sketch-to-3D-Reconstruction/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── notebooks/
│   └── Sketch_to_3D.ipynb
│
├── src/
│   └── binvox_rw.py
│
├── results/
│   ├── voxel_visualization.png
│   └── all_voxels.png
│
└── checkpoints/

Results:

Example voxel reconstruction results are available inside the results/ folder.

Model Evaluation:

The model can be evaluated using:

Intersection over Union (IoU)
Dice Score
Voxel Accuracy

IoU and Dice are especially useful because they measure the overlap between the predicted 3D shape and the ground-truth voxel representation.

Running the Project:

Install the required libraries:

pip install -r requirements.txt

The notebook can be opened in Google Colab:

notebooks/Sketch_to_3D.ipynb

The ShapeNet render images and voxel files must be downloaded separately and configured in the notebook.

Trained Model:

The model was trained for 20 epochs.

The trained PyTorch checkpoint is stored separately because model files and datasets can be too large for a normal GitHub repository.