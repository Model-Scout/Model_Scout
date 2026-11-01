---
  license: other
  task_categories:
  - image-to-3d
  - image-classification
  - object-detection
  tags:
  - fashion
  - cultural-heritage
  - 3d-reconstruction
  - andre-kim
  - haute-couture
  - korean-fashion
  - multiview
  size_categories:
  - 1K<n<10K
  language:
  - en
  - ko
  pretty_name: WCCA-AK - André Kim Haute Couture Collection
---

# WCCA-AK: Wearable Cultural Collection Archive - André Kim

  ## Dataset Description

  WCCA-AK is a large-scale dataset of 3D scans and multi-view images capturing 100 haute couture garments by André Kim
  (1962–2010), one of Korea's most iconic fashion designers. This dataset bridges computer vision research and cultural heritage    
   preservation, enabling both faithful documentation of historical artifacts and generative exploration of artistic vision.        

  ## Dataset Summary

  - **Total Items**: 100 haute couture garments
  - **Total Files**: 8,953 files
  - **Total Size**: ~152 GB
  - **Image Files**: 8,835 images (8,799 JPG + 36 PNG)
  - **3D Files**: 54 3D model files (18 FBX + 18 MTL + 18 OBJ)
  - **Metadata Files**: 36 RSInfo files, 28 DB files

  ## Dataset Structure

  The dataset is organized into 100 folders (001-100), each containing multi-view images and 3D scans of a single garment. 

  ### File Types

  - **JPG/PNG**: High-resolution multi-view photographs of garments
  - **FBX/OBJ/MTL**: 3D model files for computational analysis and reconstruction
  - **RSInfo**: Scanning metadata
  - **DB**: Database files

  ## Research Applications

  This dataset supports multiple research directions:

  1. **3D Reconstruction**: High-fidelity 3D modeling of textile and fashion artifacts
  2. **Generative Modeling**: Style transfer, design generation, and artistic continuation
  3. **Computational Fashion Analysis**: Pattern recognition, material analysis, and design evolution studies
  4. **Cultural Heritage Preservation**: Digital archiving and documentation of historical fashion
  5. **Computer Vision**: Multi-view reconstruction, texture analysis, and geometric understanding

  ## Ethical Framework

  WCCA-AK establishes an ethical framework that addresses the dual role of digital archives:

  1. **Historical Documentation**: Faithfully preserving André Kim's artistic legacy with high-fidelity digital records
  2. **Generative Exploration**: Enabling computational methods to study and extend artistic style while maintaining cultural       
  authenticity

  This approach reframes cultural preservation from static documentation into generative exploration, allowing researchers to       
  both honor historical legacy and inspire future creativity.

  ## About André Kim

  André Kim (1962–2010) was a pioneering Korean fashion designer who bridged traditional Korean aesthetics with contemporary        
  haute couture. His work represents a significant cultural heritage of Korean fashion history.

  ## Authors

  - **SeongYeon Oh**, Sogang University
  - **Soyoung Lee**, Chung-Ang University
  - **Taehoon Kim** (Professor), Sogang University
  - **YoungJoon Yoo** (Professor), Chung-Ang University

  ## ⚠️License

  This dataset is distributed under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC       
  BY-NC-SA 4.0)**. (https://creativecommons.org/licenses/by-nc-sa/4.0/)

  ### Usage Restrictions and Legal Liability

  **IMPORTANT: Please read carefully before using this dataset.**

  1. **Non-Commercial Use Only**: This dataset is strictly limited to academic and non-profit research purposes. Any form of        
  commercial use is explicitly prohibited.

  2. **Portrait Rights Protection**: Images containing faces in this dataset are protected under portrait rights laws. The
  following activities are strictly prohibited and may result in legal consequences under relevant laws (Personal Information       
  Protection Act, Information and Communications Network Act, etc.):
     - Private storage, distribution, or editing of face images for purposes other than research
     - Any infringement of portrait rights
     - Unauthorized use of personal data

  3. **Research Ethics**: Users must comply with ethical research practices and respect the cultural significance of the
  archived materials.

  ## Citation

  If you use this dataset in your research, please cite:

  ```bibtex
  @dataset{wcca_ak_2024,
    title={WCCA-AK: A Large-Scale Dataset of 3D Scans and Multi-View Images of André Kim's Haute Couture},
    author={Oh, SeongYeon and Lee, Soyoung and Kim, Taehoon and Yoo, YoungJoon},
    year={2024},
    institution={Sogang University and Chung-Ang University},
    publisher={Hugging Face},
    howpublished={\url{https://huggingface.co/datasets/SY95/WCCA-AK-images}},
    note={Licensed under CC BY-NC-SA 4.0}
  }

  Future Plans

  - Expand the collection to 1,000 garments
  - Extend the methodology to other designers
  - Develop benchmark tasks for 3D reconstruction and generation

  Contact

  For questions, collaborations, or access inquiries, please contact:
  - SeongYeon Oh: dhdev95@gmail.com
  - Sogang University / Chung-Ang University

  Acknowledgments

  This research was supported by IITP and MSIT of Korea through the Graduate School of Metaverse Convergence Program (RS-2022-00156318), and by MCST of Korea through the KOCCA grant (RS-2023-00219237) as part of the Culture, Sports, and Tourism R&D Program. Also, the research was supported by the Institute of Information & Communications Technology Planning & Evaluation (IITP) grant funded by the Korea government (MSIT) [RS-2021- II211341, Artificial Intelligence Graduate School Program (Chung-Ang University)]. We thank Tridot Inc. and the Korea Creative Content Agency (KOCCA) for essential 3D scanning facility support, and the Andre Kim Design Ate- ´ lier for archive access and guidance.

  ---
  Disclaimer: By using this dataset, you agree to comply with all usage restrictions and legal requirements stated above. The       
  authors and institutions assume no liability for misuse of this dataset.