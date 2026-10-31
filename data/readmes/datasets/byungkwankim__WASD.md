---
license: cc-by-nc-nd-4.0
language:
- en
- ko
tags:
- spectrum
- mobile
- anomaly
- detection
size_categories:
- 100B<n<1T
---


# WASD: Wireless Anomaly Signal Dataset

## Overview

WASD (Wireless Anomaly Signal Dataset) is designed for anomaly signal detection in wireless signals within fixed urban scenarios. It combines real-world signals measured across 19 LTE and 5G bands with simulated anomalous signals. This dataset is suitable for training various object detection networks and developing robust deep learning models for accurate and efficient anomaly detection in real-world environments.

## Paper Link
DOI:10.1109/ACCESS.2024.3521946 (https://ieeexplore.ieee.org/document/10813361)

## Dataset Features

* **Real-world Measurement Data**: Includes real-world signal data collected from 19 LTE and 5G bands.
* **Diverse Anomaly Signals**: Contains various types of simulated anomaly signals, including tone, chirp, and pulse signals.
* **Realistic Simulation**: Employs realistically feasible random-based parameters and configured fading channels in accordance with 3GPP standards to simulate real-world conditions.

* **Large-scale Dataset**: A comprehensive dataset comprising 85,500 samples across 19 bands.
* **Versatile Usage**: Includes both object detection and normal data, suitable for both supervised and unsupervised learning approaches.

## Notes on the ADC for power calibration (described in metadata json file)
* The iq_level_offset is a calibration correction expressed in dB, i.e., an offset applied to the raw IQ values (integer outputs from the ADC) to convert them into actual power levels in dBm.
* The reference_level specifies the absolute power level (in dBm) to which the raw IQ values correspond. The unit of iq_level_offset is dBµV. For example, if you add –26.191406 to the IQ power data, you obtain the value in dBµV, and by subtracting 107 from that, you obtain the value in dBm. The unit of reference_level is dBmV.

* **IQ Data**: Raw IQ data (`.bin` and `.json` files) measured for each band.
* **Spectrogram Data**: Spectrogram data (`.npy` files) generated using Short Time Fourier Transform (STFT).
* **Labels**: Label data (`.csv` files) containing bounding box coordinates and Interference-to-Signal Ratio (ISR) information of anomaly signals.
* **Data Loaders**: Example jupyter notebook (`.ipynb` files) for loading the IQ data, spectrogram datas into python workspaces.
* **Anomaly Signal Generation Examples**: Example jupyter notebook (`.ipynb` files) for generating abnormal wireless signal (tone, chirp, pulse) with the fading model. The detailed process and information can be found in the paper.

## I/Q Binary data examples from each 5G/LTE band for quicker evaluation (Hugging face)

## Whole Dataset Zip file


## Authors
Jinha Kim (jinha.kim@o.cnu.ac.kr), Hyeongwoo Kim (Hyeongwoo.kim@o.cnu.ac.kr), Byungkwan Kim(byungkwan.kim@cnu.ac.kr)

## Acknowledgements
This work was supported by the MSIT/IITP through the ICT R&D program (RS-2023-00229541).
