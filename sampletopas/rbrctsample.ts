# RBRCT_Topas_Simulation.tps
# Simple TOPAS simulation for RBRCT project

s:Simulation/Title = "RBRCT Beam Steering Simulation"

# Define the World (simulation boundary)
s:Geometry/World/Material = "G4_AIR"
d:Geometry/World/Dimensions = 200 cm 200 cm 200 cm

# Define the phantom (breast tissue model)
s:Geometry/Phantom/Type = "Box"
s:Geometry/Phantom/Material = "G4_TISSUE_SOFT_ICRP"
d:Geometry/Phantom/Dimensions = 10 cm 10 cm 10 cm
d:Geometry/Phantom/Translation = 0 cm 0 cm 50 cm

# Define the Janus Sphere (if needed for steering simulation)
s:Geometry/JanusSphere/Type = "Sphere"
s:Geometry/JanusSphere/Material = "G4_WATER"
d:Geometry/JanusSphere/Radius = 1 cm
d:Geometry/JanusSphere/Translation = 0 cm 0 cm 20 cm

# Define the X-ray Beam
s:Beam/Type = "Gaussian"
s:Beam/Particle = "gamma"
d:Beam/MeanEnergy = 150 keV
d:Beam/SigmaEnergy = 0 keV
d:Beam/Position = 0 cm 0 cm -50 cm
d:Beam/Divergence = 0.5 deg 0.5 deg

# Setup scoring for dose and fluence
s:Scorer/DoseToWaterScorer/Quantity = "DoseToWater"
s:Scorer/DoseToWaterScorer/Component = "Phantom"
s:Scorer/DoseToWaterScorer/OutputType = "3D"
s:Scorer/DoseToWaterScorer/OutputFile = "RBRCT_DoseOutput"

s:Scorer/FluenceScorer/Quantity = "Fluence"
s:Scorer/FluenceScorer/Component = "JanusSphere"
s:Scorer/FluenceScorer/OutputType = "1D"
s:Scorer/FluenceScorer/OutputFile = "RBRCT_FluenceOutput"

# Run parameters
i:Simulation/NumberOfPrimaries = 1000000

# Visualization
s:Visualization/TopasGraphics/Type = "OpenGL"
b:Visualization/TopasGraphics/Enabled = "True"
d:Visualization/TopasGraphics/RefreshRate = 10 Hz

