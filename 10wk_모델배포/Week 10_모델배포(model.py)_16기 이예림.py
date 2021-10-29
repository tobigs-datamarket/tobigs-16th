from joblib import load
import numpy as np

# joblib.load() : 파일(또는 경로)에 저장되어 있던 object를 파이썬 object로 반환
model = load('./model/model_params/bmiRegressor')

def predict(height: int, weight: int):   
    print("Model Start")   # 화면 출력
    # input(height, weight)에 대해 예측 수행 후 예측 결과를 result에 할당
    result = model.predict([[height, weight]])
    print("Model Finish")   # 화면 출력
    # numpy의 item 메서드 : 배열의 요소를 표준 파이썬 scalar로 복사한 후 반환
    return result.item()
