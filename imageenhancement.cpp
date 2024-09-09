#include <opencv2/opencv.hpp>
#include <iostream>

void adaptiveEnhancement(const cv::Mat& inputImage, cv::Mat& enhancedImage) {
    // Convert to grayscale if the image is colored
    cv::Mat grayImage;
    if (inputImage.channels() == 3) {
        cv::cvtColor(inputImage, grayImage, cv::COLOR_BGR2GRAY);
    } else {
        grayImage = inputImage;
    }

    // Apply CLAHE (Contrast Limited Adaptive Histogram Equalization)
    cv::Ptr<cv::CLAHE> clahe = cv::createCLAHE();
    clahe->setClipLimit(4.0);  // Adjust the clip limit to control contrast
    clahe->apply(grayImage, enhancedImage);

    std::cout << "Adaptive enhancement applied using CLAHE." << std::endl;
}

int main() {
    // Load an example image (replace with actual file path)
    cv::Mat inputImage = cv::imread("input_ct_image.png");
    if (inputImage.empty()) {
        std::cerr << "Error: Could not load the input image." << std::endl;
        return -1;
    }

    cv::Mat enhancedImage;
    adaptiveEnhancement(inputImage, enhancedImage);

    // Save or display the enhanced image
    cv::imwrite("enhanced_ct_image.png", enhancedImage);
    std::cout << "Enhanced image saved as 'enhanced_ct_image.png'." << std::endl;

    return 0;
}

