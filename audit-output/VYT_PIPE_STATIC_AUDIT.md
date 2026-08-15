# VYT-PIPE pinned static source audit — IA-120

## 1. Exact source identity and revision

- Source: `https://github.com/KazartsevEV/VYT-PIPE.git` (`vyt-pipe`).
- Acceptance branch: `audit/ia-120-source-pin`; exact audited Git revision: `67812492af3d34809aea287419c4774a6b44e088`.
- Audit timestamp: `2026-08-15T08:57:33+00:00`; auditor: OpenAI Codex (GPT-5.6 Sol).

## 2. Method and non-execution guarantee

- Enumerated every tracked blob with `git ls-tree -rz --full-tree <revision>` and read each exact object with `git cat-file blob <blob-sha>`.
- Offline Python scanners hashed and classified bytes. Repository Python modules, CLI/application entrypoints, pipeline, tests, batch/PowerShell scripts, and production output generation were **not executed or imported**. No dependency was installed and no endpoint was contacted.
- The checker independently re-enumerates Git objects and validates the canonical manifest against blob bytes.

## 3. Complete inventory and deterministic hash

- Tracked blob count: **35**. Inventory complete: **yes**.
- Canonical `files` inventory SHA-256: `11219ce942e524466928e1e96770f5357b3e3c67aa3a9c599d98e95c9bbf8ce2`.
- Full Git evidence (mode and object ID), plus canonical byte evidence:

