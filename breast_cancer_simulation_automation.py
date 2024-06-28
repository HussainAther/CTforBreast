import os
import subprocess
import numpy as np

def create_topas_input_file(filename):
    with open(filename, 'w') as file:
        file.write("# TOPAS Input File for Comprehensive Breast Cancer CT Simulation\n")
        file.write("# Author: Syed Hussain Ather\n")
        file.write("# Date: 06/24/2024\n\n")
        
        file.write("# Define the Phantom Geometry (Breast Phantom)\n")
        file.write("s:Phantom.Name = \"BreastPhantom\"\n")
        file.write("s:Phantom.Material = \"G4_BREAST_ICRP\"\n")
        file.write("s:Phantom.Size = \"256 256 256 mm\"\n")
        file.write("s:Phantom.VoxelMaterial = \"G4_BREAST_ICRP\"\n")
        file.write("s:Phantom.VoxelDataFile = \"BreastPhantom.raw\"\n")
        file.write("s:Phantom.VoxelDataType = \"float\"\n")
        file.write("s:Phantom.VoxelGridSize = \"256 256 256\"\n\n")
        
        file.write("# Define the X-ray Source\n")
        file.write("s:Source.Type = \"Beam\"\n")
        file.write("s:Source.ParticleType = \"xray\"\n")
        file.write("s:Source.Energy = \"50 keV\"\n")
        file.write("s:Source.Position = \"0 0 -300 mm\"\n")
        file.write("s:Source.Direction = \"0 0 1\"\n")
        file.write("s:Source.BeamSpread = \"0 0\"\n\n")
        
        file.write("# Define the Detector\n")
        file.write("s:Detector.Type = \"SimpleDetector\"\n")
        file.write("s:Detector.Material = \"G4_WATER\"\n")
        file.write("s:Detector.Size = \"256 256 1 mm\"\n")
        file.write("s:Detector.Bins = \"256 256 1\"\n")
        file.write("s:Detector.Position = \"0 0 300 mm\"\n")
        file.write("s:Detector.OutputFile = \"breast_projections.txt\"\n\n")
        
        file.write("# Define the rotation for CT imaging\n")
        file.write("s:Rotation.NumberOfRotations = 360\n")
        file.write("s:Rotation.AngleIncrement = 1 degree\n\n")
        
        file.write("# Define the Simulation World\n")
        file.write("s:World.PhantomMaterial = \"G4_AIR\"\n")
        file.write("s:World.PhantomSize = \"512 512 512 mm\"\n")
        file.write("s:World.BeamMaterial = \"G4_AIR\"\n")
        file.write("s:World.BeamSize = \"512 512 512 mm\"\n\n")
        
        file.write("# Run Parameters\n")
        file.write("s:Run.NumberOfHistories = 1000000\n\n")
        
        file.write("# Output Control\n")
        file.write("s:Output.FileName = \"BreastCancerCTOutput.root\"\n")
        file.write("s:Output.Format = \"root\"\n")
        file.write("s:Output.Verbose = \"1\"\n")
        file.write("s:Output.FileExtension = \".root\"\n\n")
        
        file.write("# Define Visualization (Optional)\n")
        file.write("s:VisualizationEngine = \"Geant4\"\n")
        file.write("s:VisualizationOptions = \"OGL\"\n\n")
        
        file.write("# Additional Parameters for More Accurate Simulation\n")
        file.write("s:PhysicsList = \"QGSP_BIC_EMY\"\n")
        file.write("s:RangeCut = \"0.01 mm\"\n\n")
        
        file.write("# Define the scanning geometry\n")
        file.write("s:Scan.Axis = \"y\"\n")
        file.write("s:Scan.RotationAngleStart = \"0 degree\"\n")
        file.write("s:Scan.RotationAngleStop = \"360 degree\"\n")
        file.write("s:Scan.RotationAngleStep = \"1 degree\"\n\n")
        
        file.write("# Materials Definition\n")
        file.write("s:MaterialBreastDensity = \"1.02 g/cm3\"\n")
        file.write("s:MaterialWaterDensity = \"1.0 g/cm3\"\n")

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
    input_filename = "BreastCancerCTSimulation.txt"
    create_topas_input_file(input_filename)
    run_topas_simulation(input_filename)
    projections = load_projections("breast_projections.txt")
    
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

