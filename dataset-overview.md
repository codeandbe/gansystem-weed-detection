# Dataset Overview

## Project

AI-Powered Weed Detection System for Smart Agriculture

## Objective

The objective of this project was to develop a computer vision model capable of detecting weeds within bean farms to support precision agriculture and reduce manual weed identification efforts.

## Dataset Summary

| Metric                        | Value                |
| ----------------------------- | -------------------- |
| Total Images                  | 213                   |
| Total Annotations             | 2334                  |
| Classes                       | 2                    |
| Class Names                   | Bean, Weed           |
| Average Annotations Per Image | 9.3                  |
| Image Resolution              | 3024 × 4032 (median) |

## Dataset Collection

Images were collected from agricultural environments containing bean crops and naturally occurring weeds. The dataset was designed to simulate real-world farm conditions.

## Annotation Process

All images were manually annotated using Roboflow.

Classes:

### Bean

* Total annotations: 296

### Weed

* Total annotations: 2038

Bounding boxes were used to identify and localize objects within each image.

## Dataset Split

| Split      | Images | Percentage |
| ---------- | ------ | ---------- |
| Train      | 1913     | 82%        |
| Validation | 256      | 11%        |
| Test       | 163      | 7%         |

## Preprocessing

The following preprocessing steps were applied:

* Auto Orientation
* Static Crop
* Resize to 640x640
* Contrast Stretching

## Data Augmentation

The following augmentations were applied:

* Horizontal Flip
* 90 Degree Rotation
* Zoom Augmentation
* Blur
* Motion Blur
* Noise Injection

These augmentations were used to improve model generalization and robustness.

## Challenges

* Small dataset size
* Class imbalance between bean and weed classes
* Variations in lighting conditions
* Differences in plant growth stages

## Skills Demonstrated

* Dataset Engineering
* Computer Vision
* Data Annotation
* Data Preparation
* Machine Learning Workflows
* Agricultural AI