| Path | Git mode | Git blob SHA | SHA-256 | Bytes | Type | Decision |
|---|---:|---|---|---:|---|---|
| `.gitattributes` | `100644` | `d9bd16b0923e8d3f1904878df64b8a8ca655f87a` | `86013e6b9434810158ab594bbfd2d77f64b030a5eac5f27fc17afd2f474d561e` | 17 | plain text | **reference** |
| `.gitignore` | `100644` | `dc7c4c2172cec4e99015b2c292ba0a3e0c44b58b` | `8e4303a4f01cfd09f96e1a5ba717ed5ecb991ddde52be05d0dacc673f5f6d84d` | 55 | plain text | **reference** |
| `README.md` | `100644` | `1903524e185f227854f37e433dbddc09782c2f40` | `51bbaaea9134f018f25ec768ba37f2d6256cde0d4f18505b5d8636045ce7c173` | 4808 | Markdown text | **reference** |
| `configs/sample.yaml` | `100644` | `d046e82685471d004b65cdb754938ecf706e9498` | `e955696f5bbb22c9561a3831c6df46cfb10db00d38951eb5a10a7f23aa1f9d45` | 324 | YAML configuration | **reference** |
| `input/.gitkeep` | `100644` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | 0 | plain text | **quarantine** |
| `input/sample.png.xbase64` | `100644` | `9e4b0ef1c639770c02205dd55abd92173b618b43` | `a20fbf45c6dbd30fe19df4c4afe92b2bee72a2db61b0191cdb070c35b4041ee0` | 291 | base64 data-URI text | **quarantine** |
| `make_papercut_panel.bat` | `100644` | `715f0c4dc6c522623820912b82934fc37010c1b6` | `f4f89ceba3e6fd08e4bdc8ba0f1c43355cb99708967476abf89d0da5c8620153` | 4427 | Windows batch script | **reference** |
| `make_papercut_panel.py` | `100644` | `b924ee2314ae926dad1d76470ac1d9388ec7566d` | `cce3933f62491bed5819dac5aa31a8cbd9a4905ddce207ef4a2528584e100396` | 33186 | Python source | **reference** |
| `make_papercut_panel_night.bat` | `100644` | `9dd98ca146bc532aec02e241f16dc5591b4956dd` | `ec04a639b71bbc280b8b57eed9725cb7d14c09de615bf3aa37eeba3cea46d472` | 5572 | Windows batch script | **reference** |
| `papercut_panel_builder.py` | `100644` | `33dd91f723861bb483bcf561b96ec658516186d9` | `1eee95d7f4e53f4133526cf4f3ce07ab0922c07e6943f370af6ebc16fea411b2` | 436 | Python source | **reference** |
| `pyproject.toml` | `100644` | `21f6cafd29e5b8e9b60e1a395a599f19b0766ae5` | `add5b6d7ca171a4361fdaaf294831355eaa7a2fc828aae3cfe2721141998679c` | 653 | TOML configuration | **reference** |
| `requirements.txt` | `100644` | `b2c69fb25a766caa4c722eeb65adc183297be97c` | `f546a55a787d07e7853805436aa9851b8062a35f5f478e20c23e0920ccbff33e` | 222 | plain text | **reference** |
| `src/vyt/__init__.py` | `100644` | `ff8fa007cf7d0812dd3e044a858e998500e04d63` | `4b5b3e0b94452ad7eed18406c903d434fe8bf483b12c492dd5db80f3aedf068f` | 60 | Python source | **reference** |
| `src/vyt/cli/__init__.py` | `100644` | `c3c03bffc956bdba1d5f480b80e7daa0d49f0f84` | `308d99cff60eb8aa4cf3f4feb238d3050f0494e58551a805216cc61ca7cdbb1b` | 35 | Python source | **reference** |
| `src/vyt/cli/__main__.py` | `100644` | `7b5ccca04751d0a57f82d443eabf3dd5a46714d6` | `9109b3da3c0203fb1c3cd03e9bf5988b93913143fa5282f2391d5b1006c2f9b1` | 1382 | Python source | **reference** |
| `src/vyt/core/__init__.py` | `100644` | `c1b27ce9f1f39aa58553cba186e495c3515939f4` | `531d369d7381fba1caf05f88f5a26857f934009be8a4911dc3bb7230e62d0510` | 44 | Python source | **reference** |
| `src/vyt/core/bridge.py` | `100644` | `c5ad1328820217a4d51ae65bb88fc7171feffe7c` | `e6bc554244258b6ae14d7948f9a3d910672c343d55a874b0d172a0cc50459dbb` | 1531 | Python source | **reference** |
| `src/vyt/core/compose.py` | `100644` | `707ae841a3770ee9e10cdd74116e8589f98d8a3f` | `3202047822f51c94f8a1580455645dd25ca1bd5e16c9837c2e359f93099aa453` | 298 | Python source | **reference** |
| `src/vyt/core/ingest.py` | `100644` | `ecc62ce01414e1e00c9b0de177860d9876cacbbc` | `4866817aeb8e00afd75e068124c74946da77bf90df73ae80db5bafa163872537` | 2010 | Python source | **reference** |
| `src/vyt/core/mask.py` | `100644` | `436f3386b3907615b83701b9408732df869f3ccf` | `3234e461ffc34827881bc7b4a37172e509c43121e1bf66a6198d356424a42c59` | 975 | Python source | **reference** |
| `src/vyt/core/pack.py` | `100644` | `028ed7d9205738e3e889eaa125f51f686a0f70d0` | `37ad9690bfe11db445587c3506a601236ab7eb6c526ae35bec8e974755e62768` | 520 | Python source | **reference** |
| `src/vyt/core/pipeline.py` | `100644` | `260bbb236d75a5f51c384c8e7bfbd8b0ba46ce58` | `82510542324e9790ac8bba80c8e613f6bf3e8c2bbb9a25fcf05577498afa929d` | 1725 | Python source | **reference** |
| `src/vyt/core/preview.py` | `100644` | `7a384a730e61d134d5bb2fe282dfe821cd44265b` | `1cd47544913964adf1b66cd4549f8e8549fe59564c6dac6b1e257ed5fbad44cc` | 357 | Python source | **reference** |
| `src/vyt/core/qa.py` | `100644` | `7ebf3b7f6587063c961574af07b46efff7d637af` | `57de28e0c295ad97f0d6ab5a4d64be48888cba11c2fcd96debeffdc892451535` | 483 | Python source | **reference** |
| `src/vyt/core/render_pdf.py` | `100644` | `2fb9ecad7e7a5b6394682c5ac6101038cdce8d71` | `cf6cdf079cac02802058f05fa76656f58f17d025a321cfca82b95ca7f9d97fa3` | 1187 | Python source | **reference** |
| `src/vyt/core/render_pptx.py` | `100644` | `78b788338e14ec827f0739c4c878a145e012b73d` | `009f453a10e9df2a55b5ef883f36a0a8ea74f6934bbd02abfb6bcc3a8942dfc5` | 841 | Python source | **reference** |
| `src/vyt/core/tile.py` | `100644` | `abafdbc4d314439138957c89bffd6db960c2b4d3` | `83ede9e6a2e1591ea423ebdccfe629d7a2c1ff26e8e8c50fd75218b6ccad3c50` | 5012 | Python source | **reference** |
| `src/vyt/core/vectorize.py` | `100644` | `c7b9cb34ee06cb2de2d833dc3f5abb8116eb11e4` | `4d00d286433e6102358aa048c31a9a6d3da5f814a431d3f75b0574f5b12aab32` | 585 | Python source | **reference** |
| `src/vyt/utils/__init__.py` | `100644` | `91532885dd21f357d40c62091dc11bd888c71b6a` | `8c7d2784b7e0b669fffcdc3d7aa83c0b579377384fb7d250174e7b3b5b52c0dd` | 36 | Python source | **reference** |
| `src/vyt/utils/io.py` | `100644` | `6ad9377a6c99d2588ceca849ee70bfcaef9610b9` | `9806bcbd6a86d5ea2b0b77e64f202e027aceb2745ccddcd75534e537428cba1e` | 470 | Python source | **reference** |
| `src/vyt/utils/units.py` | `100644` | `f0240e1464cc28c99b5452ab31e20c32ede1fb06` | `f274611d2c77378be5c1dadf8ba409300ea094ebb663502ba3cf5cde585d02f7` | 347 | Python source | **reference** |
| `templates/cover.svg` | `100644` | `5b437f9c25f58a89ef8d90c5180a4d8702a8d9e8` | `15e585fc4e6d21eb75efa90eea76efb44ba3c943aab55a760ce3aac21997a47e` | 395 | SVG vector asset | **reference** |
| `templates/instructions.md` | `100644` | `5c0be25d0e7620dabbab757a07061177cfcb67a0` | `8f32a535d075b12942c4b8eaf50c4584cabc55bbd25866c07453c37797eaf44c` | 284 | Markdown text | **reference** |
| `templates/readme.txt` | `100644` | `fa80f6ee874cd07ed85ec416f9e42cb1faa80e3f` | `1c0d2cf54abac632ee6f086e1439f18457cd2c64195de0b3a97c12448706e7ab` | 284 | plain text | **reference** |
| `tools/setup_env.ps1` | `100644` | `80df08706aad2c955bb59b6a34b2a19aaa331374` | `0a6428374f8def5fa160eee3555060e26de91d2456f9cb3fedd3786723bb62bc` | 660 | PowerShell script | **reference** |

