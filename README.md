# MS-EVS Dataset 
From **MS-EVS: Multispectral event-based vision for deep learning based face detection** (WACV 2024)

![ms-evs](https://github.com/ms-evs/ms-evs.github.io/assets/79908627/066f65a8-7acb-4895-b87e-b40decb13390)

## Overview

The MS-EVS Dataset is the first large-scale event-based dataset for face detection.
- Regular images (**APS**) **and** simulated events (**EVS**)
- **Multispectral** data (RGB and/or near IR)
- Very **diverse faces** and data quality (for robust face detection)

It is divided in four subsets: 
- **N-YoutubeFaces**, 3k+ celebrity faces from Youtube videos, in color (simulated events). 
- **N-MobiFace**, 80 unedited mobile live color videos (simulated events).
- **N-SpectralFace**, 69 multispectral videos captured in-house (simulated events).
- **Real-SpectralFace**, a few sequences with real multispectral events (Grayscale and Infrared).
 
⚠️ **Disclaimer:** All datasets have been automatically labeled (either from scratch or to complete existing manual labels) using an existing face detector ([YOLOv5](https://github.com/ultralytics/yolov5)) and therefore contain some (relatively few) wrong/missing bounding boxes. Any contribution is greatly appreciated.

|      **Dataset**      | **APS** | **Simulated EVS** | **Real EVS** |                **Data**                |
|:---------------------:|:-------:|:-----------------:|:------------:|:--------------------------------------:|
|   **N-YoutubeFaces**  |    x    |         x         |              |               Color (RGB)              |
|     **N-MobiFace**    |    x    |         x         |              |               Color (RGB)              |
|   **N-SpectralFace**  |    x    |         x         |              | Multispectral (9 visible + 1 infrared) |
| **Real-SpectralFace** |    x    |                   |       x      | Multispectral (1 visible + 1 infrared) |

## How to download

Script + links 

- Full, light, sample

## Cite

... How to cite ...
+ License


## More information
Disclaimer about labels 
Link to paper, supp, poster (+pointer to relevant sections)

- Script to read data (h5py --> dict) https://github.com/ms-evs/ms-evs.github.io/blob/841c390a61c43e589ccc7561fa90b7390994e55e/inspect_h5_tree.py
- Script to display image + events + labels https://github.com/ms-evs/ms-evs.github.io/blob/841c390a61c43e589ccc7561fa90b7390994e55e/plot_sample.py
