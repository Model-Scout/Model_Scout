# Jasper Japanese x Sri Lankan Textile Image Dataset

2,000 high-resolution Japanese & Sri Lankan textile images for cross-cultural AI

# Japanese × Sri Lankan Textile Image Dataset

For code supporting the dataset : https://github.com/InfiniteBloom-max/Jasper  <br>
For more details on the dataset creation and the commercial usability : https://docs.google.com/document/d/1LSrd7gN2SPSxYHzY7s1YxMX8sRrw8xZyHFPH5vs9vqE/edit?usp=sharing

## Overview

This dataset contains **2,000 high-resolution textile images** ( combination of 1,000 Japanese, 1,000 Sri Lankan) curated for computational analysis of cross-cultural design patterns. The collection supports research in computer vision, cultural heritage preservation, textile design analysis, and market intelligence for traditional handloom industries.

## Dataset Structure

```
dataset/
│
├── japanese_textiles/
│   └── image_0000.png
│   └── ...
│
├── sri_lankan_textiles/
│   └── image_0000.png
│   └── ...
│
└── metadata.csv
```

**Total Size:** ~1.2 GB  
**Image Format:** PNG  
**Resolution:** 1200 × 700 pixels  
**Preprocessing:** Background removed, color-normalized, cropped to textile surface only

## Data Sources

### Japanese Textiles (n = 1,000)

Images were collected from **publicly accessible online cultural repositories, textile documentation platforms, academic image collections, and verified textile artist portfolios**.

- Cultural heritage and textile documentation websites (~350 images)  
- Academic and open research image repositories (~300 images)  
- Textile artist portfolios and craft documentation platforms (~200 images)  
- Publicly available cultural preservation archives and design catalogs (~150 images)

**Coverage:** Traditional Japanese textile forms including **kasuri weaving**, **shibori dyeing**, and works by contemporary designers operating within traditional aesthetic frameworks. The dataset emphasizes handcrafted textiles representing authentic techniques and regional design traditions.

---

### Sri Lankan Textiles (n = 1,000)

Images were collected from **publicly available handloom documentation platforms, cultural heritage websites, textile catalogs, and academic research collections available online**.

- Cultural heritage and textile documentation websites (~380 images)  
- Publicly accessible textile catalogs and craft documentation platforms (~300 images)  
- Academic and research image repositories (~200 images)  
- Online collections of traditional craft documentation (~120 images)

**Coverage:** Traditional Sri Lankan textile styles including **Dumbara weaving**, **Beeralu lace**, **handloom sarees**, and **traditional batik designs**. Selection focused on textiles representing authentic regional techniques and historically documented design traditions.

## Preprocessing Pipeline

All images underwent standardized preprocessing to ensure consistent feature extraction:

1. **Resolution Standardization:** Resized to 1200×700 pixels using bicubic interpolation (OpenCV INTER_CUBIC)

2. **Background Removal:** Manual cropping to exclude borders, tags, display backgrounds. Semi-automated ROI detection using Canny edge detection (thresholds 50/150) with manual verification

3. **Color Normalization:** 
   - Histogram equalization applied to each RGB channel
   - White balance correction using gray-world assumption (mean RGB = 128)
   - No aggressive color transformation to preserve authentic cultural characteristics

4. **Quality Control:** Excluded images with:
   - Resolution below 800px on shortest dimension
   - Severe lighting artifacts
   - Visible damage or staining
   - Significant digital compression artifacts

**Implementation:** Python 3.9, OpenCV 4.5, NumPy 1.21, scikit-image 0.18

## Use Cases

This dataset enables research in:

- **Computer Vision:** Texture classification, pattern recognition, color analysis
- **Cultural Analytics:** Computational cultural analysis, aesthetic feature extraction
- **Machine Learning:** Training models for textile classification, style transfer, generative design
- **Market Intelligence:** Cross-cultural aesthetic comparison, design adaptation analysis
- **Heritage Preservation:** Digital documentation and analysis of traditional craft techniques

## Features Extractable from This Dataset

The accompanying research paper demonstrates extraction of **44 quantitative features** across multiple aesthetic dimensions:

### Color Analysis
- Dominant color palettes (k-means clustering, k=5)
- RGB channel statistics (mean, std, median per channel)
- Color temperature (warm/cool scoring)
- Hue/saturation/value distributions

### Pattern Complexity
- Edge density and edge mean (Canny edge detection)
- Shannon entropy (information content)
- Texture complexity (local variance)
- Normalized complexity scores

### Texture Characterization
- Local Binary Patterns (LBP) uniformity
- Gray-Level Co-occurrence Matrix (GLCM) features
- Texture contrast
- Surface variation metrics

### Motif Analysis
- Geometric ratio analysis
- Symmetry scoring (vertical/horizontal/radial)
- Pattern repetition detection
- Spatial frequency analysis

## Associated Research

This dataset was created for the research paper:

**"Bridging Heritage and Market: An AI Framework for Analyzing Sri Lankan Handloom Designs for Alignment with Japanese Aesthetic Trends"**

Published in: Lanka Nippon BizTech Institute Journal of Research and Innovation (2026)

