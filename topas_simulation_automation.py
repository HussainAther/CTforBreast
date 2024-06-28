import os
import numpy as np
import subprocess

def create_topas_input_file(filename):
    with open(filename, 'w') as file:
        file.write("# TOPAS Input File for Shepp-Logan Phantom Imaging\n")
        file.write("# Author: Syed Hussain Ather\n")
        file.write("# Date: 06/24/2024\n\n")
        
        file.write("# Define the Phantom Geometry\n")
        file.write("s:Phantom.Name = \"SheppLoganPhantom\"\n")
        file.write("s:Phantom.Material = \"Water\"\n")
        file.write("s:Phantom.Size = \"256 256 256 mm\"\n")
        file.write("s:Phantom.VoxelMaterial = \"Water\"\n")
        file.write("s:Phantom.VoxelDataFile = \"SheppLoganPhantom.raw\"\n")
        file.write("s:Phantom.VoxelDataType = \"float\"\n")
        file.write("s:Phantom.VoxelGridSize = \"256 256 256\"\n\n")
        
        file.write("# Define the X-ray Source\n")
        file.write("s:Source.Type = \"Beam\"\n")
        file.write("s:Source.ParticleType = \"xray\"\n")
        file.write("s:Source.Energy = \"100 keV\"\n")
        file.write("s:Source.Position = \"0 0 -300 mm\"\n")
        file.write("s:Source.Direction = \"0 0 1\"\n")
        file.write("s:Source.BeamSpread = \"0 0\"\n\n")
        
        file.write("# Define the Detector\n")
        file.write("s:Detector.Type = \"SimpleDetector\"\n")
        file.write("s:Detector.Material = \"G4_WATER\"\n")
        file.write("s:Detector.Size = \"256 256 1 mm\"\n")
        file.write("s:Detector.Bins = \"256 256 1\"\n")
        file.write("s:Detector.Position = \"0 0 300 mm\"\n")
        file.write("s:Detector.OutputFile = \"projections.txt\"\n\n")
        
        file.write("# Run Parameters\n")
        file.write("s:Run.NumberOfHistories = 1000000\n")

def run_topas_simulation(input_filename):
    result = subprocess.run(["topas", input_filename], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print("Error running TOPAS simulation:", result.stderr)
    else:
        print("TOPAS simulation completed successfully.")

def load_projections(filename):
    return np.loadtxt(filename)

def main():
    input_filename = "SheppLoganImaging.txt"
    create_topas_input_file(input_filename)
    run_topas_simulation(input_filename)
    projections = load_projections("projections.txt")
    
    # Further processing and reconstruction can be done here
    # For example, using your ReconstructionModule
    # recon = ReconstructionModule()
    # recon.set_projections(projections)
    # reconstructed_image = recon.ART(iterations=50)
    
    # Visualization
    # viz = VisualizationModule()
    # viz.plot_2d(reconstructed_image, title="ART Reconstruction")

if __name__ == "__main__":
    main()

