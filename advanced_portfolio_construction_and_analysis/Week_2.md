# Section 1
## 차원의 저주
### 개념
Factor가 N개가 되면 필요한 parameter
-> N개의 Expected Return
-> N개의 Volatility
-> N(N-1)/2 개의 Correlation

### 해결법
1. Factor의 개수를 줄인다
-> 쉽지만 risky하고 실현 불가능한 해결책

2. Sample Estimate

3. Constant Correlation Model
-> Correlation Parameter ρ = 상수로 가정
-> 여러개의 Parameter를 잘못 추정할 바에야, 하나의 Parameter를 정확히 추정하자

## Factor Model에서의 Covariance Matrix 추정
### 가정
두 자산의 잔차가 uncorrelated 되었다
(= 각 자산의 factor로 설명되지 않는 요소들이 uncorrelated 하다)
(= Cov(ε1ε2) = 0)

### 성공의 요건
Factor 모델의 설명력이 좋아서, 잔차가 얼마 없어야만 잘 통함

## Honey I Shrunk the Covariance Matrix
### Parameter Estimation 의 Trade off
모델을 사용하면 : 제시된 모델 자체의 리스크 존재
샘플에서 추정하면 : 샘플의 리스크, 계산 복잡도 증가

### Statistical Shrinkage Estimator

-> 델타를 어떻게 찾을 것인가가 논문의 내용

### Weight Contraints

-> Portolio Weight에 최대/최소 제약을 거는 것이 Statistical Shrinkage와 동일하다