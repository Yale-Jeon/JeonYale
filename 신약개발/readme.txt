화합물의 대사안정성 학습용 데이터 3,498종을 이용해 예측모델을 개발

개발한 모델로 경진용 데이터 483종 화합물을 이용하여 대사안정성 예측값을 제출


Dataset Info.

1. train.csv

3498개 화합물 정보
id: 샘플 고유 id
SMILES: 화합물의 분자 구조
화합물의 물성 관련 정보 (LogD의 경우 pH값 7.4에서 계산)
MLM(Mouse Liver Microsome) 포함
HLM(Human Liver Microsome) 포함
HLM 및 MLM은 간 및 마우스의 간 대사효소와 화합물을 30분 동안 반응시킨 후, 
대사되지 않고 남아있는 화합물의 양을(%) LC-MS/MS로 측정함으로써 화합물의 간 대사효소에 대한 안정성을 평가한 데이터


2. test.csv

483개 화합물 정보
id: 샘플 고유 id
SMILES: 화합물의 분자 구조
화합물의 물성 관련 정보 (LogD의 경우 pH값 7.4에서 계산)


3. sample_submission.csv

id: 샘플 고유 id
MLM: test 데이터에 대해서 MLM을 예측한 값
HLM: test 데이터에 대해서 HLM을 예측한 값