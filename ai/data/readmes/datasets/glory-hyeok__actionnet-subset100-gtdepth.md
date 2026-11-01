---
license: other
license_name: fourier-actionnet-terms
license_link: https://huggingface.co/datasets/FourierIntelligence/ActionNet
task_categories:
- robotics
tags:
- robotics
- humanoid
- gr1
- depth
- ground-truth-depth
- inverse-dynamics
- data-filtering
- pre-contact
language:
- ko
- en
size_categories:
- n<1K
configs:
- config_name: manifest
  data_files: manifest.csv
---

# ActionNet subset100 with ground-truth depth

**This is a 100-episode subset redistribution of a third-party dataset, plus our derived
artifacts.** Read the attribution before using it.

## Attribution and license

| | |
|---|---|
| Upstream dataset | [FourierIntelligence/ActionNet](https://huggingface.co/datasets/FourierIntelligence/ActionNet) (Fourier Intelligence) |
| What is redistributed | 100 episodes out of 30,121, byte-identical to the upstream tars: `rgb.mp4` (1280x800 fisheye), `depth.mkv` (lossless 16-bit), `timestamps.json`, `<ULID>.hdf5` |
| Upstream terms | Whatever the upstream repository states. **The upstream terms govern the episode payload**; if they disallow redistribution, tell us and this repo comes down. |
| Ours (CC-BY-4.0) | Everything under `derived/`, the mapping tables, `build_subset100.py`, and this document |
| Robot | Fourier GR1-T1, 6-DoF Fourier DexHands, single head-mounted camera (`top`) |

## Why this subset exists

The widely used LeRobot conversion (`lerobot/action_net`) drops depth and downscales RGB to
192x288, and its `observation.state` is indexed at the robot's 60 Hz while its rows are
labelled at the camera's 30 Hz — so image and state drift apart by up to half an episode.
Both problems are documented, with measurements, below. This subset keeps the original
1280x800 RGB, the lossless ground-truth depth, and a corrected per-video-frame state
built from the original hdf5.

## What is corrected here (2026-08-20)

| | Measured |
|---|---|
| `observation.robot_joints[k]` vs hdf5 `/state/robot[k]` | within 1e-5 on 97/100 episodes (median max abs diff 5.95e-08); the same tar-independent check passes 21/21 on a second tar |
| the documented `[2k]` rule | 0/100, median max abs diff 0.740 rad; and in 18/21 episodes of the second tar `2k` runs past the end of the hdf5 |
| FK of our corrected states vs the dataset's own `/state/pose` | left EEF median 0.29 cm, right 0.27 cm, head 0.59 cm, over 3 cm on 0/100 |
| the same check with states indexed by video frame | the moving arm sits median 7.59 cm off (range 2.96-18.66), 99/100 over 3 cm; the idle arm stays at 0.33 cm, which is why this hid for so long |

---

# Pre-Contact Level Filtering — the inputs, the verdicts, and how to apply it

Added 2026-08-24. Everything above is about the **capture**: what was redistributed, what was
corrected, and what the depth is. This part is about what we then did with it -- the filter that
decides whether a video is consistent with the action stream that goes with it -- and it ships the
inputs and verdicts so the filter can be re-run rather than taken on trust.

**The top-level directories are new and are the authoritative ones.** `derived/` is the earlier
partial staging and is kept for the artifacts that did not move: `derived/points/`,
`derived/hand_points2/`, `derived/hand_tracks3/`, and `derived/states/` (the **un**-tau-corrected
states). Two of its folders were removed rather than left to be picked by accident --
`derived/masks/` held only 43 of the 100, and `derived/states_tau/` was byte-identical to the new
`states/` (all 100 checked by md5); that folder's evidence note moved to `states/README.md`.

## F0. What the filter decides

Given a video and the action stream that goes with it, **is the video consistent with those
actions?** The question exists because generated video is used as training data: a clip whose
pixels show an arm going somewhere its actions never went teaches a policy the wrong thing.

The filter answers in two levels, and both must pass:

| level | question | space | what it can see |
|---|---|---|---|
| **Pre-Contact** | did the acting fingertip ever reach the target object's boundary? | 1280x800 pinhole | one state, the action stream, the frame-0 object. **Never the pixels.** |
| **Occlusion** | at that instant, does the arm the video draws actually cover the object? | the video's own resolution | the pixels |

The split is deliberate. Pre-Contact is a geometric screen computed from actions alone, so it
cannot be fooled by a rendering. Occlusion is the pixel check, and it is only asked at the instant
Pre-Contact names. Neither is a contact test; together they are a screen.

**This set is the reference, not the target.** Every episode here is a real teleoperated
demonstration, so the arm does reach the object. Running the filter here answers *does it destroy
good data?* -- the answer is 98/100 -- and calibrates the constants. The set it exists to judge is
generated video: see
[`glory-hyeok/robocurate-synth100`](https://huggingface.co/datasets/glory-hyeok/robocurate-synth100).

---

## F1. What is in here

```
manifest.csv                    one row per episode: ulid, task_hand, object_phrase,
                                obj_px_frame0, grasp/release frame, occlusion_pos, occlusion_neg
camera.json                     K_pinhole, K_fisheye, D, and the space definitions

gtdepth/depth_<U>.npz           GROUND-TRUTH depth, already undistorted + downsampled:
                                  depth        (T, 400, 640) float16, metres
                                  frame_indices (T,)     which video frames these are
                                  K_ds         (3,3)     the intrinsics for THIS array
                                  ds           ()        the downsample factor (2)
                                  K_full       (3,3)     the 1280x800 pinhole K
                                  zero_frac, sat_frac    per-frame sensor quality
masks/object_masks_<U>.npz      target-object masks, (T, 800, 1280) bool + frame_indices,
                                  n_px, object_phrase, method, n_obj
states/states_<U>.npz           states (T,44) + actions (T,44) + frame_indices, tau-corrected
handmasks/<U>_{L,R}.npz         tracked arm masks (24 episodes -- the sampled subset)
world3d/world3d_<U>.json        the Pre-Contact verdict, per episode + per frame
occlusion/occlusion_full.json   the Occlusion verdict, all 100 in one table
occlusion/occlusion_series.json the per-frame score inside the window
```

Also in the repo, from an earlier partial staging: `derived/points/` (VLM object points),
`derived/hand_points2/` and `derived/hand_tracks3/` (10 episodes each), `derived/states/` (the
**un**-tau-corrected states), and `subset100_gtdepth.tar`. The top-level directories above are the
authoritative ones -- `derived/masks/` held only 43 of the 100 and `derived/states_tau/` was a
byte-identical copy of `states/`, so both were removed rather than left to be picked by accident.

`gtdepth/` is multi-frame, but **the filter only uses frame 0** -- the object is not moved before it
is touched, so its boundary is built once and held (`static_box: true`, `box_frame: 0` in every
verdict). The rest of the frames ship because they are what a depth model gets scored against.

---

## F2. The scene, and why it matters

Every episode has **`n_obj = 1`**: a single pastry on a plate, on a striped tablecloth. The masks
are ours, from a SAM 3 text prompt (`croissant` x94, `bread` x3, `bagel` x2, `donut` x1), keeping
the **largest connected component** inside an area band.

That single-object scene is doing quiet work, and it is the main reason numbers measured here are
**looser than what a cluttered scene needs**. When a mask's border bleeds a pixel past the object,
here it lands on the tablecloth immediately beside it -- at nearly the pastry's own depth. In a
multi-object scene the same one-pixel error lands on a **neighbouring object tens of centimetres
away**, and the lifted point cloud gains a second cluster that stretches the boundary. See §F6.

---

## F3. How to apply Pre-Contact filtering

### F3.1 What you need beyond this repo

| | |
|---|---|
| robot model | `GR1T1_fourier_hand_6dof.urdf`, from [`FFTAI/teleoperation`](https://github.com/FFTAI/teleoperation) `@main:assets/urdf/`, md5 `78ec53140a125ef50c3a8701249fb036` (not redistributed here) |
| forward kinematics | any URDF FK that returns the world pose of every link |

The 44-channel state layout is ActionNet's own. Channels 0-6 are the left arm, 22-28 the right;
the 6 hand slots per side are declared in `configs/hand/fourier.yaml` order
(`pinky, ring, middle, index, thumb_pitch, thumb_yaw`) and are **DexHand raw units in [0, 10.3]**,
not radians, on this set.

### F3.2 The trajectory

Roll the state forward from the episode's **first** state using the recorded actions, subsampled to
15 Hz (`actions[::2]`), with a first-order tracking model:

```
q[t+1] = q[t] + beta * (q[t] - q[t-1]) + alpha * (a[t] - q[t])
         beta = 0.0    alpha = 0.45 (body)   alpha = 0.60 (hand)
```

Then add two offset layers, in this order:

1. **`rollout_offsets`** -- both arms and the waist/head chain, largest term 4.29 deg. These
   correct the controller's standing bias, which the rollout inherits.
2. **`left_arm_offset`** -- the **left arm only**: shoulder pitch 0.40, roll -0.27, yaw 4.04,
   elbow pitch 7.21 deg. This is a *left-arm encoder zero bias*, not a symmetric fudge: under it,
   9 of 10 fit episodes reach 0.26-1.12 px reprojection error, which is the level the right arm
   already reaches with no offset at all. **Do not mirror it to the right arm.** It moves the left
   fingertip by 6.11 cm, so getting this wrong on a left-handed episode is larger than the object.

Both files are in the repo root alongside this card.

### F3.3 The object boundary

At **frame 0** only:

```python
z  = np.load(f"gtdepth/depth_{u}.npz")
D  = z["depth"][list(z["frame_indices"]).index(0)].astype(float)   # (400, 640) metres
Kd, ds = z["K_ds"], int(z["ds"])

m  = np.load(f"masks/object_masks_{u}.npz")
M  = m["masks"][list(m["frame_indices"]).index(0)][::ds, ::ds]     # match depth's grid

ok = M & (D > 0.05) & (D < 2.6)                 # sensor range gate
v, u_ = np.nonzero(ok); zc = D[v, u_]
lo, hi = np.percentile(zc, [5, 95])             # drop depth outliers
k = (zc >= lo) & (zc <= hi); v, u_, zc = v[k], u_[k], zc[k]

P_cam = np.stack([(u_ - Kd[0,2]) / Kd[0,0] * zc,
                  (v  - Kd[1,2]) / Kd[1,1] * zc, zc], 1)
P_base = (base_T_cam[:3,:3] @ P_cam.T).T + base_T_cam[:3,3]

lo3 = np.percentile(P_base, 1, axis=0)          # 1-99 per axis, NOT min/max
hi3 = np.percentile(P_base, 99, axis=0)
centre = (lo3 + hi3) / 2
radius = np.linalg.norm(hi3 - lo3) / 2          # circumscribed sphere of the AABB
```

`base_T_cam = FK(q0)["head_pitch_link"] @ head_pitch_T_cam`, with the extrinsic from
`align_camera_hullfit_20260820.npz` in the repo root.

The boundary is the **circumscribed sphere of the trimmed box**, not the box. The sphere is 4.2x
the volume, which is the point: Pre-Contact is a screen, and a screen should be generous. On this
set the median radius is **8.15 cm**, from an AABB of **13.1 x 7.0 x 7.1 cm** -- genuinely a
croissant.

### F3.4 The distance, and the event

Per frame, over the **five `*_tip_link` fingertips of the task hand**:

```python
d = max(0.0, min(norm(FK(q_t)[tip][:3,3] - centre) for tip in tips) - radius)
```

`d == 0` means inside. **Pre-Contact is an EVENT, not a state**: the entry frame is the first frame
at `d == 0` *having been outside on the frame before*.

```python
if entry is None and prev is not None and d <= 0 < prev:
    entry = t
```

Frame 0 therefore can never qualify -- there is no frame before it to have been outside on. That
sounds like it should cost something, because **24 of 100 episodes already start inside the sphere**:
the demonstration often begins with the hand near the pastry. Measured, it costs **nothing**. All 24
also produce a crossing later -- the hand leaves and comes back, which is what picking a thing up
and putting it down looks like -- so **100 of 100 episodes here have an entry event**.

The same holds on the generated set: 21 of 300 clips start inside (7 per method, and exactly 7
because all three share the same 100 conditioning frames, so frame 0 does not depend on the
generator), and all 21 get an entry event anyway. **Nothing is lost to the frame-0 rule in either
set.** Clips with no entry are clips whose fingertip never reached the boundary at all, which is the
signal the filter exists to find.

### F3.5 Occlusion, at that instant only

Window: **+-1 s around the entry frame**, i.e. `+-30` frames at this set's 30 fps.

```python
obj = object_mask_at_frame_0                       # static: nothing moves it before contact
occ = max(|arm_mask[f] & obj| / |obj|  for f in window)
keep = occ >= tol
```

The denominator is **the object**, not the union. Measured on the 24 episodes with tracked arm
masks, the arm mask is **3.2x the object at the median** (range 0.5-10.1x), so on a clean grasp that
fully covers the object, IoU reads about 0.31 where coverage reads 1.0 -- it understates by roughly
the size ratio, and understates most in exactly the frames where the arm is closest. Coverage has no
such bias, and it is also the quantity the question asks for: *what fraction of the object is
covered.*

### F3.6 The threshold, and why this set cannot set it

| tol | task hand passes | idle hand falsely passes |
|---|---|---|
| 0.1 % | 98 / 100 | **0 / 100** |
| 1 % | 98 / 100 | 0 / 100 |
| 5 % | 98 / 100 | 0 / 100 |

The task hand's occlusion is **43.1 %** at the median (10th percentile 19.8 %); the idle hand --
the negative control, the arm that never moves -- reaches **0.00 % at its maximum**. Separation is
total, so **the threshold is unidentifiable here**: three values two orders of magnitude apart give
the same answer. It has to be set on generated video, where the scores are lower and the control is
much harder (an arm that genuinely moves and grasps, just not the instructed object). Treat any
`tol` in this range as provisional.

---

## F4. What came out on this set

| | |
|---|---|
| episodes | 100 |
| Pre-Contact entry found | 76 (24 start inside the sphere at frame 0 -- no observable event) |
| Occlusion, task hand | median 43.1 %, p10 19.8 % |
| Occlusion, idle hand (control) | median 0.00 %, **max 0.00 %** |
| both levels pass | 98 of the 100 that were scored |
| boundary sphere | median 8.15 cm |

98/100 is the answer to *does the filter destroy good data* -- and that is all a set of real
demonstrations can tell you. It cannot tell you whether the filter **catches** bad data, because
there is no bad data here. That requires generated video.

---

## F5. Reproducing the verdicts

`world3d/world3d_<U>.json` records the settings each verdict was produced with, so a
reimplementation can be checked against them rather than trusted:

```json
{"ulid": "...", "task_hand": "R", "static_box": true, "box_frame": 0,
 "box_trim_pct": 1.0, "boundary": "sphere", "grasp_frame": 194,
 "grasp_frame_recorded": 191, "grasp_source": "rollout",
 "tip_to_box_at_grasp_cm": 0.0, "curve_min_cm": 0.0, "n_frames_scored": 149}
```

`grasp_source: "rollout"` is worth noting: the verdict is computed from the **rolled-out**
trajectory, not the recorded states, so that this set and the generated set are judged by the same
machinery. `grasp_frame_recorded` is what the recorded states say, kept for comparison -- the two
agree to a few frames.

---

## F6. Known limitation: the boundary sphere absorbs depth leak, and here you cannot see it

The mask's border bleeds a little past the object; the lifted points then include a few at the
wrong depth. On **this** set that is nearly harmless, and the reason is worth stating because it
does not transfer:

- The croissant's AABB is **13.1 x 7.0 x 7.1 cm**. Its longest axis is *real*, and it dominates the
  half-diagonal -- depth is only 43 % of it. Adding 5 cm of leak to the depth axis grows the sphere
  **24 %**.
- On the generated set the object is a block, **5.8 x 5.0 x 3.2 cm** -- nearly isotropic, and depth
  is its *shortest* true axis, so it has the most room to be corrupted and takes over the diagonal
  the moment it is. The same 5 cm grows that sphere **42 %**.
- Add the scene: here a border leak lands on the tablecloth at the pastry's own depth; there it
  lands on a neighbouring object, which is a large jump.

Measured on the generated set, clips whose object-region depth spans under 5 cm give a 4.02 cm
sphere while those spanning over 15 cm give 11.46 cm -- **same object class, so what varies is the
measurement, not the object.** The fix is to select depth as a band around the object-region
**median** rather than by percentile; the percentile trim cannot remove a leak larger than 5 % of
the mask, and on a small object the leak is 10-20 %.

**Nothing was changed here.** The verdicts in `world3d/` use the 5-95 percentile trim, and on this
set the difference is small enough not to matter. Anyone porting these constants to a cluttered
scene or a smaller object should re-derive them first.

---

---

# ActionNet subset100 — GT depth 포함 100 에피소드

**한 줄 요약**: LeRobot 변환본에는 depth가 없고 RGB도 192×288로 줄어 있어서, 원본 tar에서
**1280×800 RGB + 무손실 GT depth**를 가진 100 에피소드만 골라 자립형으로 묶은 것입니다.

작성 2026-08-20. 상위 디렉토리의 `README_MAPPING.md`(내부 문서, 공개되지 않음)가 원본 ↔ LeRobot
대응의 근거 문서이고, 이 문서는 그중 **100개 부분집합**과 **파생 산출물**만 다룹니다.

## 정정 2026-08-20 (당일 갱신) — `derived/states`를 교체했습니다

| 무엇 | 이전 | 지금 |
|---|---|---|
| `derived/states/` | LeRobot parquet에서 뽑아 **stride 4**로 정렬 | **원본 hdf5**를 영상의 `timestamps.json` 시계에 최근접 리샘플 |
| 이전 판의 위치 | — | `derived/states_lerobot_WRONG_do_not_use/` (지우지 않고 남김) |
| LeRobot 변환본 fps (§4 표) | "15 fps" | **30 fps**, 프레임 수가 원본과 동일 (447/432/491 실측, `meta/info.json` `fps: 30`) |

원인은 상위 `README_MAPPING.md` §4(내부 문서)의 정렬 오류입니다 — LeRobot의 state 행은 30 Hz가 아니라
**60 Hz 인덱스**입니다. 그래서 **영상 프레임 번호로 state를 인덱싱한 산출물은 전부 다시
만들어야 합니다**(움직이는 팔 FK가 `/state/pose`에서 100 ep 중앙 **7.59 cm** 벗어남,
최대 18.66 cm, 99/100 ep가 3 cm 초과. 정지한 팔은 0.33 cm라 한쪽만 보면 안 보임).
마스크·points·tracks는 영향 없습니다 — 영상 프레임에서 직접 만든 것이고, 새 `derived/states`의
`frame_indices`도 같은 원본 비디오 프레임 축이라 그대로 대응합니다.

**§5에 추가된 사실 하나 더**: 공유 마스크는 **원본 어안 영상 좌표계가 아닙니다** — 언디스토트된
pinhole 렌더링 위에서 계산됐습니다. raw `rgb.mp4`에 그대로 얹으면 주변부에서 100 px 이상
틀어집니다. §5 참조.

---

## 1. 경로

> **경로 표기 주의**: 아래 표는 이 패키지가 **우리 클러스터에 놓인 위치**이고, 외부 독자에게는
> 의미가 없습니다. HF 저장소에서는 같은 것들이 저장소 루트에 있고, 파생 산출물은 `derived/`가
> 아니라 최상위 `gtdepth/ masks/ states/ handmasks/ world3d/ occlusion/`입니다.

| 무엇 | 경로 (내부) |
|---|---|
| **이 디렉토리** | `<내부 아티팩트 마운트>/action_net_og/subset100_gtdepth/` |
| ├ 페이로드 tar (100 ep, ~4.4 GB) | `subset100_gtdepth.tar` |
| ├ 명단 (한 줄에 ULID 하나) | `ulids.txt` |
| ├ **대응표** | `mapping_subset100.csv` / `.json` |
| ├ 재현 스크립트 | `build_subset100.py` |
| └ 파생 산출물 (우리 Stage-5 작업물) | `derived/` |
| 상위: 원본 tar 4개 + 전체 대응표 | `..` |
| HF 원본 | `https://huggingface.co/datasets/FourierIntelligence/ActionNet` |

---

## 2. tar 안에 무엇이 있는가

에피소드당 4개 파일, **평균 44 MB** (rgb 31 MB + depth 11.7 MB + hdf5 1 MB):

```
<ULID>/top/rgb.mp4          1280x800, 30 fps, h264
<ULID>/top/depth.mkv        1280x800, 16-bit, ffv1 / gray16le  (무손실)
<ULID>/top/timestamps.json  프레임별 타임스탬프 문자열
<ULID>.hdf5                 /state/{robot(32),hand(12),pose(27)}, /action/{...}, /timestamp
```

원본 tar과 **동일한 레이아웃**이라, 기존에 tar을 다루던 코드가 그대로 돕니다.

---

## 3. 이 100개가 무엇인가 — 크루아상 과제로 의도적으로 고정했습니다

| 항목 | 값 |
|---|---|
| 출처 tar | **48개** ← `01JMEX00XF-01JN0B0VXS.tar`, **52개** ← `01JN0B1N7D-01JN0Y2AWR.tar` |
| distinct prompt | **3종뿐** |
| ├ Pick up the croissant and put it on a plate | 55 |
| ├ Put the croissant in the container | 42 |
| └ Place the croissant into the container | 3 |

**전부 크루아상 과제이고, 이는 의도한 선택입니다.** Stage-5 필터링은 "생성 영상이 잡는 것처럼
보일 때 IDM action이 3D에서 실제로 물체에 닿았는가"를 검증하는 일이고, 그걸 처음 세울 때는
과제를 하나로 고정하는 편이 훨씬 쉽습니다 — 물체가 하나뿐이면 물체 마스크·3D 박스·접촉 판정이
과제별 변수 없이 비교됩니다. 세 문장은 표현만 다르고 같은 과제입니다.

과제 다양성이 필요한 실험에는 상위 디렉토리의 전체 대응표에서 다시 고르면 됩니다
(`mapping_*.csv`의 `prompt` / `task_group` 열).

---

## 4. depth를 쓸 때 알아야 하는 것 (측정으로 확인한 사실)

| 사실 | 근거 |
|---|---|
| **절대 metric이다** (상대·affine 모호성 없음) | 파일은 **uint16 밀리미터**이고 로더가 `/1000.0`으로 미터로 바꾼다. 원시 분포 min **251~260**, 중앙 **771~799**, max **2698** mm. 기하로 교차검증: 카메라 65 cm 높이·테이블 ~9 cm·tilt 42° → 테이블 중앙 사거리 ≈ 82 cm, 실측 77~80 cm. 또 depth로 적합한 광학중심(base_link 위 65.14 cm)이 URDF FK의 `head_pitch_link`(64.43 cm)와 **0.7 cm** 차 |
| **포화 상한 2698 mm** | 모든 프레임에서 `p99 = max = 2698`. 2.7 m 밖은 잘려 있으니 배경 거리로 쓰면 안 된다 |
| **무효 픽셀 17~18%** | 값 0. 마스크·평면 적합 전에 `depth > 0`으로 걸러야 한다 |
| **z-depth이다** (광선 방향 거리가 아니다) | 테이블보 평면 잔차를 **전 화면 반경**에서 재면 z 해석은 0.83 cm 이내로 평평하고, range 해석은 −2.85 cm로 휜다. 중앙 ROI만 보면 두 해석이 구분되지 않는다 (cos θ ≈ 1) |
| 평면성 | 전체 테이블보로 강건 적합 시 잔차가 **전 반경 0.63 cm 이내** |
| **카메라 캘리브레이션은 데이터셋에 없다** | tar 엔트리 전수·hdf5 attrs·`meta/info.json`을 다 확인했다. hdf5 root에는 `camera_names=['top']`뿐이고 intrinsic·distortion·extrinsic은 어디에도 없다 |
| 어안 초점거리 `f_native = 577.47 px` | **출처 없는 데이터시트 추정치.** 다만 인용된 세 FOV(H 127°, V 79.5°, D 150°)가 `r = f·θ` 아래 0.16%로 일치하고 pinhole로는 83% 벌어지므로, **모델**은 잘 뒷받침된다. 상세는 `filtering/docs/camera.md` (내부 RoboCurate_V2, 비공개) |
| **시계가 두 개다 (2026-08-20 정정)** | hdf5 **59.9 Hz** / 원본 비디오 **30 fps** / LeRobot 영상도 **30 fps**(프레임 수가 원본과 동일). 이전 판의 "LeRobot 15 fps"는 틀렸다 — `meta/info.json` `fps: 30`, ffprobe 실측 447/432/491 프레임이 원본 카메라 프레임 수와 같다. **행 수는 30 fps인데 LeRobot state 값은 60 Hz 인덱스**이므로 프레임 대응은 반드시 각 파일의 `frame_indices`·`timestamp`로 맞출 것 |

### hdf5의 `/state/pose`는 그냥 지나치기 아깝습니다

`(T, 27)` = **3 자세 × (위치 3 + 회전 6)** 이고, 순서는 **왼 EEF / 오른 EEF / 머리**입니다.
GR1T1 URDF로 FK를 돌려 대조하면 이렇게 맞습니다:

| | 데이터셋 `/state/pose` | URDF FK | 차이 |
|---|---|---|---|
| 왼 EEF | [0.2143, 0.2437, 0.1735] | `left_end_effector_link` [0.2132, 0.2451, 0.1697] | **0.4 cm** |
| 오른 EEF | [0.2268, −0.2085, 0.1733] | `right_end_effector_link` [0.2284, −0.2071, 0.1752] | **0.3 cm** |
| 머리 | [−0.0041, −0.001, 0.6443] | `head_pitch_link` [−0.0021, 0.005, 0.6443] | 0.6 cm |

즉 **운동학과 state 매핑을 데이터셋 자체로 검증할 수 있습니다.** 다만 세 가지를 지키세요.

1. **맞는 링크는 `{left,right}_end_effector_link`입니다.** `{L,R}_hand_base_link`로 비교하면
   약 **2.1 cm**가 남습니다(에피소드 전체에서 거의 일정 = 링크 선택 차이, 오차가 아님).
   즉 이 데이터셋이 말하는 "EEF"는 hand_base가 아니라 end_effector 링크입니다.
2. **`/state/pose`는 60 Hz입니다** — 행 수가 mp4 프레임 수의 약 2배입니다(892/447, 799/401,
   1133/567 …). 그래서 `P[영상프레임]`으로 인덱싱하면 틀립니다. frame 0끼리는 그냥 맞지만,
   그 밖의 프레임은 `/timestamp`로 리샘플하세요.
   ⚠️ **LeRobot의 state 행도 똑같이 60 Hz 인덱스입니다** (2026-08-20 실측:
   `observation.robot_joints[k] == /state/robot[k]`, 100 ep 중 97건이 max|diff| 1e-5 이내,
   중앙 **5.949e-08**; `[2k]` 가설은 **0/100**, 중앙 0.740). LeRobot의 행 수는 영상 프레임 수와
   같아서 "그러니 영상 프레임으로 인덱싱해도 된다"고 착각하기 쉬운데, **행 수가 맞는 것과
   내용의 시계가 맞는 것은 다른 문제입니다.** hdf5든 LeRobot이든 **영상 프레임 번호로
   state를 인덱싱하지 마세요** — 시계로 리샘플하세요. 근거는 상위 `README_MAPPING.md` §4(내부 문서).
3. `/state/robot`의 채널 순서는 LeRobot 44차원과 **다릅니다** — 다만 그 순서는 이제
   측정으로 확정돼 상위 `README_MAPPING.md` §6-2에 표로 적혀 있습니다(적용하면 100/100
   에피소드에서 max|diff| = 0). `derived/states`의 44차원도 그 순서입니다.

---

## 5. `derived/` — 우리가 만든 파생 산출물 (진행 중)

| 경로 | 개수 | 내용 |
|---|---|---|
| `derived/states/states_<ULID>.npz` | 100 | **원본 hdf5**에서 만든 per-video-frame 상태, **τ 보정 전**. 아래 참조 (2026-08-20 재생성) |
| ~~`derived/states_tau/`~~ → **`states/`** | **100** | τ 보정 상태. 영상 프레임과 짝지을 때는 이것을 쓰세요. 근거는 `states/README.md` |
| `derived/states_lerobot_WRONG_do_not_use/` | 100 | **쓰지 마세요.** 정렬이 틀린 이전 판(LeRobot 유래, stride 4). 판정용으로만 남겨 둡니다 |
| `derived/points/vlm_points_<ULID>.json` | 99 | **물체** point prompt (positive/negative), 에피소드별 수동 지정 |
| ~~`derived/masks/`~~ → **`masks/`** | **100** | SAM3 물체 마스크, 전 프레임. 43개뿐이던 `derived/masks/`는 삭제했고 최상위 `masks/`가 100편 전부입니다 |
| `derived/hand_points2/points_<ULID>.json` | 10 | **팔+손** point prompt: 손당 3점(손가락·손바닥·팔뚝) + negative |
| `derived/hand_tracks3/tracks_<ULID>.npz` | 10 | SAM3 팔+손 마스크, 전 프레임, **좌/우 분리** (`left`, `right`, `frame_indices`) |

### `derived/states` — 원본 hdf5에서 다시 만들었습니다 (2026-08-20)

이전 판은 LeRobot parquet의 state 열을 **stride 4**로 영상 프레임에 얹은 것이었는데,
전제("LeRobot 15 fps × stride 4 = 60 Hz")가 둘 다 틀렸습니다 — LeRobot은 30 fps이고
state 행은 **60 Hz 인덱스**입니다(§4, 상위 `README_MAPPING.md` §4(내부 문서)). 지금 판은 LeRobot을
아예 거치지 않고, **원본 hdf5를 영상 자신의 `timestamps.json` 시계에 최근접 리샘플**합니다
(보간 금지 — 손 12채널이 계단식 원시 단위라 보간하면 로봇이 보고한 적 없는 값이 생깁니다).
빌더는 내부 RoboCurate_V2의 `tools/build_states_hdf5.py`(비공개).

| 키 | shape (예: `01JMXF99BYFPWU5NOL`, T=447) | 내용 |
|---|---|---|
| `states` / `actions` | (447, 44) float64 | 44차원 GR1-T1 순서 (상위 문서 §6-2 표) |
| `frame_indices` | (447,) int64 | **원본 비디오 프레임 번호** (0..T−1, 마스크·tracks와 같은 축) |
| `hdf5_rows` | (447,) int64 | 각 프레임이 고른 hdf5 행 |
| `pose` | (447, 3, 9) float64 | `/state/pose` 같은 행 (왼 EEF / 오른 EEF / 머리) |
| `video_t`, `lag_s`, `clock_offset_s` | (447,), (447,), scalar | 영상 시계 초, 프레임−행 잔차, hdf5↔영상 시계 오프셋 |

검증 (100 ep 전수, FK vs 데이터셋 자신의 `/state/pose`):

| | 중앙 | 최악 | 3 cm 초과 |
|---|---|---|---|
| 왼 EEF | **0.29 cm** | 0.37 cm | 0/100 |
| 오른 EEF | **0.27 cm** | 0.32 cm | 0/100 |
| 머리 | 0.59 cm | 0.60 cm | 0/100 |

프레임↔행 잔차(`lag_s`)는 46,927 프레임 중 **98.6%가 8.34 ms(60 Hz 반 칸) 이내**
(중앙 2.51 ms, p95 6.42 ms, 16.7 ms 초과 1 프레임, 최악 24.35 ms — 한 에피소드
`01JN0XAGCRDDJ33ML4`에 몰려 있음). **각 에피소드의 마지막 프레임만** hdf5가 영상보다 먼저
끝나서 **−12.0 ~ −57.7 ms**(중앙 −29.7 ms) 벌어집니다. 시계 오프셋은 −21.6 ~ +11.1 ms.
마지막 프레임을 쓸 거면 이 값을 감안하세요.

### ⚠️ 마스크는 원본 어안 좌표계가 아닙니다 — 언디스토트된 pinhole 공간입니다

`derived/hand_tracks3/`와 `derived/masks/`는 **raw `rgb.mp4` 위에서 계산된 것이 아닙니다.**
`filtering/src/depth/undistort_fisheye.py --hfov 90`으로 다시 렌더한 **rectilinear(pinhole)
영상** 위에서 SAM3를 돌린 결과입니다. 즉 두 npz의 좌표계는:

| 항목 | 값 |
|---|---|
| 해상도 | 1280×800 (원본과 같음 — 그래서 육안으로 구분되지 않습니다) |
| K | `[[640, 0, 639.5], [0, 640, 399.5], [0, 0, 1]]` (hfov 90°) |
| 투영 | pinhole (`r = f·tanθ`). 원본은 equidistant 어안 (`r = f·θ`) |
| npz 안의 증거 | `video` 키 = `/tmp/rc_undist_<ULID>.mp4` / `/tmp/rc_full_<jobid>_<ULID>.mp4`, 둘 다 위 스크립트 출력 |

**raw `rgb.mp4`에 이 마스크를 그대로 얹으면 주변부에서 100 px 이상 틀어집니다.**
같은 픽셀이 두 공간에서 얼마나 떨어져 있는지(위 두 모델로 계산):

| 언디스토트 영상의 픽셀 | 광축에서 | 대응하는 원본 어안 픽셀 | 어긋남 |
|---|---|---|---|
| (1279, 399.5) 오른쪽 끝 중앙 | 44.98° | (1092.8, 399.5) | **186 px** |
| (1279, 799) 오른아래 코너 | 49.68° | (1064.1, 664.8) | **253 px** |
| (959.5, 399.5) 오른쪽 절반 지점 | 26.57° | (907.2, 399.5) | 52 px |
| 화면 중앙 | 0° | 화면 중앙 | 0 px |

중앙에서는 0이라 **중앙 ROI만 보면 두 공간이 구분되지 않습니다** — 이 오류가 눈에 띄지 않는
이유입니다. 또 hfov 90°는 어안이 담은 화각(127°)보다 좁으므로 **어안의 바깥 주변부는
압축되지 않고 버려집니다**(1280×800에서 깨끗하게 뽑을 수 있는 최대 hfov는 95.9°).

맞는 영상을 다시 만드는 법:

```bash
cd <내부 RoboCurate_V2>/filtering/src
python depth/undistort_fisheye.py <데이터>/data_og/$U/top/rgb.mp4 --hfov 90 -o /tmp/rc_undist_$U.mp4
# 프레임 수·순서는 원본과 동일하므로 mask의 frame_indices가 그대로 맞습니다
```

**색상 판정·depth 조회도 반드시 같은 언디스토트 공간에서** 하세요. depth는
`depth/gt_depth_npz.py`(기본 `--hfov 90`)가 rgb와 depth를 **같은 어안→pinhole 맵**으로
리샘플하므로(RGB 이중선형, depth 최근접) 그 출력과 마스크가 픽셀 단위로 대응합니다.
raw `depth.mkv`를 직접 읽어 마스크 픽셀로 인덱싱하면 **다른 픽셀의 거리값을 집게 됩니다.**

**마스크를 쓸 때의 주의 (숨기지 않고 적습니다)**: 팔+손 마스크는 10개 에피소드 중 8개에서
한쪽이 **61,3xx~61,43x px**에 뭉쳐 있습니다. 이는 추출 상한(`max_obj_frac 0.06 × 1,024,000 =
61,440`)에 **깎여 붙은 테이블보 누출**입니다. 깨끗한 마스크는 14k~33k px(프레임의 1.4~3.3%)이니
**면적 상한 0.045로 걸러서** 쓰세요. 프레임 선별기는 내부 RoboCurate_V2(비공개)의
`filtering/src/align/filter_mask_frames.py`에 있고, 판정에 카메라 자세를 일절 쓰지 않습니다
(현재 extrinsic과 잘 맞는 프레임만 고르면 그 extrinsic을 확증해 버리기 때문).

---

## 6. 쓰는 법

```bash
D=.        # HF 저장소를 받은 디렉토리 (내부에서는 아티팩트 마운트 경로)

# 전체 풀기 (4.4 GB)
mkdir -p ~/actionnet_subset100 && tar -xf $D/subset100_gtdepth.tar -C ~/actionnet_subset100

# 한 에피소드만
U=01JMXF99BYFPWU5NOL
tar -xf $D/subset100_gtdepth.tar -C ~/actionnet_subset100 $U/ $U.hdf5

# 16-bit depth를 numpy로 (ffv1/gray16le는 OpenCV로 열리지 않습니다)
ffmpeg -i $U/top/depth.mkv -f rawvideo -pix_fmt gray16le - \
  | python -c "import sys,numpy as np; \
      a=np.frombuffer(sys.stdin.buffer.read(),np.uint16).reshape(-1,800,1280); \
      print(a.shape, a.dtype, a[0].max())"
```

`depth`의 단위는 **mm(uint16)** 이고, 내부 RoboCurate_V2(비공개)의 `filtering/src/depth/gt_depth_npz.py`는
이 mkv와 rgb를 **같은 어안→pinhole 맵**으로 리샘플해(RGB 이중선형, **depth 최근접**) npz로 만듭니다.
depth를 보간하면 물체 경계에서 없는 거리값이 생기므로 최근접이어야 합니다.

---

## 7. 재현·검증

```bash
cd $D
python build_subset100.py --verify     # 대응표 재생성 + 400개 페이로드 파일 존재 확인
sha256sum -c subset100_gtdepth.tar.sha256
```

`build_subset100.py`는 ULID↔LeRobot 대응을 **다시 계산하지 않습니다** — 상위
`build_mapping.py`가 만든 per-tar 대응표에서 우리 100개 행만 골라내므로, 두 표가 어긋날 수
없습니다. 검증 결과는 작성 시점에 **400/400**이었습니다.

## 추가 2026-08-21 — `derived/states_tau/`와 왼팔 보정값

영상 타임스탬프가 노출 시각보다 약 167 ms 늦게 기록돼 있음을 마스크 대비 실측으로 확인했고,
그 시프트를 반영한 상태를 **최상위 `states/`**(예전 `derived/states_tau/`)에 두었습니다(`derived/states/`는 그대로).
영상 프레임과 상태를 짝지어 쓰는 용도에는 `states_tau`를 쓰세요. 왼팔 관절 영점 바이어스
보정값은 저장소 루트의 `left_arm_offset_20260821.json`에 있습니다. 둘 다 근거와 수치는
`states/README.md`에 적었습니다.
