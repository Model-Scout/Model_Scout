---
license: cc0-1.0
task_categories:
  - text-classification
  - feature-extraction
language:
  - en
  - zh
  - es
  - fr
  - de
  - ja
  - ko
  - pt
  - ru
  - ar
configs:
- config_name: default
  data_files:
  - split: train
    path: "data/*.parquet"
  default: true
pretty_name: "Phishing & Malware Website Snapshots"
size_categories:
  - 100K<n<1M
---

# Phishing & Malware Website Snapshots

136,414 phishing and malware website snapshots captured by a headless Chromium browser between July 24 and August 15, 2024. URLs were confirmed or high-confidence phishing/malware at the time of collection, though some hosts had already been blocked or taken down when the snapshot was taken. Each row contains the full HTML source, extracted visible text, complete network traffic from HAR recording, parsed page features, and resource fingerprints.

Collected in mid-2024, published March 2026. All of the phishing domains and infrastructure captured here are long dead. The value is in page content, kit patterns, and network behavior rather than live IOCs.

55,339 unique domains, 23,588 of which appear more than once.

## Use Cases

- Training phishing/malware classifiers (URL-level, page-level, or multimodal)
- Static rule generation for phishing kit detection
- Threat intelligence on phishing infrastructure and hosting
- Feature engineering for browser-based detection extensions
- Academic research on web-based social engineering

## Schema

Single flat Parquet table, 42 columns per row. Nested columns use Parquet `list<struct>` types.

### Identification & Metadata

| Column | Type | Description |
|---|---|---|
| `id` | string | Unique archive ID (`hostname_rand5`) |
| `domain` | string | Target hostname |
| `url` | string | Original URL visited |
| `scan_timestamp` | string | ISO timestamp of capture |
| `language` | string | Declared page language |

### Page Content

| Column | Type | Description |
|---|---|---|
| `html` | large_string | Full page HTML source |
| `html_length` | int64 | HTML byte length |
| `extracted_text` | large_string | Visible text via trafilatura |
| `text_length` | int64 | Extracted text byte length |
| `title` | string | Page `<title>` content |
| `meta_tags` | list\<struct\> | All `<meta>` tags (name + content) |
| `html_comments` | list\<string\> | HTML comments (useful for kit signatures) |

### Scripts & Styles

| Column | Type | Description |
|---|---|---|
| `external_script_urls` | list\<string\> | External `<script src>` URLs |
| `inline_scripts` | list\<large_string\> | Full inline JavaScript |
| `inline_scripts_count` | int32 | Number of inline `<script>` blocks |
| `inline_scripts_total_bytes` | int64 | Total inline JS size |
| `external_css_urls` | list\<string\> | External stylesheet URLs |
| `inline_style_count` | int32 | Number of inline `<style>` blocks |

### Forms & Inputs

| Column | Type | Description |
|---|---|---|
| `form_actions` | list\<string\> | `<form action>` URLs |
| `form_count` | int32 | Number of `<form>` elements |
| `input_fields` | list\<struct\> | Input fields with type, name, placeholder |
| `input_count` | int32 | Number of `<input>` elements |
| `has_password_field` | bool | Page contains a password input |
| `has_file_upload` | bool | Page contains a file upload input |

### Linked Resources

| Column | Type | Description |
|---|---|---|
| `favicon_urls` | list\<string\> | Favicon link hrefs |
| `favicon_hashes` | list\<struct\> | MD5/SHA256 of favicon content |
| `anchor_hrefs` | list\<string\> | All `<a href>` targets |
| `image_srcs` | list\<string\> | All `<img src>` URLs |
| `iframe_srcs` | list\<string\> | All `<iframe src>` URLs |
| `external_domains` | list\<string\> | Unique external domains referenced |

### Network & HTTP

| Column | Type | Description |
|---|---|---|
| `final_url` | string | URL after redirects |
| `redirect_chain` | list\<string\> | Full redirect path |
| `server_header` | string | `Server` response header |
| `x_powered_by` | string | `X-Powered-By` response header |
| `content_security_policy` | string | `Content-Security-Policy` header |
| `http_status` | int32 | Final HTTP status code |
| `network_requests` | list\<struct\> | All HAR entries (see below) |
| `network_request_count` | int32 | Total network requests |
| `resource_hashes` | list\<struct\> | MD5/SHA256 of served resources (see below) |

### Availability Flags

| Column | Type | Description |
|---|---|---|
| `has_html` | bool | Row has HTML content |
| `has_har` | bool | Row has HAR data |
| `has_text` | bool | Row has extracted text |

### Nested Struct: `network_requests`

Each entry: `method`, `url`, `url_domain`, `status`, `mime_type`, `response_size`, `server_ip`, `is_redirect`, `redirect_url`, `response_headers` (list of key/value structs), `request_cookies`, `response_cookies` (with name, domain, httpOnly, secure).

### Nested Struct: `resource_hashes`

Each entry: `url`, `mime_type`, `resource_type` (script / style / image / font / document / other), `body_size`, `body_md5`, `body_sha256`, `is_favicon`.

### Nested Struct: `input_fields`

Each entry: `type`, `name`, `placeholder`, `id`, `class_name`, `required`, `autocomplete`.

### Nested Struct: `meta_tags`

Each entry: `name`, `content`.

## Statistics

| Metric | Value |
|---|---|
| Rows | 136,414 |
| Unique domains | 55,339 |
| Multi-snapshot domains | 23,588 |
| Rows with HTML | 135,407 (99.3%) |
| Rows with HAR data | 126,747 (92.9%) |
| Rows with extracted text | 134,114 (98.3%) |
| Rows with forms | 52,089 (38.2%) |
| Rows with password fields | 33,199 (24.3%) |
| Total resource hashes | 2,349,290 |
| Median network requests/row | 11 |
| Mean network requests/row | 20.2 |
| Median HTML size | 25 KB |
| Mean HTML size | 124 KB |
| Total inline JS | 6.1 GB (uncompressed) |
| Shards | 28 |
| Total size on disk | 2.0 GB (zstd level 19) |

### Language Distribution (top 10)

| Language | Rows |
|---|---|
| en | 50,925 |
| en-US | 9,037 |
| ru | 7,926 |
| fr | 3,618 |
| en-us | 1,759 |
| zh-CN | 1,483 |
| ja | 1,378 |
| (empty) | 1,290 |
| de | 1,226 |
| fr-FR | 777 |

## Collection Method

A headless Chromium browser (Playwright) running inside Docker, controlled by a Flask API, visited each URL. Per visit:

1. Navigate to URL with HAR recording active
2. Save rendered HTML (`index.html`)
3. Capture all network requests and responses (`requests.har`, HAR 1.2 format)
4. Extract visible text via trafilatura (`trafilatura.txt`)
5. Compress into a `.7z` archive

During conversion to Parquet, HAR response bodies were hashed (MD5 + SHA256) rather than stored. This reduced the dataset from ~76 GB of raw archives to 2 GB of compressed Parquet. Full HTML and inline JavaScript are preserved.

Archives containing blocked or error pages were excluded. Filtered titles: "403 Forbidden", "Not found", "Attention Required! | Cloudflare", "Suspected phishing site | Cloudflare". Empty and corrupted archives were also removed. 31,793 archives were filtered in total.

## Safety

This dataset contains snapshots of malicious websites. The HTML and scripts include:

- Credential harvesting forms that mimic legitimate services
- Obfuscated JavaScript for redirects, fingerprinting, or exploit delivery
- References to attacker-controlled infrastructure

Do not execute JavaScript or render HTML from this dataset in a browser without sandboxing. This data is for defensive security research.

## License

CC0-1.0
