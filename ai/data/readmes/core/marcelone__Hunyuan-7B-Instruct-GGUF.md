---
license: other
license_name: tencent-hunyuan
license_link: https://github.com/Tencent-Hunyuan/Hunyuan-7B/blob/main/LICENSE.txt
base_model: tencent/Hunyuan-7B-Instruct
base_model_relation: quantized
tags:
- imatrix
- hunyuan_v1_dense
language:
- zh
- en
- ja
- es
- pt
- fr
- ko
pipeline_tag: text-generation
---
<table>
  <thead>
    <tr>
      <th colspan="9">Output + Embedding</th>
    </tr>
    <tr>
      <th>2-bit</th>
      <th>3-bit</th>
      <th>4-bit</th>
      <th>5-bit</th>
      <th>6-bit</th>
      <th>8-bit</th>
      <th>16-bit</th>
      <th>32-bit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AXL</td>
      <td>BXL</td>
      <td>CXL</td>
      <td>DXL</td>
      <td>EXL</td>
      <td>FXL</td>
      <td>GXL</td>
      <td>HXL</td>
    </tr>
  </tbody>
</table>

**Notes**
* This model performs poorly on correcting German texts.
