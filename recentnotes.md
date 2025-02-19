🚀 Recent Updates & Improvements (Last 6 Months)

1️⃣ Fan Beam & Random Rays - Experimental Testing

Implemented Wu's Antialiasing Algorithm to improve line approximations in simulated rays.

Developed a framework for random rays and fan beam ray sampling.

Introduced 360° fan beam rotation to improve ray coverage and reduce artifacts.

Adjusted ray spread and density to improve reconstruction stability.

Debugged vertical streaking artifacts in fan beam reconstructions, applying adaptive filtering to correct over-reinforcement along dominant paths.

2️⃣ MART Algorithm Enhancements

Introduced adaptive correction factors to prevent over-amplification during iterative reconstruction.

Implemented localized smoothing strategies with Gaussian and median filtering.

Reduced update variance by clamping correction factors in a safe range (0.995 - 1.005).

Balanced update weights to distribute correction adjustments evenly across regions.

3️⃣ Sharpness-Based Early Stopping & Optimization

Introduced Laplacian Variance Sharpness Detection to determine optimal stopping points for reconstruction.

Improved early stopping by monitoring Euclidean Norm behavior over iterations.

Identified that norm values peak and stabilize around 300-500 iterations, reducing computational requirements.

Final result: No need for thousands of iterations, saving time and computing power.

4️⃣ Debugging the White Dot Experiment

Designed a black image with a single white dot to evaluate reconstruction performance.

Random rays successfully reconstructed the dot without streaking artifacts.

Fan beam initially produced vertical streaking, which we mitigated by:

Expanding beam coverage from 180° to 360°.

Using adaptive Gaussian filtering only where needed.

Increasing view count from 90 to 250+ for better ray distribution.

📊 Key Takeaways

Random rays consistently outperform fan beam reconstructions in terms of sharpness and artifact reduction.

Fan beam requires careful balancing of ray distribution, correction factors, and filtering to avoid streaking artifacts.

Sharpness-based early stopping is highly effective, preventing unnecessary computation.

Lena (Male) & White Dot experiments confirmed reconstruction stability, setting the stage for more complex testing.

🔥 Next Steps

Re-run Male Lena with the latest filtering and MART adjustments.

Continue improving fan beam reconstruction stability.

Explore deep-learning-assisted denoising to further refine reconstructions.

Submit findings for publication 🚀.
