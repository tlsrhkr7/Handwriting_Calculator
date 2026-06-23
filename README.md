# Handwriting Calculator

손으로 쓴 수식을 LaTeX로 변환하고 자동으로 계산해 주는 공학용 계산기입니다. 태블릿 캔버스에 직접 쓰거나 종이에 적은 수식을 사진으로 찍어 업로드할 수 있습니다.

## 개요

공학 수업에서 다루는 복잡한 수식은 버튼·키보드 입력으로 다시 쓰기 번거롭습니다. 손글씨를 그대로 인식해 계산함으로써 입력 시간을 줄이고 공학 계산을 직관적으로 만드는 것이 목표입니다.

## 주요 기능

- 손글씨 캔버스 입력 / 손글씨 사진 이미지 업로드
- 변환된 LaTeX 수식 미리보기
- 원클릭 계산 및 예외 처리

## 동작 방식

```
[손글씨 / 이미지] → [Mathpix OCR] → [LaTeX] → [latex2sympy2] → [SymPy 계산] → [결과]
```

- Mathpix API: 수식 인식 특화 OCR
- latex2sympy2: LaTeX → SymPy 변환
- SymPy: 수식 평가

## 기술 스택

Python · Ubuntu · Mathpix API · SymPy · latex2sympy2

## 설치 및 실행

```bash
pip install sympy latex2sympy2 requests
```

1. Mathpix API 키 발급 후 환경 변수(MATHPIX_APP_ID, MATHPIX_APP_KEY)로 설정 (키는 커밋 금지)
2. 입력 방식 선택 (이미지 / 캔버스 / 키보드)
3. 생성된 LaTeX 확인 후 계산

## 향후 계획

- 행렬, 라플라스 변환 등 고급 기능 추가
- 수학 기호 버튼 제공, 카메라·클립보드 입력 지원
- 인식·계산 속도 최적화