## 4. CLI and entrypoint map

- `pyproject.toml` declares console command `vyt = vyt.cli.__main__:app`; `src/vyt/cli/__main__.py` exposes Typer commands `make`, `batch`, `qa`, and `pack` and is also a module entrypoint. Only `make` connects to the pipeline; the others are stubs/read-only QA behavior.
- `make_papercut_panel.py` is an independent argparse CLI. `make_papercut_panel.bat` is an interactive Windows wrapper; `make_papercut_panel_night.bat` recursively batches images on Windows.

## 5. Portable pipeline-stage map

`config YAML → ingest/copy or base64 materialization → raster mask → bridge reinforcement → placeholder vector SVG → placeholder composition → A4 SVG tiling → PDF/PPTX render → preview/QA → ZIP package`. The orchestrator is `src/vyt/core/pipeline.py`. Several modules explicitly describe themselves as stubs/placeholders, so behavior is not production-complete.

## 6. Papercut/image-processing boundary

- The monolithic builder performs Pillow-based normalization, grayscale/autocontrast, threshold/detail segmentation, morphological closing/fill, gap joining, inversion selection, mask compositing, 3×4 A4 slicing, and optional PNG/PDF/PPTX writes.
- The package pipeline separately relies on OpenCV/NumPy/Pillow for thresholding and bridge reinforcement, then writes SVG/PDF/PPTX/ZIP artifacts. Raster decoding, untrusted image complexity, embedded SVG references, and output sizing require downstream validation and resource limits.

