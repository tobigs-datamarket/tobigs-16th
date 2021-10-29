from flask import request
from flask import Flask
from flask_cors import CORS   # 외부에서 접속해도 에러가 나지 않게 보안 설정 적용
from model import model
import json

app = Flask(__name__)   # Flask 객체를 app에 할당. 이때,  __name__은 현재 실행 중인 모듈 이름(파일명)을 전달.
CORS(app)   # 외부에서 접속해도 에러가 나지 않게 보안 설정 적용

""" status check """
# @app.route() : 데코레이터 활용, 이때 app.route() 메서드 활용해서 라우팅 경로 설정.
# 서버로 접근할 때, 요청이 들어오면 아래 함수가 실행됨
# http://localhost:5000/ 가리킴. 기본적으로 flask에서는 5000번 포트 사용하기 때문.
@app.route("/")
def index():   # 위에서 라우팅한 주소에 대한 함수
    result = {
        'message': 'Status is OK.'
    }
    return json.dumps(result)   # json.dumps() : 파이썬 객체를 json 문자열로 변환

""" ------------ """

""" model predict """
# 클라이언트에서 서버로 POST 요청 보내기 (이때, methods=['POST']를 통해 POST 요청만 허용)
# 참고 1) GET : 데이터를 url에 쿼리스트링을 통해 보냄 VS POST : 데이터를 http body에 포함시켜서 보냄
# 쿼리스트링 : URL의 끝에 ?와 함께 이름과 값으로 쌍을 이루는 요청 파라미터 (파라미터가 여러 개이면 &로 연결)
# 참고 2) GET은 전송할 데이터 양이 적을 때, POST는 많을 때 주로 사용
@app.route('/predict', methods=['POST'])
def predict_model(): # 위에서 라우팅한 주소에 대한 함수

    print("Predict method Start..")   # 화면 출력
    params = request.get_json()   # flask에서 json 데이터를 받아 처리
    # input(params['height'], params['weight'])에 대해 예측 수행 후 예측 결과를 pred에 할당
    pred = model.predict(params['height'], params['weight'])
    # message와 예측 결과를 딕셔너리 형태로 result에 할당
    result = {
        'message': 'Succefully Predicted',
        'result': pred
    }

    print("Predict Finish ..")   # 화면 출력
    print(result)   # 화면 출력

    return json.dumps(result)
""" ------------- """


if __name__ == "__main__":   # 인터프리터에서 직접 실행했을 경우에만 app 실행하도록 하는 코드
    app.run();   # app을 서버에서 실행
