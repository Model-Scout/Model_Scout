---
library_name: mlx
license: other
license_name: lfm1.0
license_link: LICENSE
language:
- ar
- zh
- en
- fr
- de
- hi
- id
- it
- ja
- ko
- pl
- pt
- ru
- es
- th
- vi
pipeline_tag: text-generation
tags:
- liquid
- lfm2.5
- edge
- heretic
- uncensored
- decensored
- abliterated
- mlx
base_model: MuXodious/LFM2.5-2.6B-absolute-heresy
---
Data:  
  Top 20 most-sensitive layers at 2-bit:  
      1. model.layers.2.self_attn.v_proj                               sens=7.307e-01  params=1,048,576  
      2. model.layers.0.conv.out_proj                                  sens=5.406e-01  params=4,194,304  
      3. model.layers.1.feed_forward.w3                                sens=3.643e-01  params=22,020,096  
      4. model.layers.9.self_attn.out_proj                             sens=3.638e-01  params=4,194,304  
      5. model.layers.13.self_attn.out_proj                            sens=3.602e-01  params=4,194,304  
      6. model.layers.4.feed_forward.w2                                sens=3.485e-01  params=22,020,096  
      7. model.layers.0.feed_forward.w2                                sens=3.388e-01  params=22,020,096  
      8. model.layers.5.self_attn.out_proj                             sens=3.303e-01  params=4,194,304  
      9. model.layers.5.self_attn.v_proj                               sens=3.085e-01  params=1,048,576  
     10. model.layers.0.conv.in_proj                                   sens=3.071e-01  params=12,582,912  
     11. model.layers.17.self_attn.out_proj                            sens=3.023e-01  params=4,194,304  
     12. model.layers.1.feed_forward.w2                                sens=2.946e-01  params=22,020,096  
     13. model.layers.2.feed_forward.w2                                sens=2.865e-01  params=22,020,096  
     14. model.layers.4.conv.in_proj                                   sens=2.805e-01  params=12,582,912  
     15. model.layers.0.feed_forward.w3                                sens=2.795e-01  params=22,020,096  
     16. model.layers.1.feed_forward.w1                                sens=2.742e-01  params=22,020,096  
     17. model.layers.2.self_attn.out_proj                             sens=2.651e-01  params=4,194,304  
     18. model.layers.4.feed_forward.w3                                sens=2.635e-01  params=22,020,096  
     19. model.layers.3.feed_forward.w3                                sens=2.525e-01  params=22,020,096  
     20. model.layers.2.feed_forward.w3                                sens=2.499e-01  params=22,020,096  
  
  Top 20 most-sensitive layers at 3-bit:  
      1. model.layers.2.self_attn.v_proj                               sens=2.607e-01  params=1,048,576  
      2. model.layers.4.feed_forward.w2                                sens=1.994e-01  params=22,020,096  
      3. model.layers.0.conv.out_proj                                  sens=1.972e-01  params=4,194,304  
      4. model.layers.5.self_attn.v_proj                               sens=1.700e-01  params=1,048,576  
      5. model.layers.1.feed_forward.w1                                sens=1.336e-01  params=22,020,096  
      6. model.layers.13.self_attn.out_proj                            sens=1.232e-01  params=4,194,304  
      7. model.layers.1.feed_forward.w2                                sens=1.207e-01  params=22,020,096  
      8. model.layers.1.feed_forward.w3                                sens=1.141e-01  params=22,020,096  
      9. model.layers.5.self_attn.out_proj                             sens=1.129e-01  params=4,194,304  
     10. model.layers.0.feed_forward.w2                                sens=1.096e-01  params=22,020,096  
     11. model.layers.2.feed_forward.w2                                sens=1.058e-01  params=22,020,096  
     12. model.layers.9.self_attn.out_proj                             sens=1.055e-01  params=4,194,304  
     13. model.layers.21.self_attn.v_proj                              sens=1.033e-01  params=1,048,576  
     14. model.layers.4.feed_forward.w3                                sens=1.023e-01  params=22,020,096  
     15. model.layers.2.feed_forward.w3                                sens=9.710e-02  params=22,020,096  
     16. model.layers.3.feed_forward.w2                                sens=9.666e-02  params=22,020,096  
     17. model.layers.17.self_attn.v_proj                              sens=9.598e-02  params=1,048,576  
     18. model.layers.17.self_attn.out_proj                            sens=9.486e-02  params=4,194,304  
     19. model.layers.2.self_attn.out_proj                             sens=9.419e-02  params=4,194,304  
     20. model.layers.3.feed_forward.w3                                sens=9.351e-02  params=22,020,096  
  
  Top 20 most-sensitive layers at 4-bit:  
      1. model.layers.29.feed_forward.w2                               sens=0.000e+00  params=22,020,096  
      2. model.layers.29.feed_forward.w3                               sens=0.000e+00  params=22,020,096  
      3. model.layers.29.feed_forward.w1                               sens=0.000e+00  params=22,020,096  
      4. model.layers.29.conv.out_proj                                 sens=0.000e+00  params=4,194,304  
      5. model.layers.29.conv.in_proj                                  sens=0.000e+00  params=12,582,912  
      6. model.layers.28.feed_forward.w2                               sens=0.000e+00  params=22,020,096  
      7. model.layers.28.feed_forward.w3                               sens=0.000e+00  params=22,020,096  
      8. model.layers.28.feed_forward.w1                               sens=0.000e+00  params=22,020,096  
      9. model.layers.28.conv.out_proj                                 sens=0.000e+00  params=4,194,304  
     10. model.layers.28.conv.in_proj                                  sens=0.000e+00  params=12,582,912  
     11. model.layers.27.feed_forward.w2                               sens=0.000e+00  params=22,020,096  
     12. model.layers.27.feed_forward.w3                               sens=0.000e+00  params=22,020,096  
     13. model.layers.27.feed_forward.w1                               sens=0.000e+00  params=22,020,096  
     14. model.layers.27.self_attn.out_proj                            sens=0.000e+00  params=4,194,304  
     15. model.layers.27.self_attn.v_proj                              sens=0.000e+00  params=1,048,576  
     16. model.layers.27.self_attn.k_proj                              sens=0.000e+00  params=1,048,576  
     17. model.layers.27.self_attn.q_proj                              sens=0.000e+00  params=4,194,304  
     18. model.layers.26.feed_forward.w2                               sens=0.000e+00  params=22,020,096  
     19. model.layers.26.feed_forward.w3                               sens=0.000e+00  params=22,020,096  
     20. model.layers.26.feed_forward.w1                               sens=0.000e+00  params=22,020,096  

  Top 20 most-sensitive layers at 5-bit:  
      1. model.layers.4.feed_forward.w2                                sens=1.022e-01  params=22,020,096  
      2. model.layers.5.self_attn.v_proj                               sens=7.293e-02  params=1,048,576  
      3. model.layers.2.self_attn.v_proj                               sens=6.815e-02  params=1,048,576  
      4. model.layers.0.conv.out_proj                                  sens=6.409e-02  params=4,194,304  
      5. model.layers.9.self_attn.v_proj                               sens=3.789e-02  params=1,048,576  
      6. model.layers.17.self_attn.v_proj                              sens=3.775e-02  params=1,048,576  
      7. model.layers.1.feed_forward.w3                                sens=3.597e-02  params=22,020,096  
      8. model.layers.1.feed_forward.w2                                sens=3.568e-02  params=22,020,096  
      9. model.layers.0.feed_forward.w2                                sens=3.500e-02  params=22,020,096  
     10. model.layers.21.self_attn.v_proj                              sens=3.448e-02  params=1,048,576  
     11. model.layers.2.feed_forward.w2                                sens=3.330e-02  params=22,020,096  
     12. model.layers.13.self_attn.out_proj                            sens=3.272e-02  params=4,194,304  
     13. model.layers.5.self_attn.out_proj                             sens=3.143e-02  params=4,194,304  
     14. model.layers.2.self_attn.out_proj                             sens=3.026e-02  params=4,194,304  
     15. model.layers.4.feed_forward.w3                                sens=2.964e-02  params=22,020,096  
     16. model.layers.3.feed_forward.w2                                sens=2.858e-02  params=22,020,096  
     17. model.layers.9.self_attn.out_proj                             sens=2.793e-02  params=4,194,304  
     18. model.layers.0.conv.in_proj                                   sens=2.732e-02  params=12,582,912  
     19. model.layers.3.feed_forward.w3                                sens=2.728e-02  params=22,020,096  
     20. model.layers.2.feed_forward.w3                                sens=2.688e-02  params=22,020,096  
  
  Top 20 most-sensitive layers at 6-bit:  
      1. model.layers.4.feed_forward.w2                                sens=7.575e-02  params=22,020,096  
      2. model.layers.5.self_attn.v_proj                               sens=6.363e-02  params=1,048,576  
      3. model.layers.2.self_attn.v_proj                               sens=6.206e-02  params=1,048,576  
      4. model.layers.0.conv.out_proj                                  sens=5.120e-02  params=4,194,304  
      5. model.layers.9.self_attn.v_proj                               sens=2.948e-02  params=1,048,576  
      6. model.layers.17.self_attn.v_proj                              sens=2.920e-02  params=1,048,576  
      7. model.layers.0.feed_forward.w2                                sens=2.915e-02  params=22,020,096  
      8. model.layers.1.feed_forward.w2                                sens=2.905e-02  params=22,020,096  
      9. model.layers.1.feed_forward.w3                                sens=2.714e-02  params=22,020,096  
     10. model.layers.2.feed_forward.w2                                sens=2.657e-02  params=22,020,096  
     11. model.layers.2.self_attn.out_proj                             sens=2.654e-02  params=4,194,304  
     12. model.layers.21.self_attn.v_proj                              sens=2.609e-02  params=1,048,576  
     13. model.layers.5.self_attn.out_proj                             sens=2.546e-02  params=4,194,304  
     14. model.layers.13.self_attn.out_proj                            sens=2.542e-02  params=4,194,304  
     15. model.layers.4.feed_forward.w3                                sens=2.422e-02  params=22,020,096  
     16. model.layers.3.feed_forward.w2                                sens=2.306e-02  params=22,020,096  
     17. model.layers.3.feed_forward.w3                                sens=2.277e-02  params=22,020,096  
     18. model.layers.2.feed_forward.w3                                sens=2.276e-02  params=22,020,096  
     19. model.layers.9.self_attn.out_proj                             sens=2.264e-02  params=4,194,304  
     20. model.layers.0.feed_forward.w3                                sens=2.245e-02  params=22,020,096  
  
Unfortunately OptiQ was not able to exactly 4.83B (around the size for Q4_K quants).   
  
[INFO] Quantizing  
[INFO] Quantized model with 5.447 bits per weight.  
  <...>  
  Output model size: 1751.3 MB  