## 7. Templates and assets (separate from Python)

- `templates/cover.svg`, `templates/instructions.md`, and `templates/readme.txt` are placeholder/reference assets and bounded-port proposals only. The SVG contains text/font/layout assumptions and an XML namespace URI, not a network fetch.
- `input/sample.png.xbase64` is a text data-URI example; it and the input placeholder are quarantined, not candidates. No template is licensed independently.

## 8. Dependencies and version evidence

- **15 unique declared dependencies**: 2 build requirements and 13 runtime requirements. Runtime pins are duplicated consistently in `pyproject.toml` and `requirements.txt`; `setuptools>=66` and unpinned `wheel` are build-system requirements.
- Runtime: `typer[all]==0.12.5`, `rich==13.9.2`, `PyYAML==6.0.2`, `Pillow==10.4.0`, `opencv-python==4.10.0.84`, `numpy==2.1.1`, `scikit-image==0.24.0`, `shapely==2.0.6`, `svgwrite==1.4.3`, `svgpathtools==1.6.1`, `cairosvg==2.7.1`, `pikepdf==9.3.2`, `python-pptx==0.6.23`. No lockfile or hashes establish reproducible transitive resolution.

## 9. Network, subprocess, external-binary, and filesystem boundaries

- **Network services (1):** `tools/setup_env.ps1` invokes pip, whose package-index endpoint is environment-configured; it was not contacted. No application runtime HTTP/API client was found. The Potrace project URL and SVG namespace strings are informational identifiers only.
- **Subprocess/external binaries:** repository Python source contains no subprocess invocation. Windows wrappers invoke `python` and PowerShell; setup invokes Python/pip and probes `inkscape` and `potrace`. CairoSVG/PikePDF/OpenCV may carry native-library boundaries through dependencies.
- **Filesystem/mutable state:** reads config/source/SVG/PDF; creates `.venv`, `build/<id>/{work,out}`, copied/materialized inputs, masks, vectors, tiles, PDF/PPTX/PNG/JPG/QA/ZIP, per-image output directories, and `.log` files. ZIP creation recursively packages output files.

## 10. Windows/POSIX portability findings

- `.bat` launchers use `cmd.exe`, delayed expansion, Windows path syntax, PowerShell, `pause`, and `%ERRORLEVEL%`; `tools/setup_env.ps1` hard-codes `.venv\Scripts`. These are Windows blockers.
- Python uses `pathlib` and is mostly cross-platform, but assumes available native/image/PDF stacks, fonts (Arial), filesystem write access, and case/path behavior. The standalone shebang is POSIX-friendly but does not remove dependency/native-tool blockers.

## 11. Secret scan (redacted evidence only)

- Completed offline scan of all exact blob bytes for private-key markers, credential assignments, authorization headers, common API-token forms, passwords/cookies, and high-entropy token candidates. **0 findings**. Evidence records counts and paths only; no raw credential value is present. The sample base64 payload was treated as an expected image data URI, not a credential.

## 12. Large-file and generated-output findings

- Large-file threshold: **1,048,576 bytes (inclusive)**. Findings: **0**. Largest blob: `make_papercut_panel.py` (33186 bytes).
- Generated/example scan: no tracked `build/`, cache, history, archive, PDF, PPTX, rendered PNG, or packaged output blob. Two input/example-area paths are conservatively quarantined: `input/.gitkeep` and `input/sample.png.xbase64`.

## 13. License and ownership disposition

- No tracked `LICENSE`, `COPYING`, `NOTICE`, SPDX grant, or explicit downstream reuse permission was found. Repository ownership/public visibility is not treated as permission. Disposition: **`unlicensed_reference_only`**.

