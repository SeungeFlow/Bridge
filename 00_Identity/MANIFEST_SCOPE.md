# Manifest Scope

`00_Identity/FILE_SHA256SUMS.txt`는 자기 자신을 제외한 Package 내부 모든 파일의 SHA-256을 기록한다.

- `PACKAGE_TREE.txt`: Manifest에 포함
- `BUILD_REPORT.md`: Manifest에 포함
- `FILE_SHA256SUMS.txt`: 자기참조 방지를 위해 제외
- ZIP 외부파일: Manifest 범위 밖
