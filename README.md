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


|      **Dataset**      | **APS** | **Simulated EVS** | **Real EVS** |                **Data**                |
|:---------------------:|:-------:|:-----------------:|:------------:|:--------------------------------------:|
|   **N-YoutubeFaces**  |    x    |         x         |              |               Color (RGB)              |
|     **N-MobiFace**    |    x    |         x         |              |               Color (RGB)              |
|   **N-SpectralFace**  |    x    |         x         |              | Multispectral (9 visible + 1 infrared) |
| **Real-SpectralFace** |    x    |                   |       x      | Multispectral (1 visible + 1 infrared) |

## How to download

As the MS-EVS Dataset is quite big (a few hundred GBs), we compressed all the h5 files and split the dataset into many different subsets.

General procedure:
- **Select** the relevant datasets for your project
- **Download** the selected files, e.g. with `wget -np -R "index.html*" -c -nH -r http://ms-evs.aisoft.org/link/to/subset/` (change link)
- **Uncompress** the h5 files (`zstd -d ./path/to/compressed/file.h5.zst -o ./path/to/uncompressed/file.h5`)
- **Enjoy!**
- Optional: have a look at our [demo scripts](#useful-scripts) to inspect the dataset files.

### MS-EVS Dataset: All channels (RGB, Multispectral, Grayscale)

<details>
  <summary>Click to see the download links (for wget)</summary>
  
- N-YoutubeFaces (211G) : https://ms-evs.aisoft.org/N-YoutubeFaces/full/
- N-MobiFace (83G) : https://ms-evs.aisoft.org/N-MobiFace/full/
- N-SpectralFace (25G) : https://ms-evs.aisoft.org/N-SpectralFace/full/
- Real-SpectralFace () : Coming soon...

</details>

### LIGHT MS-EVS Dataset: Grayscale only (~3 times lighter)
<details>
  <summary>Click to see the download links (for wget)</summary>
  
- N-YoutubeFaces (103G) : https://ms-evs.aisoft.org/N-YoutubeFaces/gs/
- N-MobiFace (30G) : https://ms-evs.aisoft.org/N-MobiFace/gs/
- N-SpectralFace (15G) : https://ms-evs.aisoft.org/N-SpectralFace/gs/
- Real-SpectralFace () : Coming soon...

</details>

### DEMO MS-EVS Samples: A selection of files to quickly explore the data
<details>
  <summary>Click to see the download links (for wget)</summary>
  
- N-YoutubeFaces (1.2G) : https://ms-evs.aisoft.org/N-YoutubeFaces/sample/
- N-MobiFace (1.5G) : https://ms-evs.aisoft.org/N-MobiFace/sample/
- N-SpectralFace (2.5G) : https://ms-evs.aisoft.org/N-SpectralFace/sample/
- Real-SpectralFace () : Coming soon...

</details>

**BONUS:** Some files (8.5G) were removed from N-SpectralFace but can be downloaded here (https://ms-evs.aisoft.org/N-SpectralFace/extra/) : it is either captured under regular office light (LED) so it does not have infrared illumination (not used for our experiments) AND/OR it contains obvious labelling/calibration/syncing issues.

## Cite

If you find the **MS-EVS Dataset** useful, please consider citing:
```
@InProceedings{Himmi_2024_WACV,
    author    = {Himmi, Saad and Parret, Vincent and Chhatkuli, Ajad and Van Gool, Luc},
    title     = {MS-EVS: Multispectral Event-Based Vision for Deep Learning Based Face Detection},
    booktitle = {Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)},
    month     = {January},
    year      = {2024},
    pages     = {616-625}
}
```

Saad Himmi, Vincent Parret, Ajad Chhatkuli, and Luc Van Gool. Ms-evs: Multispectral event-based vision for deep learning based face detection. In _Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)_, pages 616–625, January 2024.

This dataset is distributed under the permissive **MIT License**.

## More information
[[paper](https://openaccess.thecvf.com/content/WACV2024/papers/Himmi_MS-EVS_Multispectral_Event-Based_Vision_for_Deep_Learning_Based_Face_Detection_WACV_2024_paper.pdf)][[supp](https://openaccess.thecvf.com/content/WACV2024/supplemental/Himmi_MS-EVS_Multispectral_Event-Based_WACV_2024_supplemental.pdf)][[poster](https://github.com/ms-evs/ms-evs.github.io/blob/40d657cce1f60f32b6745c5514daeeef5d18d1aa/wacv24-poster.pdf)]

**Have a look at the supplementary material** for more information about the dataset composition, capture, cleaning and labelling.

⚠️ **Disclaimer:** All datasets have been automatically labeled (either from scratch or to complete existing manual labels) using an existing face detector ([YOLOv5](https://github.com/ultralytics/yolov5)) and therefore contain some (relatively few) wrong/missing bounding boxes. Any contribution is greatly appreciated.

## Useful scripts

Use the following script to see the HDF5 data dictionary structure: [link](https://github.com/ms-evs/ms-evs.github.io/blob/841c390a61c43e589ccc7561fa90b7390994e55e/inspect_h5_tree.py). The structure depends on the number of devices used to record the dataset (1 for N-MobiFace and YoutubeFaces, 2 for the SpectralFace datasets) or the number of channels (RGB, Multispectral, GS+IR...) 

The images, events and labels are all aligned and temporally synced! One can use [this script](https://github.com/ms-evs/ms-evs.github.io/blob/841c390a61c43e589ccc7561fa90b7390994e55e/plot_sample.py) to display synchronized data. This can serve 1)as an example on how to handle HDF5 files and/or events, or 2)as a way to quickly inspect files' data.

Use this script to automatically download and uncompress all the DEMO MS-EVS Samples (~5.2G total). This script can be easily modified to download/uncompress the MS-EVS Dataset (or LIGHT version).