## 14. Per-path decision counts

- `canonical`: **0**; `reference`: **33**; `quarantine`: **2**. Exactly one decision exists for every inventoried path.

## 15. Exact bounded-port candidate proposals

These **24** files are proposals for a later licensed, reviewed bounded port; this list is **not permission to import or transfer**.

| Path | SHA-256 | Bytes | Rationale |
|---|---|---:|---|
| `configs/sample.yaml` | `e955696f5bbb22c9561a3831c6df46cfb10db00d38951eb5a10a7f23aa1f9d45` | 324 | Candidate for isolated behavior/config/template review; reference-only pending license and downstream adaptation. |
| `make_papercut_panel.py` | `cce3933f62491bed5819dac5aa31a8cbd9a4905ddce207ef4a2528584e100396` | 33186 | Candidate for isolated behavior/config/template review; reference-only pending license and downstream adaptation. |
| `src/vyt/__init__.py` | `4b5b3e0b94452ad7eed18406c903d434fe8bf483b12c492dd5db80f3aedf068f` | 60 | Candidate for isolated behavior/config/template review; reference-only pending license and downstream adaptation. |
| `src/vyt/cli/__init__.py` | `308d99cff60eb8aa4cf3f4feb238d3050f0494e58551a805216cc61ca7cdbb1b` | 35 | Candidate for isolated behavior/config/template review; reference-only pending license and downstream adaptation. |
| `src/vyt/cli/__main__.py` | `9109b3da3c0203fb1c3cd03e9bf5988b93913143fa5282f2391d5b1006c2f9b1` | 1382 | Candidate for isolated behavior/config/template review; reference-only pending license and downstream adaptation. |
| `src/vyt/core/__init__.py` | `531d369d7381fba1caf05f88f5a26857f934009be8a4911dc3bb7230e62d0510` | 44 | Candidate for isolated behavior/config/template review; reference-only pending license and downstream adaptation. |
| `src/vyt/core/bridge.py` | `e6bc554244258b6ae14d7948f9a3d910672c343d55a874b0d172a0cc50459dbb` | 1531 | Candidate for isolated behavior/config/template review; reference-only pending license and downstream adaptation. |
| `src/vyt/core/compose.py` | `3202047822f51c94f8a1580455645dd25ca1bd5e16c9837c2e359f93099aa453` | 298 | Candidate for isolated behavior/config/template review; reference-only pending license and downstream adaptation. |
| `src/vyt/core/ingest.py` | `4866817aeb8e00afd75e068124c74946da77bf90df73ae80db5bafa163872537` | 2010 | Candidate for isolated behavior/config/template review; reference-only pending license and downstream adaptation. |
| `src/vyt/core/mask.py` | `3234e461ffc34827881bc7b4a37172e509c43121e1bf66a6198d356424a42c59` | 975 | Candidate for isolated behavior/config/template review; reference-only pending license and downstream adaptation. |
| `src/vyt/core/pack.py` | `37ad9690bfe11db445587c3506a601236ab7eb6c526ae35bec8e974755e62768` | 520 | Candidate for isolated behavior/config/template review; reference-only pending license and downstream adaptation. |
| `src/vyt/core/pipeline.py` | `82510542324e9790ac8bba80c8e613f6bf3e8c2bbb9a25fcf05577498afa929d` | 1725 | Candidate for isolated behavior/config/template review; reference-only pending license and downstream adaptation. |
| `src/vyt/core/preview.py` | `1cd47544913964adf1b66cd4549f8e8549fe59564c6dac6b1e257ed5fbad44cc` | 357 | Candidate for isolated behavior/config/template review; reference-only pending license and downstream adaptation. |
| `src/vyt/core/qa.py` | `57de28e0c295ad97f0d6ab5a4d64be48888cba11c2fcd96debeffdc892451535` | 483 | Candidate for isolated behavior/config/template review; reference-only pending license and downstream adaptation. |
| `src/vyt/core/render_pdf.py` | `cf6cdf079cac02802058f05fa76656f58f17d025a321cfca82b95ca7f9d97fa3` | 1187 | Candidate for isolated behavior/config/template review; reference-only pending license and downstream adaptation. |
| `src/vyt/core/render_pptx.py` | `009f453a10e9df2a55b5ef883f36a0a8ea74f6934bbd02abfb6bcc3a8942dfc5` | 841 | Candidate for isolated behavior/config/template review; reference-only pending license and downstream adaptation. |
| `src/vyt/core/tile.py` | `83ede9e6a2e1591ea423ebdccfe629d7a2c1ff26e8e8c50fd75218b6ccad3c50` | 5012 | Candidate for isolated behavior/config/template review; reference-only pending license and downstream adaptation. |
| `src/vyt/core/vectorize.py` | `4d00d286433e6102358aa048c31a9a6d3da5f814a431d3f75b0574f5b12aab32` | 585 | Candidate for isolated behavior/config/template review; reference-only pending license and downstream adaptation. |
| `src/vyt/utils/__init__.py` | `8c7d2784b7e0b669fffcdc3d7aa83c0b579377384fb7d250174e7b3b5b52c0dd` | 36 | Candidate for isolated behavior/config/template review; reference-only pending license and downstream adaptation. |
| `src/vyt/utils/io.py` | `9806bcbd6a86d5ea2b0b77e64f202e027aceb2745ccddcd75534e537428cba1e` | 470 | Candidate for isolated behavior/config/template review; reference-only pending license and downstream adaptation. |
| `src/vyt/utils/units.py` | `f274611d2c77378be5c1dadf8ba409300ea094ebb663502ba3cf5cde585d02f7` | 347 | Candidate for isolated behavior/config/template review; reference-only pending license and downstream adaptation. |
| `templates/cover.svg` | `15e585fc4e6d21eb75efa90eea76efb44ba3c943aab55a760ce3aac21997a47e` | 395 | Candidate for isolated behavior/config/template review; reference-only pending license and downstream adaptation. |
| `templates/instructions.md` | `8f32a535d075b12942c4b8eaf50c4584cabc55bbd25866c07453c37797eaf44c` | 284 | Candidate for isolated behavior/config/template review; reference-only pending license and downstream adaptation. |
| `templates/readme.txt` | `1c0d2cf54abac632ee6f086e1439f18457cd2c64195de0b3a97c12448706e7ab` | 284 | Candidate for isolated behavior/config/template review; reference-only pending license and downstream adaptation. |

