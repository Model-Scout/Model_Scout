"""Stage 2가 HF 응답에서 사실을 뽑고 출처를 기록하는 resolver 모음.

``ai/backfill``의 일회성 로직이 여기로 들어왔다. 앞으로 "정규 파이프라인 →
백필"이 아니라, 처음부터 모든 모델이 safetensors·GGUF·config·siblings를
함께 본다.

데이터 계약은 ``ai/contract/``에 있다.
"""