**Key Findings:**
- Sri Lankan textiles demonstrate warmer color palettes (warm_cool_score: 0.178 vs -0.111, p<0.001, d=3.059)
- Japanese textiles exhibit 64.3% higher texture complexity (p=0.002, d=1.590)
- Statistically significant differences across 4 of 13 primary metrics with very large effect sizes (d>1.2)
- Distinct cultural aesthetic signatures validated through multiple-comparison corrected statistical analysis

**Analysis Code:** Available on GitHub at [repository link - to be added]

## Citation

If you use this dataset in your research, please cite:

```bibtex
@dataset{rashmikara2026jasper,
  author = {Rashmikara, Ronith},
  title = {Japanese × Sri Lankan Textile Image Dataset (JASPER)},
  year = {2026},
  publisher = {Kaggle},
  url = {https://www.kaggle.com/datasets/[your-username]/jasper-textile-dataset}
}
```

And the associated research paper:

```bibtex
@article{rashmikara2026bridging,
  author = {Rashmikara, Ronith},
  title = {Bridging Heritage and Market: An AI Framework for Analyzing Sri Lankan Handloom Designs for Alignment with Japanese Aesthetic Trends},
  journal = {Lanka Nippon BizTech Institute Journal of Research and Innovation},
  year = {2026},
  supervisor = {Jayathilake, M.},
  institution = {Lanka Nippon BizTech Institute}
}
```

## License

**CC BY 4.0** - Creative Commons Attribution 4.0 International

You are free to:
- **Share** — copy and redistribute the material
- **Adapt** — remix, transform, and build upon the material

Under the following terms:
- **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made

**Note:** Some source images may have additional restrictions. Images from public domain sources (National Museum of Colombo, Kyoto National Museum CC0 collections) have no restrictions. For commercial use of adapted designs, users should verify source permissions.

## Ethical Considerations

This dataset was compiled with respect for cultural heritage and intellectual property:

1. **Cultural Sensitivity:** Traditional designs represent centuries of cultural knowledge and craftsmanship. Users should approach analysis and derivative works with respect for the cultural significance of these textiles.

2. **Attribution:** When using patterns or designs inspired by this dataset, acknowledge the cultural traditions represented (Japanese kasuri/shibori, Sri Lankan Dumbara/Beeralu).

3. **Commercial Use:** While the dataset is available under CC BY 4.0, users creating commercial products inspired by traditional designs should consider:
   - Fair compensation to traditional artisan communities
   - Cultural appropriation vs. appreciation
   - Supporting preservation of traditional craft industries

4. **Source Permissions:** All images comply with copyright and ethical use requirements. Restricted images not available for open distribution have been replaced with source references and access instructions in the metadata.

## Limitations

Users should be aware of the following limitations:

1. **Digital Reproduction:** Images capture visual appearance but cannot represent tactile characteristics, three-dimensional structure, or how textiles interact with light and movement.

2. **Selection Bias:** Museum and archival specimens may skew toward higher quality or historically significant pieces, potentially underrepresenting everyday textiles.

3. **Regional Coverage:** Japanese specimens emphasize kasuri and shibori traditions; Sri Lankan specimens focus on Dumbara, Beeralu, and handloom sarees. Some regional traditions may be underrepresented.

4. **Color Accuracy:** Digital color reproduction may not perfectly match physical specimens, especially for textiles with complex surface properties.

5. **Temporal Range:** Collection spans historical and contemporary pieces without strict temporal categorization. Date metadata not available for all specimens.

## Updates and Versioning

**Current Version:** 1.0 (March 2026)

**Expected Update Frequency:** Annually

Future versions may include:
- Expanded dataset with additional cultural traditions (Korean, Chinese, Indian textiles)
- Enhanced metadata (temporal information, regional categorization, weaving technique tags)
- 3D scans or multi-spectral imaging for select specimens
- Annotated features (color palettes, pattern classifications, motif labels)

## Contact and Contributions

**Dataset Creator:** Ronith Rashmikara  
**Institution:** Lanka Nippon BizTech Institute (LNBTI)  
**Research Supervisor:** Mr. Jayathilake M (mewan@edu.lnbti.lk)

**Feedback Welcome:**
- Report data quality issues
- Suggest additional features or metadata
- Share your research using this dataset

For questions or collaboration inquiries, please contact via Kaggle messages or through LNBTI.

## Acknowledgments

This dataset was made possible through:

- **Lanka Nippon BizTech Institute (LNBTI)** - Institutional support
- **Cultural institutions** that provided access to digital archives
- **Traditional artisans** whose craft is preserved in these images
- **Research supervisor Mr. Jayathilake M** for guidance on methodology and cultural interpretation

This research embodies Japan-Sri Lanka cooperation, demonstrating how mutual respect and knowledge exchange can strengthen both nations' cultural industries while preserving authentic traditions.

---

**Last Updated:** March 2026  
**Version:** 1.0  
**Total Images:** 2,000  
**Total Size:** 1.2 GB

출처: Kaggle (ronithrr/jasper-japanese-x-sri-lankan-textile-image-dataset)
태그: clothing and accessories, computer vision, k-means, image, image classification
라이선스: CC BY-SA 4.0
수정일: 2026-03-12T18:20:59.293Z