## 16. Explicitly excluded generated/example outputs

- `input/.gitkeep` and `input/sample.png.xbase64` are quarantined as mutable-input/example material. Runtime products matching `build/**`, `*.log`, `*_original.png`, `*_panel.png`, `*_3x4_A4.pdf`, `*_3x4_A4.pptx`, previews, QA JSON, tiles, and ZIP packages are explicitly excluded; none is tracked at the pinned revision.

## 17. Blockers and unresolved evidence gaps

- Blocking: absent reuse license; stub/placeholder stages; no lock/hashes for transitive dependencies; native-library/tool/font assumptions; Windows-only wrappers; output/path and resource-limit hardening not evidenced; no executed behavioral/security tests permitted by this audit.
- Unresolved: authorship/provenance of each asset, compatibility of any future target licenses, exact native dependency versions, SVG/image parser threat model, and expected production-quality acceptance criteria.

## 18. Relevance to subsequent #18 and #12

- For follow-up `#18`, use the stage/boundary map to design a minimal portable CLI contract without copying source. For follow-up `#12`, use the papercut and template/asset candidate tables to scope independently authorized reimplementation and asset provenance checks. Neither follow-up may treat this audit as reuse authorization.

## 19. Outcome and permitted next transition

- Outcome: **`REFERENCE_ONLY`**. Permitted next transition: obtain explicit license/provenance evidence, then perform target-side design/reimplementation review against the exact hashes above. No source import, canonical designation, or production transfer is currently permitted.
