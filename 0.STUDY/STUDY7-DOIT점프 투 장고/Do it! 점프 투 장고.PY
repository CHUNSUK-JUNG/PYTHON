# 출처 [https://wikidocs.net/book/4223, Do it! 점프 투 장고]


# [2장 장고의 기본 요소 익히기!]
# 이 장에서는 장고 개발을 하는 데 필요한 기본 내용을 모두 다룰 것이다. 여러분이 앞으로 만들 ‘파이보’가 완성된 빌딩이라면 이 장은
# 기초 공사에 해당한다. 기초 공사를 탄탄히 하여 안전한 빌딩의 토대를 마련해 보자.
# 이 장의 목표
# - urls.py 파일을 이용해 URL과 매핑되는 뷰 함수를 관리한다.
# - 장고 ORM을 이용해 데이터베이스를 제어한다.
# - 파이보 게시판에 질문 목록과 질문 상세 기능을 만든다.

# [2-04 질문 목록과 질문 상세 기능 구현하기]
# [완성 소스] : github.com/pahkey/djangobook/tree/2-04
# 이제 파이보의 핵심 기능을 구현할 것이다. 바로 질문 목록과 질문 상세 기능이다. 우선은 /pybo/ 에 접속하면 질문을 모두 조회할 수 있는 기능을
# 구현해 볼 것이다.
# 지금은 localhost:8000/pybo에 접속하면 '안녕하세요 pybo에 오신것을 환영합니다.'가 출력되는 상태이다.
# 질문 목록 기능 구현하기
# [1] Question 모델 데이터 작성일시 역순으로 조회하기
# [2] render로 화면 출력하기
# [3] 템플릿을 모아 저장할 디렉터리 만들기
# [4] 템플릿 디렉터리 위치 config/settings.py에 등록하기
# [5] 템플릿 파일 만들기
# [6] 질문 목록이 잘 출력되는지 확인해 보기
# 질문 상세 기능 구현하기
# [1] 질문 목록에서 아무 질문이나 눌러 보기
# [2] pybo/urls.py 열어 URL 매핑 추가하기
# [3] pybo/views.py 열어 화면 추가하기
# [4] pybo/question_detail.html 작성하기
# [5] 질문 상세 페이지에 접속해 보기
# 오류 화면 구현하기
# [1] 잘못된 주소에 접속해 보기
# [2] 페이지가 존재하지 않음(404 페이지) 출력하기
# [3] 404 페이지 출력 확인하기
# 질문 목록 기능 구현하기
# 질문 목록 조회를 위해 pybo/views.py 파일을 열어 코드를 조금씩 수정해 보자.
# [1] Question 모델 데이터 작성일시 역순으로 조회하기
# Question 모델을 임포트해 Question 모델 데이터를 작성한 날짜의 역순으로 조회하기 위해 order_by 함수를 사용했다. 
# 조회한 Question 모델 데이터는 context 변수에 저장했다. context 변수는 조금 후에 설명할 render 함수가 템플릿을 HTML로 변환하는 과정에서
# 사용되는 데이터이다.
# [파일이름: C:/projects/mysite/pybo/views.py]
# from django.http import HttpResponse
# # ---------------------------------- [edit] ---------------------------------- #
# from .models import Question
# # ---------------------------------------------------------------------------- #


# def index(request):
# # ---------------------------------- [edit] ---------------------------------- #
#     """
#     pybo 목록 출력
#     """
#     question_list = Question.objects.order_by('-create_date')
#     context = {'question_list': question_list}
# # ---------------------------------------------------------------------------- #    
#     return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")
# order_by 함수는 조회한 데이터를 특정 속성으로 정렬하며, '-create_date'는 - 기호가 앞에 붙어 있으므로 작성일시의 역순을 의미한다.
# [2] render로 화면 출력하기
# 이제 조회한 Question 모델 데이터를 템플릿 파일을 사용하여 화면에 출력할 수 있는 render 함수를 사용해 보자.
# [파일이름: C:/projects/mysite/pybo/views.py]
# # ---------------------------------- [edit] ---------------------------------- #
# from django.shortcuts import render
# # ---------------------------------------------------------------------------- #
# from .models import Question
# def index(request):
#     """
#     pybo 목록 출력
#     """
#     question_list = Question.objects.order_by('-create_date')
#     context = {'question_list': question_list}
# # ---------------------------------- [edit] ---------------------------------- #    
#     return render(request, 'pybo/question_list.html', context)
# # ---------------------------------------------------------------------------- #    
# render 함수는 context에 있는 Question 모델 데이터 question_list를 pybo/question_list.html 파일에 적용하여 HTML 코드로 변환한다. 
# 그리고 장고에서는 이런 파일(pybo/question_list.html)을 템플릿이라 부른다. 템플릿은 장고의 태그를 추가로 사용할 수 있는 HTML 파일이라
# 생각하면 된다. 템플릿에 대해서는 바로 다음 실습 과정을 통해 자연스럽게 알아보겠다.
# [3] 템플릿을 모아 저장할 디렉터리 만들기
# 템플릿을 만들기 전에 템플릿을 저장할 디렉터리를 루트 디렉터리 바로 밑에 만들자.
# 루트 디렉터리는 장고 프로젝트 디렉터리(C:/projects/mysite)를 의미한다.
# [명령 프롬프트]
# (mysite) C:\projects\mysite>mkdir templates
# [4] 템플릿 디렉터리 위치 config/settings.py에 등록하기
# 위에서 만든 템플릿 디렉터리를 장고 config/settings.py 파일에 등록하자. config/settings.py 파일을 열어 TEMPLATES 항목을 다음과 같이 수정하자.
# [파일이름: C:/projects/mysite/config/settings.py]
# (... 생략 ...)
# TEMPLATES = [
#     {
#         (... 생략 ...)
# # ---------------------------------- [edit] ---------------------------------- #
#         'DIRS': [BASE_DIR / 'templates'],
# # ---------------------------------------------------------------------------- #
#         (... 생략 ...)
#     },
# ]
# (... 생략 ...)
# DIRS에는 템플릿 디렉터리를 여러 개 등록할 수 있다. 다만 현재 우리가 개발하는 파이보는 1개의 템플릿 디렉터리를 쓸 것이므로
# BASE_DIR / 'templates'와 같이 1개의 디렉터리만 등록하자. 현재 BASE_DIR은 C:/projects/mysite이므로 templates만 더 붙여 
# C:/projects/mysite/templates를 반환한다.
# 장고는 앱 하위에 있는 templates 디렉터리를 자동으로 템플릿 디렉터리로 인식한다
# 장고는 DIRS에 설정한 디렉터리 외에도 특정 앱(예를 들어 pybo 앱) 디렉터리 하위에 있는 templates라는 이름의 디렉터리를 자동으로 
# 템플릿 디렉터리로 인식한다. 예를 들어 다음과 같은 pybo 앱 디렉터리 밑의 templates 디렉터리는 별다른 설정을 하지 않아도 템플릿 
# 디렉터리로 인식된다.
# C:\projects\mysite\pybo\templates
# 하지만 필자는 이 방법을 권장하지 않는다. 왜냐하면 하나의 사이트에서 여러 앱을 사용할 때 여러 앱의 화면을 구성하는 템플릿은 한 
# 디렉터리에 모아 관리하는 편이 여러모로 좋기 때문이다. 예를 들어 여러 앱이 공통으로 사용하는 공통 템플릿을 어디에 저장해야 할지 
# 생각해 보면 왜 이런 방법을 선호하는지 쉽게 이해될 것이다.
# 그래서 파이보는 템플릿 디렉터리를 mysite/pybo/templates와 같은 방식이 아니라 mysite/templates/pybo 같은 방식으로 관리하며, 
# 공통으로 사용하는 템플릿은 C:/projects/mysite/templates에 저장한다.
# 구분	경로
# 공통 템플릿 디렉터리	C:/projects/mysite/templates
# pybo 앱 템플릿 디렉터리	C:/projects/mysite/templates/pybo
# [5] 템플릿 파일 만들기
# 위에서 만든 템플릿 디렉터리를 참고하여 question_list.html 템플릿 파일을 mysite/templates/pybo/ 디렉터리에 생성하자.
# pybo 디렉터리를 templates 안에 새로 만들어 파일을 추가해야 한다.
# [templates/pybo/ 위치에 저장한 question list.html 파일]
# 그리고 템플릿 파일을 다음과 같이 작성하자.
# [파일이름: C:/projects/mysite/templates/pybo/question_list.html]
# <!-- ------------------------------- [edit] -------------------------------- -->
# {% if question_list %}
#     <ul>
#     {% for question in question_list %}
#         <li><a href="/pybo/{{ question.id }}/">{{ question.subject }}</a></li>
#     {% endfor %}
#     </ul>
# {% else %}
#     <p>질문이 없습니다.</p>
# {% endif %}
# <!-- ----------------------------------------------------------------------- -->
# {% if question_list %}라는 문장이 눈에 띌 것이다. 바로 이것이 템플릿 태그이다. 템플릿 태그는 {% 와 %}로 둘러싸인 문장을 말한다.
# 다음 표에 정리한 템플릿 태그의 의미를 살펴보면 파이썬 문법과 크게 다르지 않음을 알 수 있다. 템플릿 태그는 따로 문법을 설명하지 않고 
# 그때그때 필요할 때마다 설명하겠다.
# 템플릿 태그	의미
# {% if question_list %}	question_list가 있다면
# {% for question in question_list %}	question_list를 반복하며 순차적으로 question에 대입
# {{ question.id }}	for 문에 의해 대입된 question 객체의 id 출력
# {{ question.subject }}	for 문에 의해 대입된 question 객체의 subject 출력
# - 템플릿 태그에서 사용된 question_list가 바로 render 함수에서 템플릿으로 전달한 Question 모델 데이터이다.
# - 만약 템플릿 태그의 자세한 내용이 궁금하다면 장고 공식 문서를 참고하자.
# - 템플릿 장고 공식 문서 주소: docs.djangoproject.com/en/3.0/topics/templates
# 템플릿 태그! 3가지 유형만 정리하면 끝!
# 장고의 템플릿 태그는 분기, 반복, 객체 출력이라는 3가지 유형만 알면 된다. 분기 템플릿 태그는 다음과 같다. 문법을 보면 알겠지만 파이썬의
# if 문과 다르지 않다. 다만 if 문이 끝나는 부분에 {% endif %}를 사용하는 점만 다르다.
# {% if 조건문1 %}
#     <p>조건문1에 해당되는 경우</p>
# {% elif 조건문2 %}
#     <p>조건문2에 해당되는 경우</p>
# {% else %}
#     <p>조건문1, 2에 모두 해당되지 않는 경우</p>
# {% endif %}
# 반복 템플릿 태그는 다음과 같다. 이 역시 파이썬의 for 문과 다르지 않으며, 역시 for 문의 마지막은 {% endfor %}로 닫아야 한다.
# {% for item in list %}
#     <p>순서: {{ forloop.counter }} </p>
#     <p>{{ item }}</p>
# {% endfor %}
# 또한 반복 템플릿 안에서는 forloop 객체를 사용할 수도 있다. forloop 객체는 반복 중 유용한 값을 제공한다.
# forloop 객체 속성	설명
# forloop.counter	for 문의 순서로 1부터 표시
# forloop.counter0	for 문의 순서로 0부터 표시
# forloop.first	for 문의 첫 번째 순서인 경우 True
# forloop.last	for 문의 마지막 순서인 경우 True
# 객체 출력 템플릿 태그는 다음과 같다. 객체에 속성이 있으면 파이썬과 동일한 방법으로 점(.) 연산자를 사용한다.
# {{ question }}
# {{ question.id }}
# {{ question.subject }}
# [6] 질문 목록이 잘 출력되는지 확인해 보기
# 템플릿 디렉터리를 추가한 상태이므로 장고 개발 서버를 다시 시작해 /pybo/에 접속하자. 장고 개발 서버를 다시 시작하지
# 않으면 장고가 템플릿 디렉터리를 인식하지 못해 오류가 발생한다.
# [/pybo/에서 볼 수 있는 질문 목록]
# 화면을 보면 이전에 등록한 질문 2건이 보인다. 직접 장고 셸이나 장고 Admin에서 다른 질문도 추가해 보면서 질문 목록이 
# 잘 만들어지는지 테스트해 보기 바란다.
# 질문 상세 기능 구현하기
# [1] 질문 목록에서 아무 질문이나 눌러 보기
# 질문 목록 화면에서 아무 질문(예를 들면 Django Model Question)이나 눌러 보자. 그러면 다음과 같은 오류 화면이 나타난다.
# [질문 목록에서 질문을 눌러 이동한 화면(오류 화면)]
# 오류 화면이 나타난 이유는 /pybo/2/ 에 대한 URL 매핑을 추가하지 않았기 때문이다.
# 질문을 눌렀을 때 /pybo/2/와 같은 주소로 이동한 이유는 템플릿에서 href 엘리먼트에 link 속성을
# <a href="/pybo/{{ question.id }}/">으로 지정했기 때문이다.
# [2] pybo/urls.py 열어 URL 매핑 추가하기
# /pybo/2/의 숨은 의도는 'Question 모델 데이터 중 id값이 2인 데이터를 조회하라'이다. 이 의도에 맞게 결과 화면을 보여줄 수 있도록 
# pybo/urls.py 파일에서 path('<int:question_id>/', views.detail) URL 매핑을 추가하자.
# [파일이름: C:/projects/mysite/pybo/urls.py]
# from django.urls import path
# from . import views
# urlpatterns = [
#     path('', views.index),
# # ---------------------------------- [edit] ---------------------------------- #
#     path('<int:question_id>/', views.detail),
# # ---------------------------------------------------------------------------- #
# ]
# /pybo/2/가 요청되면 이 매핑 규칙에 의해 /pybo/<int:question_id>/가 적용되어 question_id에 2라는 값이 저장되고 views.detail 함수가 실행된다.
# - 장고는 pybo/까지는 config/urls.py의 URL 매핑을, pybo/에 이은 2/는 pybo/urls.py의 URL 매핑을 참고할 것이다.
# - int:는 question_id에 숫자가 매핑되었음을 의미한다.
# [3] pybo/views.py 열어 화면 추가하기
# pybo/views.py 파일을 열어 detail 함수를 추가하자.
# [파일이름: C:/projects/mysite/pybo/views.py]
# (... 생략 ...)
# # ---------------------------------- [edit] ---------------------------------- #
# def detail(request, question_id):
#     """
#     pybo 내용 출력
#     """
#     question = Question.objects.get(id=question_id)
#     context = {'question': question}
#     return render(request, 'pybo/question_detail.html', context)
# # ---------------------------------------------------------------------------- #
# 추가된 내용은 앞에서 만든 index 함수와 크게 다르지 않다. 다만 detail 함수의 매개변수 question_id가 추가된 점이 다르다.
# 바로 이것이 URL 매핑에 있던 question_id이다. 즉, /pybo/2/ 페이지가 호출되면 최종으로 detail 함수의 매개변수 question_id에 2가 전달된다.
# [4] pybo/question_detail.html 작성하기
# 위에서 render 함수가 question_detail.html 파일을 사용하고 있으므로 이에 대한 작업도 해야 한다. templates/pybo 디렉터리에 
# question_detail.html 파일을 만든 후 다음처럼 코드를 작성하자.
# [파일이름: C:/projects/mysite/templates/pybo/question_detail.html]
# <!-- ------------------------------- [edit] -------------------------------- -->
# <h1>{{ question.subject }}</h1>
# <div>
#     {{ question.content }}
# </div>
# <!-- ----------------------------------------------------------------------- -->
# {{ question.subject }}, {{ question.content }}의 question 객체는 detail 함수에서 render 함수에 전달한 context에 저장한 데이터이다.
# [5] 질문 상세 페이지에 접속해 보기
# /pybo/2/에 접속해 보자. 그러면 질문 상세 화면이 나타난다! 축하한다!
# [/pybo/2/에 제대로 접속된 화면]
# 오류 화면 구현하기
# 지금까지 질문 목록, 질문 상세 기능을 구현했다. 그런데 사용자가 잘못된 주소에 접속하면 어떻게 처리해야 할까?
# [1] 잘못된 주소에 접속해 보기
# /pybo/30/에 접속해 보자. 그러면 다음과 같은 DoesNotExist 오류 화면이 나온다.
# [/pybo/30/ 페이지 호출 시 나타나는 오류 화면]
# 당연한 오류이다. question_id가 30인 데이터를 조회하는 Question.object.get(id=30)에서 오류가 발생했기 때문이다.
# - 참고로 현재는 config/settings.py의 DEBUG 항목이 True로 설정되어 있어 개발자에게 여러 정보를 알려 주는 오류 화면이 나타난다. 
# 그런데 실제 서비스 화면에는 그런 중요한 정보가 표현되면 안 된다. 그래서 서비스를 할 때는 DEBUG 항목을 False로 설정한다.
# - cofing/settings.py의 DEBUG 항목을 False로 설정하는 부분은 4장에서 자세히 다룬다.
# [2] 페이지가 존재하지 않음(404 페이지) 출력하기
# 존재하지 않는 페이지에 접속하면 오류 대신 404 페이지를 출력하도록 detail 함수를 수정하자. Question.objects.get(id=question_id)를 
# get_object_or_404(Question, pk=question_id)로 수정하면 된다.
# [파일이름: C:/projects/mysite/pybo/views.py]
# # ---------------------------------- [edit] ---------------------------------- #
# from django.shortcuts import render, get_object_or_404
# # ---------------------------------------------------------------------------- #
# (... 생략 ...)
# def detail(request, question_id):
#     """
#     pybo 내용 출력
#     """
# # ---------------------------------- [edit] ---------------------------------- #    
#     question = get_object_or_404(Question, pk=question_id)
# # ---------------------------------------------------------------------------- #    
#     context = {'question': question}
#     return render(request, 'pybo/question_detail.html', context)
# get_object_or_404 함수는 모델의 기본키를 이용하여 모델 객체 한 건을 반환한다. pk에 해당하는 건이 없으면 오류 대신 404 페이지를 반환한다.
# [3] 404 페이지 출력 확인하기
# /pybo/30/에 접속하면 404 페이지가 출력된다.
# [get_object_or_404 함수로 나타나는 404 페이지]
# 404 페이지가 무엇인가요?
# 웹 브라우저는 HTTP 요청을 하고, 장고는 그 요청에 응답을 한다. 보통의 경우에는 성공을 의미하는 200 응답 코드가 자동으로 반환된다. 
# 하지만 요청하는 페이지가 없거나 서버에서 오류가 발생하면 다음과 같은 응답 코드가 반환된다.
# 오류코드	설명
# 200	성공
# 500	서버오류(Internal Server Error )
# 404	페이지 존재하지 않음(Not Found)
# 장고 제네릭뷰 간단 소개
# 제네릭뷰(generic view)는 목록 조회나 상세 조회처럼 특정 패턴이 있는 뷰를 작성할 때 사용하는 매우 편리한 기능이다. 
# 하지만 장고 입문자에게는 제네릭뷰의 실행 방식이 무척 이해하기 어렵다. 여러분에게는 제네릭뷰가 오히려 장고 학습에 혼란을 줄 수 
# 있으므로 코너로 소개한다. 눈으로 코드를 살펴보기만 하자. 만약 우리가 views.py 파일에 작성한 index 함수나 detail 함수를 제네릭뷰로 
# 변경하면 다음처럼 간략하게 작성할 수 있다.
# [제네릭뷰 예시: view.py]
# class IndexView(generic.ListView):
#     """
#     pybo 목록 출력
#     """
#     def get_queryset(self):
#         return Question.objects.order_by('-create_date')
# class DetailView(generic.DetailView):
#     """
#     pybo 내용 출력
#     """
#     model = Question
# IndexView 클래스가 index 함수를 대체하고 DetailView 클래스가 detail 함수를 대체했다고 생각하면 된다. 
# IndexView 클래스는 템플릿명이 명시적으로 지정되지 않으면 자동으로 모델명_list.html를 템플릿명으로 사용한다. 
# 정리하자면 Question 모델을 사용하는 IndexView 클래스는 question_list.html, DetailView 클래스는 question_detail.html을 템플릿명으로 사용한다.
# 이어서 urls.py 파일은 다음과 같이 변경해야 한다.
# [제네릭뷰 예시: urls.py]
# from django.urls import path
# from . import views
# app_name = 'pybo'
# urlpatterns = [
#     path('', views.IndexView.as_view()),
#     path('<int:pk>/', views.DetailView.as_view()),
# ]
# 이렇듯 단순 모델의 목록 조회나 상세 조회는 제네릭뷰를 사용하면 매우 간편하다. 단 제네릭뷰는 복잡한 문제를 해결할 때 오히려 개발 난이도를
# 높이는 경우도 있으니 주의해야 한다.

# [2-03 개발 편의를 제공하는 장고 Admin]
# [완성 소스] : github.com/pahkey/djangobook/tree/2-03
# 필자가 장고를 처음 접하고 가장 깜짝 놀란 기능이 바로 장고 Admin이다. 장고 Admin은 한 문장으로 표현하기 어려울 정도로 개발자에게 마법 같은 
# 기능을 제공한다. 여기서는 장고 Admin에 대해 알아보자.
# 장고 Admin 사용하기
# [1] 슈퍼 유저 생성하기
# [2] 장고 Admin에 접속해 로그인하기
# [3] 장고 Admin에서 모델 관리하기
# [4] 장고 Admin 새로고침 하기
# [5] Question 모델 데이터 추가하기
# [6] 장고 Admin에 데이터 검색 기능 추가하기
# [7] 장고 Admin에서 데이터 검색해 보기
# 장고 Admin 사용하기
# 장고 Admin을 사용하려면 슈퍼 유저를 먼저 생성해야 한다. 슈퍼 유저는 쉽게 말해 장고 운영자 계정이라 생각하면 된다.
# [1] 슈퍼 유저 생성하기
# 명령 프롬프트에서 python manage.py createsuperuser 명령을 실행하여 슈퍼 유저를 생성하자. 사용자 이름에는 admin을 입력하고
# (다른 것을 입력해도 된다), 이메일 주소는 가상의 이메일 주소를 적는다. 비밀번호는 여러분이 기억하기 쉬운 것으로 입력하자. 
# 이때 단순한 구성의 비밀번호를 입력하면 경고 메시지가 나올 텐데, 이를 무시하는 옵션으로 'Bypass password validation and create user anyway?'의 
# 질문에 y를 입력해 답하자.
# 여기서는 학습을 위해 비밀번호를 단순하게 입력했다. 만약 실제 사이트를 운영할 계획이라면 보안에 취약한 비밀번호는 사용하면 안 되므로 주의하자.
# [명령 프롬프트]
# (mysite) c:\projects\mysite>python manage.py createsuperuser
# 사용자 이름 (leave blank to use 'pahke'): admin
# 이메일 주소: admin@mysite.com
# Password:
# Password (again):
# 비밀번호가 너무 짧습니다. 최소 8 문자를 포함해야 합니다.
# 비밀번호가 너무 일상적인 단어입니다.
# 비밀번호가 전부 숫자로 되어 있습니다.
# Bypass password validation and create user anyway? [y/N]: y
# Superuser created successfully.
# 여기서는 다음과 같은 정보로 슈퍼 유저를 생성했다.
# 항목	값
# 사용자명	admin
# 이메일 주소	admin@mysite.com
# Password	1111
# [2] 장고 Admin에 접속해 로그인하기
# 1단계를 통해 슈퍼 유저가 생성되었으니 장고 개발 서버를 구동한 후 localhost:8000/admin에 접속해 보자.
# [장고 Admin 로그인 화면]
# 그리고 앞에서 입력한 사용자명과 비밀번호를 입력해 로그인까지 진행하면 다음과 같은 화면이 나타난다.
# [장고 Admin 로그인 후 볼 수 있는 화면]
# 장고 Admin에서는 현재 등록된 그룹 및 사용자에 대한 정보 확인과 수정을 할 수 있다. 물론 그룹은 아직 등록하지 않았으므로 클릭해서 조회해
# 보아도 아무것도 표시되지 않는다. 그러면 본격적으로 장고 Admin의 재미있는 기능을 알아보자.
# [3] 장고 Admin에서 모델 관리하기
# 우리는 Question, Answer 모델을 만들었다. 이 모델들을 장고 Admin에 등록하면 손쉽게 모델을 관리할 수 있다. 쉽게 말해 장고 셸로 수행했던
# 데이터 저장, 수정, 삭제 등의 작업을 장고 Admin에서 할 수 있다. 장고 Admin에서 어떤 마법이 벌어지는지 살펴보자.
# pybo/admin.py 파일을 열고 다음과 같이 코드를 입력하여 Question 모델을 장고 Admin에 등록하자.
# [파일이름: ]
# from django.contrib import admin
# # ---------------------------------- [edit] ---------------------------------- #
# from .models import Question
# admin.site.register(Question)
# # ---------------------------------------------------------------------------- #
# [4] 장고 Admin 새로고침 하기
# 장고 Admin으로 돌아가 새로고침 하면 다음처럼 Question 모델이 추가되어 있다.
# [pybo/admin.py에 모델 등록 후 장고 Admin에서 볼 수 있는 모델]
# 장고 Admin에 Question 모델을 등록했으니 이제 장고 셸이 아닌 장고 Admin 화면에서 Question 모델 데이터를 직관적으로 관리할 수 있다. Question 모델 데이터를 추가하고 수정하고 삭제하는 작업을 좀 더 쉽게 할 수 있게 되었다. 정말 그럴까?
# [5] Question 모델 데이터 추가하기
# 화면에서 Question 모델의 <+ 추가> 버튼을 누르자. 그러면 Question 모델의 데이터 등록 화면이 나타난다. 이어서 Question 모델의 속성에 맞는 값을
# 입력하고 <저장> 버튼을 누르자.
# [모델 데이터 등록 화면]
# 그러면 Question 모델 데이터가 추가된다.
# [모델 데이터 등록 후 볼 수 있는 화면]
# [6] 장고 Admin에 데이터 검색 기능 추가하기
# 장고 Admin에서 제목으로 질문을 검색할 수 있도록 검색 항목을 추가하자. pybo/admin.py 파일에 QuestionAdmin 클래스를 추가하고 search_fields에
# 'subject'를 추가하자.
# [파일이름: C:/projects/mysite/pybo/admin.py]
# from django.contrib import admin
# from .models import Question
# # ---------------------------------- [edit] ---------------------------------- #
# class QuestionAdmin(admin.ModelAdmin):
#     search_fields = ['subject']
# admin.site.register(Question, QuestionAdmin)
# # ---------------------------------------------------------------------------- #
# [7] 장고 Admin에서 데이터 검색해 보기
# 장고 Admin으로 돌아가서 새로고침을 하면 검색 기능이 추가되었음을 알 수 있다. 검색어로 '장고'를 입력하고 <검색>을 눌러보자.
# [장고 검색 시 볼 수 있는 화면]
# 그러면 제목에 '장고'가 포함된 Question 모델 데이터만 조회된다. 장고 Admin에는 이런 마법 같은 기능이 무궁무진하다.
# 장고 Admin의 기능이 궁금하다면 장고 공식 문서를 참고하자.
# 장고 공식 문서 주소(장고 Admin 기능): docs.djangoproject.com/en/3.0/ref/contrib/admin

# [2-02 데이터를 관리하는 모델]
# [완성 소스] : github.com/pahkey/djangobook/tree/2-02
# 장고는 모델로 데이터를 관리한다. 모델로 데이터를 관리한다는 것은 무엇이며 어떤 이점이 있을까? 보통 웹 개발에서는 데이터의 저장 · 조회를 
# 위해 SQL 쿼리문을 이용한다. 이 말은 데이터 저장 · 조회를 위해서는 별도의 SQL 쿼리문을 배워야 한다는 말과 같다. 학습 장벽이 하나 더 생기는 
# 셈이다. 하지만 놀랍게도 모델을 사용하면 SQL 쿼리문을 몰라도 데이터를 저장 · 조회할 수 있다. 모델이 무엇이길래 이렇게 파격적으로 이야기하는지
# 실습을 통해 알아보자.
# migrate와 테이블 알아보기
# [1] 장고 개발 서버 구동 시 나오는 경고 메시지 살펴보기
# [2] config/settings.py 열어 기본으로 설치된 앱 확인하기
# [3] config/settings.py에서 데이터베이스 정보 살펴보기
# [4] migrate 명령으로 앱이 필요로 하는 테이블 생성하기
# [5] DB Browser for SQLite로 테이블 살펴보기
# [6] DB Browser for SQLite 살펴보기
# 모델 만들기
# [1] 모델 속성 구상하기
# [2] pybo/models.py에 질문 모델 작성하기
# [3] pybo/models.py에 답변 모델 작성하기
# [4] config/settings.py를 열어 pybo 앱 등록하기
# [5] pybo/apps.py 열어 살펴보기
# [6] migrate로 테이블 생성하기
# [7] makemigrations로 테이블 작업 파일 생성하기
# [8] makemigrations로 생성된 파일 위치 살펴보기
# [9] makemigrations 한 번 더 실행해 보기
# [10] migrate 실행하기
# [11] DB Browser for SQLite로 생성된 테이블 확인하기
# 데이터 만들고 저장하고 조회하기
# [1] 장고 셸 실행하기
# [2] Question, Answer 모델 임포트하기
# [3] Question 모델로 Question 모델 데이터 만들기
# [4] Question 모델 데이터의 id값 확인하기
# [5] Question 모델로 Question 모델 데이터 1개 더 만들기
# [6] Question 모델 데이터 모두 조회하기
# [7] Question 모델 데이터 조회 결과에 속성값 보여 주기
# [8] Question 모델 데이터 다시 조회해 보기
# [9] 조건으로 Question 모델 데이터 조회하기
# [10] Question 모델 데이터 하나만 조회하기
# [11] get으로 조건에 맞지 않는 데이터 조회하기
# [12] filter로 조건에 맞지 않는 데이터 조회하기
# [13] 제목의 일부를 이용하여 데이터 조회하기
# 데이터 수정하기
# [1] Question 모델 데이터 수정하기
# [2] subject 속성 수정하기
# [3] 수정한 Question 모델 데이터 데이터베이스에 저장하기
# 데이터 삭제하기
# [1] Question 모델 데이터 삭제하기
# [2] 삭제 확인하기
# 연결된 데이터 알아보기
# [1] Answer 모델 데이터 만들기
# [2] id 확인하기
# [3] Answer 모델 데이터 조회하기
# [4] 연결된 데이터로 조회하기: 답변에 있는 질문 조회하기
# [5] 연결된 데이터로 조회하기: 질문을 통해 답변 찾기
# migrate와 테이블 알아보기
# [1] 장고 개발 서버 구동 시 나오는 경고 메시지 살펴보기
# 모델을 알아보기 위해 python manage.py runserver 명령 실행 시 나오는 경고 메시지를 조금 더 자세히 살펴보자. 
# 중간쯤에 있는 경고 메시지를 보면 "아직 적용되지 않은 18개의 migration이 있다"고 한다.
# [명령 프롬프트]
# (mysite) c:\projects\mysite>python manage.py runserver
# Watching for file changes with StatReloader
# Performing system checks...
# System check identified no issues (0 silenced).
# You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s):
# admin, auth, contenttypes, sessions.
# Run 'python manage.py migrate' to apply them.
# May 06, 2020 - 09:49:37
# Django version 3.1.3, using settings 'config.settings'
# Starting development server at http://127.0.0.1:8000/
# Quit the server with CTRL-BREAK.
# migration이 무엇인지 아직은 잘 모를 것이다. 하지만 적어도 이 경고 메시지가 admin, auth, contenttypes, sessions 앱과 관련된 내용이며, 
# 이 오류를 해결하려면 python manage.py migrate를 실행해야 한다는 안내는 확인할 수 있다.
# admin, auth, content types, sessions 앱은 장고 프로젝트를 만들 때 기본으로 생성되어 설치된다
# [2] config/settings.py 열어 기본으로 설치된 앱 확인하기
# 그러면 경고 메시지에 표시된 앱은 어디서 확인할 수 있고, 왜 경고 메시지에 언급되었을까? 그 이유는 config/settings.py 파일을 열어 보면 
# 어느 정도 짐작할 수 있다. 파일을 열어 INSTALLED_APPS 항목을 찾아보자.
# [파일이름: C:/projects/mysite/config/settings.py]
# (... 생략 ...)
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
# ]
# (... 생략 ...)
# INSTALLED_APPS는 현재 장고 프로젝트에 설치된 앱이다. 경고 메시지에 언급되지 않은 messages, staticfiles 앱도 보일 것이다.
# 이 앱들은 데이터베이스와 상관 없으므로 경고 메시지에 언급되지 않은 것이다.
# [3] config/settings.py에서 데이터베이스 정보 살펴보기
# 살펴보는 김에 config/settings.py 파일을 조금 더 살펴보자. config/settings.py 파일에는 설치된 앱뿐만 아니라 사용하는 데이터베이스에
# 대한 정보도 정의되어 있다. DATABASES 설정 중 default의 'ENGINE' 항목을 보면 데이터베이스 엔진이 django.db.backends.sqlite3로 정의되어
# 있음을 알 수 있다. 그리고 'NAME' 항목을 보면 데이터베이스는 BASE_DIR에 있는 db.sqlite3이라는 파일에 저장되는 것도 알 수 있다.
# - BASE_DIR은 프로젝트 디렉터리를 의미하며, 현재 우리의 BASE_DIR은 C:/projects/mysite이다.
# - 데이터베이스를 여러 개 사용할 때 default에 지정한 데이터베이스 외에 추가로 등록해 사용할 수 있다.
# [파일이름: C:/projects/mysite/config/settings.py]
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
# SQLite는 파일 기반의 아주 작은 데이터베이스이다
# SQLite는 주로 소규모 프로젝트에서 사용되는 파일 기반의 가벼운 데이터베이스이다. 보통 초기 개발 단계에서 SQLite를 사용하여 빠르게 개발하고, 
# 서비스로 제공할 때 운영 환경에 어울리는 데이터베이스로 바꾼다.
# [4] migrate 명령으로 앱이 필요로 하는 테이블 생성하기
# migrate 명령을 실행하여 경고 메시지에 있던 앱들이 필요로 하는 테이블들을 생성하자. 명령 프롬프트에서 python manage.py migrate를 입력하면
# 다음과 같은 메시지가 출력된다.
# 테이블은 데이터베이스에서 데이터를 저장하기 위한 데이터 집합의 모음이라고 생각하면 된다.
# [명령 프롬프트]
# (mysite) C:\projects\mysite>python manage.py migrate
# Operations to perform:
#   Apply all migrations: admin, auth, contenttypes, sessions
# Running migrations:
#   Applying contenttypes.0001_initial... OK
#   Applying auth.0001_initial... OK
#   Applying admin.0001_initial... OK
#   Applying admin.0002_logentry_remove_auto_add... OK
#   Applying admin.0003_logentry_add_action_flag_choices... OK
#   Applying contenttypes.0002_remove_content_type_name... OK
#   Applying auth.0002_alter_permission_name_max_length... OK
#   Applying auth.0003_alter_user_email_max_length... OK
#   Applying auth.0004_alter_user_username_opts... OK
#   Applying auth.0005_alter_user_last_login_null... OK
#   Applying auth.0006_require_contenttypes_0002... OK
#   Applying auth.0007_alter_validators_add_error_messages... OK
#   Applying auth.0008_alter_user_username_max_length... OK
#   Applying auth.0009_alter_user_last_name_max_length... OK
#   Applying auth.0010_alter_group_name_max_length... OK
#   Applying auth.0011_update_proxy_permissions... OK
#   Applying sessions.0001_initial... OK
# 메시지는 migrate를 통해 admin, auth, contenttypes, sessions 앱이 사용하는 테이블이 생성되었음을 알려준다. 아직 여러분은 어떤 테이블이 
# 생성되었는지 깊게 알 필요 없다. 왜냐하면 이 앱들을 사용하더라도 직접 테이블을 건드릴 일은 거의 없기 때문이다.
# [5] DB Browser for SQLite로 테이블 살펴보기
# 테이블의 정체가 궁금하다면 migrate 명령을 통해 어떤 테이블이 만들어졌는지 잠깐 확인해 보자. SQLite의 GUI 도구(그래픽 도구)인 
# 'DB Browser for SQLite'를 설치하면 데이터베이스의 테이블을 확인할 수 있다. sqlitebrowser.org/dl에 접속하여 'DB Browser for SQLite'를 내려받자.
# [DB Browser for SQLite 내려받기]
# 여러분의 PC 환경에 맞는 설치 파일을 선택하여 내려받아 설치하자.
# [6] DB Browser for SQLite 살펴보기
# 설치 후 실행하면 다음과 같은 창이 나타난다.
# [DB Browser for SQLite 화면]
# [데이터베이스 열기 → C:/projects/mysite/db.sqlite3 파일 선택]을 수행하면 앞에서 만든 테이블을 눈으로 확인할 수 있다.
# [DB Browser for SQLite에서 mysite/db.sqlite3 파일을 열면 나타나는 화면]
# 화면에 뭔가 많이 나타나서 겁먹었을 수도 있겠지만, 여러분은 테이블의 내용을 자세히 볼 필요가 없다. 왜냐하면 장고는 테이블 작업을 위한
# 쿼리문을 알아서 수행하기 때문이다.
# 장고의 ORM은 쿼리문을 몰라도 데이터 작업을 할 수 있다
# 쿼리문이란 데이터베이스의 테이블을 생성, 수정, 삭제 또는 테이블 데이터의 내용을 생성, 수정, 삭제 시 사용하는 데이터베이스 질의(문법)이다.
# 쉽게 말해 데이터 작업을 위한 문법이다. 데이터를 다루고 싶다면 데이터베이스 종류에 맞는 쿼리문을 공부해야 한다. 하지만 다행스럽게도 여러분은
# 쿼리문을 전혀 몰라도 된다. 왜냐하면 장고에는 ORM(object relational mapping)이라는 기능이 있기 때문이다. ORM은 파이썬으로 데이터 작업을 할 수 
# 있게 해주는 기능이라고 생각하면 된다. 즉, 장고에서는 쿼리문을 몰라도 파이썬을 안다면 데이터를 다룰 수 있다.
# ORM은 데이터베이스 사용 방식의 단점 3가지를 제거한다
# 전통적으로 데이터베이스를 사용하는 프로그램들은 데이터베이스의 데이터를 조회하거나 저장하기 위해 쿼리문을 사용해야 했다. 
# 이 방식은 여전히 많이 사용되고 있는 방식이다. 하지만 이 전통적인 방식에는 몇 가지 단점이 있다. 첫 번째, 쿼리문은 같은 목적으로 작성해도
# 개발자마다 다양한 쿼리문이 만들어지므로 통일성이 깨진다. 두 번째, 개발자가 쿼리문을 잘못 작성하게 되면 시스템의 성능이 저하될 수도 있다. 
# 세 번째, 데이터베이스를 변경하면(MySQL → 오라클) 특정 데이터베이스에 의존하는 쿼리문을 모두 수정해야 하므로 유지 보수의 어려움이 생긴다.
# 하지만 장고의 ORM은 데이터베이스의 테이블을 모델화하여 사용하기 때문에 위에서 열거한 단점이 모두 사라진다.
# ORM이 쿼리문을 자동으로 생성하므로 통일성이 보장된다. 그리고 쿼리문 자체를 잘못 작성할 가능성도 사라진다. 또한 데이터베이스에 맞게 자동으로
# 쿼리문을 생성해 주므로 쿼리문 수정 작업이 사라진다. 바로 이것이 ORM을 사용하는 이유이다.
# 모델 만들기
# 이제 파이보에서 사용할 모델을 만들어 보자. 파이보는 질문 답변 게시판이므로 질문과 답변에 해당하는 모델이 있어야 한다.
# [1] 모델 속성 구상하기
# 질문과 답변 모델에는 어떤 속성이 있어야 할까? 질문 모델에는 다음 속성이 필요하다.
# 속성명	설명
# subject	질문의 제목
# content	질문의 내용
# create_date	질문을 작성한 일시
# 답변 모델은 다음과 같은 속성이 필요하다.
# 속성명	설명
# question	질문(어떤 질문의 답변인지 알아야 하므로 질문 속성이 필요함)
# content	답변의 내용
# create_date	답변을 작성한 일시
# 이와 같이 설계한 모델을 구현해 보자.
# [2] pybo/models.py에 질문 모델 작성하기
# 질문 모델을 pybo/models.py에 작성해 보자. 질문 모델은 Question 클래스로 만든다. 앞으로 대부분의 모델은 클래스로 만들 것이며, 
# 이후 책에서는 클래스명으로 모델을 언급하겠다. 이를테면 질문 모델은 Question 모델이라 하겠다.
# [파일이름: C:/projects/mysite/pybo/models.py]
# from django.db import models
# # ---------------------------------- [edit] ---------------------------------- #
# class Question(models.Model):
#     subject = models.CharField(max_length=200)
#     content = models.TextField()
#     create_date = models.DateTimeField()
# # ---------------------------------------------------------------------------- #
# Question 모델에는 제목(subject), 내용(content), 작성일시(create_date)를 속성으로 추가했다. subject는 최대 200자까지 입력할 수 있도록
# max_length=200을 매개변수로 전달하여 설정했다. 이처럼 글자 수를 제한하고 싶은 데이터는 CharField를 사용해야 한다. content는 글자 수 제한이
# 없는 데이터이다. 글자 수 제한이 없는 데이터는 TextField를 사용한다. create_date 같은 날짜 · 시간 관련 속성은 DateTimeField를 사용한다.
# [3] pybo/models.py에 답변 모델 작성하기
# 이어서 같은 파일에 Answer 모델도 작성하자.
# [파일이름: C:/projects/mysite/pybo/models.py]
# from django.db import models
# class Question(models.Model):
#     subject = models.CharField(max_length=200)
#     content = models.TextField()
#     create_date = models.DateTimeField()
# # ---------------------------------- [edit] ---------------------------------- #
# class Answer(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     content = models.TextField()
#     create_date = models.DateTimeField()
# # ---------------------------------------------------------------------------- #
# Answer 모델은 어떤 질문에 대한 답변이므로 Question 모델을 속성으로 가져야 한다. 이처럼 어떤 모델이 다른 모델을 속성으로 가지면
# ForeignKey를 이용한다. ForeignKey는 쉽게 말해 다른 모델과의 연결을 의미하며, on_delete=models.CASCADE는 답변에 연결된 질문이 삭제되면
# 답변도 함께 삭제하라는 의미이다.
# 장고에서 사용할 수 있는 속성은 아주 많다. 속성이 궁금하다면 장고 공식 문서에 접속하여 어떤 속성이 있는지 읽어 보자.
# 장고 속성 공식 문서 주소: docs.djangoproject.com/en/3.0/ref/models/fields/#field-types
# [4] config/settings.py를 열어 pybo 앱 등록하기
# 위에서 만든 모델을 이용하여 테이블을 생성하자. 테이블 생성을 하려면 config/settings.py 파일에서 INSTALLED_APPS 항목에 pybo 앱을 추가해야 한다.
# [파일이름: C:/projects/mysite/config/settings.py]
# (... 생략 ...)
# INSTALLED_APPS = [
# # ---------------------------------- [edit] ---------------------------------- #
#     'pybo.apps.PyboConfig',
# # ---------------------------------------------------------------------------- #
#     'django.contrib.admin',
#     'django.contrib.auth',
#     (... 생략 ...)
# ]
# (... 생략 ...)
# INSTALLED_APPS에 추가한 pybo.apps.PyboConfig 클래스는 pybo/apps.py 파일에 있는 클래스이다. 잠깐 해당 파일을 열어 확인하고 넘어가자.
# [5] pybo/apps.py 열어 살펴보기
# pybo/apps.py 파일을 열어 보자. 이 파일은 pybo 앱을 만들 때 자동으로 생성된 것이다. 따로 생성할 필요 없다. 그저 눈으로 확인하고 넘어가자.
# [파일이름: C:/projects/mysite/pybo/apps.py]
# from django.apps import AppConfig
# class PyboConfig(AppConfig):
#     name = 'pybo'
# 여기서 꼭 이해하고 넘어가야 할 점은 이 파일에 정의된 PyboConfig 클래스가 config/settings.py 파일의 INSTALLED_APPS 항목에 추가되지 않으면 
# 장고는 pybo 앱을 인식하지 못하고 데이터베이스 관련 작업도 할 수 없다는 사실이다. 좀 더 자세히 설명하자면 장고는 모델을 이용하여 데이터베이스의
# 실체가 될 테이블을 만드는데, 모델은 앱에 종속되어 있으므로 반드시 장고에 앱을 등록해야 테이블 작업을 진행할 수 있다. pybo 앱 등록이 어떤 
# 의미인지 알았으니 이제 모델로 실제 테이블을 만들어 보자.
# [6] migrate로 테이블 생성하기
# 테이블을 생성을 위해 migrate 명령을 실행하자.
# [명령 프롬프트]
# (mysite) C:\projects\mysite>python manage.py migrate
# Operations to perform:
#   Apply all migrations: admin, auth, contenttypes, sessions
# Running migrations:
#   No migrations to apply.
#   Your models have changes that are not yet reflected in a migration, and so won't be applied.
#   Run 'manage.py makemigrations' to make new migrations, and then re-run 'manage.py migrate' to apply them.
# [7] makemigrations로 테이블 작업 파일 생성하기
# 그런데 migrate 명령이 제대로 수행되지 않는다! 왜냐하면 모델이 생성되거나 변경된 경우 migrate 명령을 실행하려면 테이블 작업 파일이 필요하고,
# 테이블 작업 파일을 만들려면 makemigrations 명령을 실행해야 하기 때문이다. makemigrations 명령을 먼저 실행하자.
# [명령 프롬프트]
# (mysite) c:\projects\mysite>python manage.py makemigrations
# Migrations for 'pybo':
#   pybo\migrations\0001_initial.py
#     - Create model Question
#     - Create model Answer
# makemigrations 명령은 장고가 테이블 작업을 수행하기 위한 파일들을 생성한다. 많은 장고 학습자가 makemigrations 명령을 실제 테이블 생성 명령으로
# 오해한다. 하지만 실제 테이블 생성 명령은 migrate이다.
# [8] makemigrations로 생성된 파일 위치 살펴보기
# makemigrations 명령을 수행하면 pybo/migrations/0001_initial.py이라는 파일이 자동으로 생성된다. 파일 위치를 확인해 보자.
# [migrations 폴더에 생성된 파일 확인]
# [9] makemigrations 한 번 더 실행해 보기
# makemigrations 명령을 한 번 더 실행해도 'No changes detected'라는 메시지만 뜬다. 모델의 변경사항이 없다면 '모델 변경 사항 없음'이라고 알려 주는 것이다.
# [명령 프롬프트]
# (mysite) c:\projects\mysite>python manage.py makemigrations
# No changes detected
# [10] migrate 실행하기
# 이제 드디어 migrate 명령을 실행할 때가 되었다. 이 명령을 실행하면 장고는 등록된 앱에 있는 모델을 참조하여 실제 테이블을 생성한다.
# [명령 프롬프트]
# (mysite) C:\projects\mysite>python manage.py migrate
# Operations to perform:
#   Apply all migrations: admin, auth, contenttypes, pybo, sessions
# Running migrations:
#   Applying pybo.0001_initial... OK
# [11] DB Browser for SQLite로 생성된 테이블 확인하기
# migrate 명령은 정말로 실제 테이블을 생성했을까? DB Browser for SQLite를 이용하여 테이블이 잘 생성되었는지 확인해 보자.
# [DB Browser for SQLite에서 확인한 실제 테이블]
# 실제 테이블명을 보면 Question 모델은 pybo_question으로, Answer 모델은 pybo_answer로 테이블 이름이 지어졌음을 확인할 수 있다. 
# 혹시 이 실습 과정 때문에 '실제 테이블명을 알아야 개발을 진행할 수 있나?'라고 오해하는 독자가 없길 바란다. 실제로 장고 개발을 진행할 때는
# 실제 테이블명은 전혀 몰라도 된다. 그저 우리는 Question, Answer 모델을 사용하면 된다.
# sqlmigrate를 실행하면 실제로 어떤 쿼리문이 실행되는지 볼 수 있다
# migrate 명령을 실행할 때 실제로 어떤 쿼리문이 실행될까? 혹시 궁금한 독자가 있다면 sqlmigrate 명령을 실행해 보자. 다음은 
# python manage.py sqlmigrate pybo 0001 명령을 실행한 결과이다.
# [명령 프롬프트]
# (mysite) C:\projects\mysite>python manage.py sqlmigrate pybo 0001
# BEGIN;
# --
# -- Create model Question
# --
# CREATE TABLE "pybo_question" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "subject" varchar(200) NOT NULL, 
# "content" text NOT NULL, "create_date" datetime NOT NULL);
# --
# -- Create model Answer
# --
# CREATE TABLE "pybo_answer" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content" text NOT NULL, 
# "create_date" datetime NOT NULL, "question_id" integer NOT NULL REFERENCES "pybo_question" ("id") DEFERRABLE INITIALLY DEFERRED);
# CREATE INDEX "pybo_answer_question_id_e174c39f" ON "pybo_answer" ("question_id");
# COMMIT;
# 명령어의 의미를 하나씩 설명하자면 'pybo'는 makemigrations 명령을 실행할 때 생성된 pybo/migrations/0001_initial.py의 마이그레이션명
# 'pybo'를 의미하고, '0001'은 생성된 파일의 일련번호를 의미한다. 실행 결과 메시지에는 SQL 문이 있다. 혹시 SQL 문에 익숙한 독자라면 이 
# 메시지로 데이터베이스에서 어떤 일이 벌어졌는지 유추할 수 있을 것이다.
# 데이터 만들고 저장하고 조회하기
# 지금까지 모델을 이용하여 실제 테이블을 만들었다. 그러면 장고에서는 모델을 어떻게 사용할까? 장고 셸을 사용하면 모델 사용법을 쉽게 익힐 수 있다.
# [1] 장고 셸 실행하기
# 다음을 입력하여 장고 셸을 실행하자.
# [명령 프롬프트]
# (mysite) C:\projects\mysite>python manage.py shell
# Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# 장고 셸을 실행해 보면 '파이썬 셸과 비슷한 것 같은데?'라는 생각이 들 수 있다. 하지만 장고 셸은 장고에 필요한 환경들이 자동으로 설정되어 
# 실행되므로 파이썬 셸과는 약간의 차이가 있다.
# [2] Question, Answer 모델 임포트하기
# 장고 셸을 실행했으면 다음 명령으로 Question과 Answer 모델을 장고 셸에 임포트하자.
# [명령 프롬프트]
# >>> from pybo.models import Question, Answer
# [3] Question 모델로 Question 모델 데이터 만들기
# 이어서 Question 모델을 이용하여 Question 모델 데이터를 하나만 만들어 보자. Question 모델의 subject 속성에 제목을, 
# content 속성에 질문 내용을 입력한다. create_date 속성은 DateTimeField이므로 timezone.now()로 현재 일시를 입력한다.
# [명령 프롬프트]
# >>> from django.utils import timezone
# >>> q = Question(subject='pybo가 무엇인가요?', content='pybo에 대해서 알고 싶습니다.', create_date=timezone.now())
# >>> q.save()
# 이 과정을 통해 객체 q가 생성된다. 객체가 생성된 다음 q.save()를 입력하면 Question 모델 데이터 1건이 데이터베이스에 저장된다.
# [4] Question 모델 데이터의 id값 확인하기
# Question 모델 데이터가 잘 생성되었는지 확인해 보자. 장고는 데이터 생성 시 데이터에 id값을 자동으로 넣어준다.
# [명령 프롬프트]
# >>> q.id
# 1
# id는 데이터의 유일한 값이며, 프라이머리 키(PK: primary key)라고 부르기도 한다. id값은 여러분이 데이터를 생성할 때마다 1씩 증가한 값으로
# 자동으로 입력될 것이다.
# [5] Question 모델로 Question 모델 데이터 1개 더 만들기
# 이를 확인하기 위해 두 번째 Question 모델 데이터를 만들어 저장해 보자.
# [명령 프롬프트]
# >>> q = Question(subject='장고 모델 질문입니다.', content='id는 자동으로 생성되나요?', create_date=timezone.now())
# >>> q.save()
# >>> q.id
# 2
# 결과를 보면 두 번째로 생성한 Question 모델 데이터의 id는 예상대로 2이다.
# [6] Question 모델 데이터 모두 조회하기
# 지금까지의 실습 과정은 모두 Question 모델 데이터를 저장하기 위한 것이었다. 이번에는 저장된 데이터를 조회해 보자. 
# 여기서는 특별히 모든 Question 모델 데이터를 조회하기 위해 Question.objects.all()을 입력한다.
# [명령 프롬프트]
# >>> Question.objects.all()
# <QuerySet [<Question: Question object (1)>, <Question: Question object (2)>]>
# 장고에서 저장된 모델 데이터는 Question.objects를 사용하여 조회할 수 있다. 그리고 Question.objects.all()은 
# Question에 저장된 모든 데이터를 조회하는 함수이다. 결과를 보면 QuerySet 객체가 반환됨을 알 수 있다. 그리고 QuerySet에는
# 2개의 Question 객체가 포함되어 있다. 이때 <Question object (1)>, <Question object (2)>의 1, 2가 바로 장고에서 Question 모델 데이터에 
# 자동으로 입력해 준 id이다.
# [7] Question 모델 데이터 조회 결과에 속성값 보여 주기
# 그런데 위의 결과는 데이터 유형을 출력한 것이므로 사람이 보기 불편하다. 이때 Question 모델에 __str__ 메서드를 추가하면 된다.
# [파일이름: C:/projects/mysite/pybo/models.py ]
# (... 생략 ...)
# class Question(models.Model):
#     subject = models.CharField(max_length=200)
#     content = models.TextField()
#     create_date = models.DateTimeField()
# # ---------------------------------- [edit] ---------------------------------- #
#     def __str__(self):
#         return self.subject
# # ---------------------------------------------------------------------------- #
# (... 생략 ...)
# 이렇게 수정하면 데이터 조회 시 id가 아닌 제목을 표시해 준다.
# [8] Question 모델 데이터 다시 조회해 보기
# 모델이 수정되었으므로 장고 셸을 다시 시작하자. 장고 셸에서 quit() 명령을 실행해 종료한 후 다시 장고 셸을 시작한다. 
# 그다음, Question 모델을 다시 임포트한 후 Question 모델 데이터를 조회해 보자.

# [명령 프롬프트]

# (mysite) C:\projects\mysite>python manage.py shell
# Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# >>> from pybo.models import Question, Answer
# >>> Question.objects.all()
# <QuerySet [<Question: pybo가 무엇인가요?>, <Question: 장고 모델 질문입니다.>]>
# 그러면 Question 모델 데이터에 id가 아니라 제목이 표시된다. 여기서 '모델이 수정되었는데 왜 makemigrations, migrate 명령을 실행하지 않지?'라는
# 의문을 가진 독자가 있을 수 있다. 좋은 질문이다. makemigrations, migrate 명령은 모델의 속성이 추가되거나 변경된 경우에 실행해야 하는 명령이다. 
# 지금은 메서드가 추가된 것이므로 이 과정은 하지 않아도 된다.
# [9] 조건으로 Question 모델 데이터 조회하기
# 이전 단계에서는 Question 모델 데이터를 모두 조회했다. 조건을 주어 Question 모델 데이터를 조회하고 싶다면 filter 함수를 사용하면 된다.
# [명령 프롬프트]
# >>> Question.objects.filter(id=1)
# <QuerySet [<Question: pybo가 무엇인가요?>]>
# filter 함수는 조건에 해당하는 데이터를 모두 찾아준다. 지금은 유일한 값인 id를 조건에 사용했으므로 Question 모델 데이터 하나만 나왔다. 
# 하지만 filter 함수는 1개 이상의 데이터를 반환한다. 다만 filter 함수는 반환값이 리스트 형태인 QuerySet이므로 정말로 1개의 데이터만
# 조회하고 싶다면 filter 함수 대신 get 함수를 쓰는 것이 좋다.
# [10] Question 모델 데이터 하나만 조회하기
# get 함수를 사용하면 리스트가 아닌 데이터 하나만 조회할 수 있다.
# [명령 프롬프트]
# >>> Question.objects.get(id=1)
# <Question: pybo가 무엇인가요?>
# 반환값을 보면 QuerySet이 아니라 Question이다. 여기서 filter 함수와 get 함수의 차이점을 알 수 있다. filter 함수는 여러 건의 데이터를
# 반환하지만, get 함수는 단 한 건의 데이터를 반환한다. 두 함수의 차이점을 꼭 알아 두기 바란다.
# [11] get으로 조건에 맞지 않는 데이터 조회하기
# 조건에 맞지 않는 데이터를 get 함수로 조회하면 어떻게 될까? id가 3인 데이터를 조회해 보자.
# [명령 프롬프트]
# >>> Question.objects.get(id=3)
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
#   File "C:\venvs\mysite\lib\site-packages\django\db\models\manager.py", line 82, in manager_method
#     return getattr(self.get_queryset(), name)(*args, **kwargs)
#   File "C:\venvs\mysite\lib\site-packages\django\db\models\query.py", line 415, in get
#     raise self.model.DoesNotExist(
# pybo.models.Question.DoesNotExist: Question matching query does not exist.
# 그러면 이와 같은 오류 메시지를 볼 수 있다. 조건에 맞는 데이터 1개를 반환해야 하는데 조건에 맞는 데이터가 없으니 오류가 발생한 것이다.
# [12] filter로 조건에 맞지 않는 데이터 조회하기
# 그러면 filter 함수는 어떨까? filter 함수로 조건에 맞지 않는 데이터를 조회해 보자.
# [명령 프롬프트]
# >>> Question.objects.filter(id=3)
# <QuerySet []>
# filter 함수는 조건에 맞는 데이터가 없으면 그저 빈 QuerySet을 반환한다. get 함수는 반드시 1건의 데이터를 반환해야 한다는 특징이 있으므로 
# 오류가 발생할 것이다. 이번에는 조금 더 유용한 데이터 조회 방법을 알아보자. 만약 제목에 '장고'라는 글자가 포함된 데이터를 조회하려면
# 어떻게 해야 할까?
# [13] 제목의 일부를 이용하여 데이터 조회하기
# subject에 "장고"라는 문자열이 포함된 데이터를 조회하려면 조건에 subject__contains를 이용하면 된다. 이때 subject와 contains 사이의 
# 언더스코어는 1개가 아니라 2개이다. 장고 셸에서 다음 코드를 입력해 보자.
# [명령 프롬프트]
# >>> Question.objects.filter(subject__contains='장고')
# <QuerySet [<Question: 장고 모델 질문입니다.>]>
# subject__contains='장고'의 의미는 'subject 속성에 '장고'라는 문자열이 포함되어 있는가?'이다. 이 밖에도 filter 함수의 사용 방법은 무궁무진하다. 
# 자세한 filter 함수의 사용 방법은 장고 공식 문서를 참조하자.
# - 장고는 외워서 사용할 수 있는 프레임워크가 아니므로 장고 공식 문서를 자주 참고하는 습관을 들이는 것이 좋다.
# - 장고 공식 문서(데이터 조회 관련): docs.djangoproject.com/en/3.0/topics/db/queries
# 데이터 수정하기
# 이번에는 지금까지 저장했던 Question 모델 데이터를 수정하자.
# [1] Question 모델 데이터 수정하기
# Question 모델 데이터를 수정하려면 우선 수정할 데이터를 조회해야 한다. 다음은 id가 2인 데이터를 조회한 것이다. 이 데이터를 수정할 것이다.
# [명령 프롬프트]
# >>> q = Question.objects.get(id=2)
# >>> q
# <Question: 장고 모델 질문입니다.>
# [2] subject 속성 수정하기
# subject 속성을 수정하자.
# [명령 프롬프트]
# >>> q.subject = 'Django Model Question'
# [3] 수정한 Question 모델 데이터 데이터베이스에 저장하기
# 위의 단계만으로는 변경된 Question 모델 데이터가 데이터베이스에 적용되지 않는다. 반드시 다음처럼 save 함수를 실행해야 변경된 
# Question 모델 데이터가 데이터베이스에 반영된다.
# [명령 프롬프트]
# >>> q.save()
# >>> q
# <Question: Django Model Question>
# 데이터 삭제하기
# 이번에는 Question 모델 데이터를 데이터베이스에서 삭제해 보자.
# [1] Question 모델 데이터 삭제하기
# 데이터 삭제는 데이터 수정과 비슷한 과정으로 진행된다. 여기서는 id가 1인 Question 모델 데이터를 삭제한다.
# [명령 프롬프트]
# >>> q = Question.objects.get(id=1)
# >>> q.delete()
# (1, {'pybo.Question': 1})
# delete 함수를 수행하면 해당 데이터가 데이터베이스에서 즉시 삭제되며, 삭제된 데이터의 추가 정보가 반환된다.
# (1, {'pybo.Question': 1})에서 앞의 1은 삭제된 Question 모델 데이터의 id를 의미하고 {'pybo.Question': 1}은 
# 삭제된 모델 데이터의 개수를 의미한다.
# Answer 모델을 만들 때 ForeignKey로 Question 모델과 연결한 것이 기억나는가? 만약 삭제한 Question 모델 데이터에 2개의 Answer 모델 
# 데이터가 등록된 상태라면 (1, {'pybo.Answer': 2, 'pybo.Question': 1})와 같이 삭제된 답변 개수도 함께 반환될 것이다.
# [2] 삭제 확인하기
# Question 모델 데이터가 정말로 삭제되었는지 확인해 보자.
# [명령 프롬프트]
# >>> Question.objects.all()
# <QuerySet [<Question: Django Model Question>]>
# 결과를 보면 첫 번째 질문은 삭제되고, 두 번째 질문만 남아 있다.
# 연결된 데이터 알아보기
# 앞에서 Answer 모델을 만들 때 ForeignKey로 Question 모델과 연결한 내용이 기억날 것이다. Answer 모델은 Question 모델과 연결되어 있으므로
# 데이터를 만들 때 Question 모델 데이터가 필요하다.
# [1] Answer 모델 데이터 만들기
# id가 2인 Question 모델 데이터를 얻은 다음, 이를 이용하여 Answer 모델 데이터를 만들어 보자.
# [명령 프롬프트]
# >>> q = Question.objects.get(id=2)
# >>> q
# <Question: Django Model Question>
# >>> from django.utils import timezone
# >>> a = Answer(question=q, content='네 자동으로 생성됩니다.', create_date=timezone.now())
# >>> a.save()
# [2] id 확인하기
# Answer 모델 데이터에도 id가 있다.
# [명령 프롬프트]
# >>> a.id
# 1
# [3] Answer 모델 데이터 조회하기
# Answer 모델 데이터를 get 함수로 조회해 보자. 조건은 id를 사용한다.
# [명령 프롬프트]
# >>> a = Answer.objects.get(id=1)
# >>> a
# <Answer: Answer object (1)>
# [4] 연결된 데이터로 조회하기: 답변에 있는 질문 조회하기
# Answer 모델 데이터에는 Question 모델 데이터가 연결되어 있으므로 Answer 모델 데이터에 연결된 Question 모델 데이터를 조회할 수 있다.
# [명령 프롬프트]
# >>> a.question
# <Question: Django Model Question>
# Answer 모델 객체인 a에는 question 속성이 있으므로 a를 통해 질문을 찾는 것은 매우 쉽다. 그렇다면 반대로 질문을 통해 답변을 찾을 수 있을까?
# Question 모델에는 답변 속성이 없어서 불가능할 것 같지만 실제로는 가능하다.
# [5] 연결된 데이터로 조회하기: 질문을 통해 답변 찾기
# 다음처럼 answer_set을 사용하면 된다.
# [명령 프롬프트]
# >>> q.answer_set.all()
# <QuerySet [<Answer: Answer object (1)>]>
# Question 모델과 Answer 모델처럼 서로 연결되어 있으면 연결모델명_set과 같은 방법으로 연결된 데이터를 조회할 수 있다. 
# 그리고 아마 여러분은 연결모델명_set을 써야 하는 경우와 그렇지 않은 경우가 헷갈릴 것이다.
# 이때는 질문과 답변이 달리는 게시판을 상식적으로 생각해 보자. 질문 1개에는 1개 이상의 답변이 달릴 수 있으므로 질문에 달린 답변은
# q.answer_set으로 조회해야 한다(답변 세트를 조회). 답변은 질문 1개에 대한 것이므로 애초에 여러 개의 질문을 조회할 수 없다. 
# 다시 말해 답변 1개 입장에서는 질문 1개만 연결되어 있으므로 a.question만 실행할 수 있다. 1개의 답변으로 여러 개의 질문을 
# a.question_set으로 조회하는 것은 불가능하며, 상식적으로 생각해 보아도 이상하다. 연결모델명_set은 정말 신통방통한 장고의 
# 기능이 아닐 수 없다. 연결모델명_set은 자주 사용할 기능이니 꼭 기억하자.

# [2-01 주소와 화면을 연결하는 URL과 뷰]
# [완성 소스] : github.com/pahkey/djangobook/tree/2-01
# 이제부터 파이보를 만들면서 장고의 기능을 살펴볼 것이다. 가장 먼저 요청 URL을 어떻게 처리하고 또 어떻게 파이썬 프로그램을 호출하는지 알아보자.
# 앱 생성하고 확인하기
# [1] pybo 앱 생성하기
# [2] 생성된 앱 확인하기
# 안녕하세요 파이보?
# [1] 개발 서버 구동하기
# [2] localhost:8000/pybo에 접속하기
# [3] 오류 메시지 확인하기
# [4] config/urls.py 수정하기
# [5] config/urls.py 다시 살펴보기
# [6] 오류 메시지 확인하기
# [7] pybo/views.py 작성하기
# [8] 첫 번째 장고 프로그램 완성!
# 장고 개발 흐름 정리하기
# URL 분리하기
# [1] config/urls.py 다시 살펴보기
# [2] config/urls.py 수정하기
# [3] pybo/urls.py 생성하기
# [4] pybo/urls.py 수정하기
# 앱 생성하고 확인하기
# 1장에서 mysite 프로젝트를 생성했다. 프로젝트에는 장고가 제공하는 기본 앱과 개발자(여러분)가 직접 만든 앱이 포함될 수 있으며,
# 장고에서 말하는 '앱'은 안드로이드 앱과 성격이 다르다고 언급했다. 그러면 장고의 앱이란 정말로 무엇일까? 우리의 파이보 서비스에 필요한
# pybo 앱을 만들어 보며 알아보자.
# [1] pybo 앱 생성하기
# 명령 프롬프트에서 django-admin의 startapp 명령을 이용하여 pybo 앱을 생성하자.
# [명령 프롬프트]
# (mysite) C:\projects\mysite>django-admin startapp pybo
# (mysite) C:\projects\mysite>
# [2] 생성된 앱 확인하기
# 1단계를 진행하면 아무런 메시지가 나타나지 않을 것이다. 하지만 파이참에서 다음의 프로젝트 디렉터리 목록을 살펴보면 pybo라는 이름의 디렉터리가
# 생성되었음을 확인할 수 있다.
# [pybo 디렉터리를 펼친 모습]
# > 모양으로 되어 있는 디렉터리는 디렉터리가 접혀 있는 상태를 의미하며, 디렉터리 이름을 더블클릭하면 디렉터리가 펼쳐진다.
# __init__.py, admin.py, apps.py 같은 파일이 바로 pybo 앱을 위한 것이다. 이 파일들은 실습을 진행하며 작성 또는 수정할 것이다.
# 안녕하세요 파이보?
# 지금부터 실습을 시작해 보자. 실습을 진행하면 파이보 서비스가 조금씩 완성될 것이다. 여기서 필자가 여러분에게 한 가지 부탁하고 싶은 것이 있다.
# 결과를 보기 위해 실습을 무작정 따라 하지 않길 바란다. 결과를 보고 싶은 조급한 마음은 이해하지만, 결과가 나온 이유를 명확하게 이해하면서 따라
# 해야 좋은 개발자가 될 수 있다.
# [1] 개발 서버 구동하기
# 개발 서버를 구동하자.
# [명령 프롬프트]
# (mysite) C:\projects\mysite> python manage.py runserver
# [2] localhost:8000/pybo에 접속하기
# 우리는 아직 아무런 작업도 하지 않았다. 하지만 그냥 웹 브라우저 주소창에 다음을 입력하여 접속해 보자. 앞으로 이 과정을 '페이지를 요청한다' 또는
# localhost:8000을 생략하여 '/pybo/를 요청한다'라고 할 것이다.
# localhost:8000/pybo
# [3] 오류 메시지 확인하기
# 그러면 'Page not found (404)' 오류 페이지가 보인다.
# [웹 브라우저에서 볼 수 있는 Page not found (404) 화면]
# 명령 프롬프트에도 같은 오류가 보인다.
# [명령 프롬프트에서 볼 수 있는 Page not found (404) 화면]
# 404는 HTTP 오류 코드 중 하나로, 사용자가 요청한 페이지를 찾을 수 없는 경우 발생하는 오류이다. 장고는 오류 발생 시 오류 원인을 웹 브라우저
# 또는 명령 프롬프트에 자세히 보여 준다.
# 이 오류는 왜 발생했을까? 장고는 사용자가 웹 브라우저에서 /pybo/라는 페이지를 요청하면 해당 페이지를 가져오는 URL 매핑이 있는지
# config/urls.py 파일을 뒤져 찾아본다. 그런데 아직 /pybo/ 페이지에 해당하는 URL 매핑을 장고에 등록하지 않았다. 그래서 장고는 /pybo/
# 페이지를 찾을 수 없다고 메시지를 보낸 것이다.
# [4] config/urls.py 수정하기
# 그럼 이제 할 일은 정해졌다. 장고가 사용자의 페이지 요청을 이해할 수 있도록 config/urls.py 파일을 수정하자. 앞으로 이를 'URL 매핑을 추가한다'고 
# 말할 것이다. URL 매핑을 추가하기 위해 config/urls.py 파일을 수정하자.
# - config/urls.py 파일은 페이지 요청 시 가장 먼저 호출되며, 요청 URL과 뷰 함수를 1:1로 연결해 준다.
# - 뷰 함수는 아직 살펴보지 않았다. 뷰 함수는 화면을 보여 주기 위한 함수로, views.py에 있는 함수다. 이 함수도 곧 공부할 것이다.
# [파일이름: C:\projects\mysite\config\urls.py]
# from django.contrib import admin
# from django.urls import path
# # ---------------------------------- [edit] ---------------------------------- #
# from pybo import views
# # ---------------------------------------------------------------------------- #
# urlpatterns = [
#     path('admin/', admin.site.urls),
# # ---------------------------------- [edit] ---------------------------------- #    
#     path('pybo/', views.index)''
# # ---------------------------------------------------------------------------- #    
# ]
# 코드의 urlpatterns 변수를 보면 path 함수를 사용하여 pybo/ URL과 views.index를 매핑했다. views.index는 views.py 파일의 index 함수를 의미한다.
# 장고는 이런 식으로 URL과 뷰 함수를 매핑했다.
# [urls.py와 views.py가 매핑되어 연결되는 모습]
# [5] config/urls.py 다시 살펴보기
# 그런데 여러분이 urlpatterns에 입력한 URL은 웹 브라우저에 입력한 localhost:8000/pybo에서 호스트명 localhost와 포트 번호 :8000이 생략된 pybo/이다.
# 호스트명과 포트는 장고가 실행되는 환경에 따라 변하는 값이며 장고가 이미 알고 있는 값이다. 그러므로 urlpatterns에는 호스트명과 포트를 입력하지
# 않는다.
# [urls.py 파일의 urlpatterns]
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('pybo/', views.index)''
# ]
# 그리고 pybo에 슬래시 /를 붙여 입력한 점에도 주목하자! 슬래시를 붙이면 사용자가 슬래시 없이 주소를 입력해도 장고가 자동으로 슬래시를 붙여 준다.
# 이는 URL을 정규화하는 장고의 기능 덕분이다. 아무튼! 특별한 경우가 아니라면 URL 매핑에는 호스트명과 포트를 생략하고 끝에는 슬래시를 붙이자.
# 웹 브라우저 주소창에 localhost:8000/pybo라고 입력하면 장고가 자동으로 localhost:8000/pybo/와 같이 슬래시를 붙여 준다.
# 프로젝트 디렉터리는 BASE_DIR 변수에 저장되어 있다
# 여러분의 파이보 프로젝트 디렉터리는 C:/projects/mysite일 것이다. 장고는 이 경로를 settings.py 파일의 BASE_DIR 변수에 저장한다.
# 이 책에서는 파일 경로를 언급할 때 BASE_DIR을 생략한다. 예를 들어 config/urls.py라 언급하면 BASE_DIR의 값인 C:/projects/mysite가 생략된
# 것이므로 실제 언급하는 파일 위치는 C:/projects/mysite/config/urls.py이다.
# [6] 오류 메시지 확인하기
# 다시 localhost:8000/pybo/ 에 접속해 보자. 그러면 웹 브라우저에 '사이트에 연결할 수 없음' 오류가 표시되고, 개발 서버에는 다음과 같은 오류가
# 표시된다.
# [명령 프롬프트]
# (... 생략 ...)
#   File "c:\projects\mysite\config\urls.py", line 23, in <module>
#     path('pybo/', views.index),
# AttributeError: module 'pybo.views' has no attribute 'index'
# config/urls.py 파일을 수정했음에도 이런 오류가 발생한 이유는 URL 매핑에 추가한 뷰 함수인 views.index가 없기 때문이다.
# [7] pybo/views.py 작성하기
# pybo/views.py 파일에 index 함수를 추가하자.
# [파일이름: c:\projects\mysite\pybo\views.py]
# # ---------------------------------- [edit] ---------------------------------- #
# from django.http import HttpResponse
# def index(request):
#     return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")
# # ---------------------------------------------------------------------------- #
# - index 함수의 매개변수 request는 장고에 의해 자동으로 전달되는 HTTP 요청 객체이다.
# - request는 사용자가 전달한 데이터를 확인할 때 사용된다.
# return 문에 사용된 HttpResponse는 페이지 요청에 대한 응답을 할 때 사용하는 장고 클래스이다. 여기서는 HttpResponse에
# "안녕하세요 pybo에 오신것을 환영합니다."라는 문자열을 전달하여 이 문자열이 웹 브라우저에 그대로 출력되도록 만들었다.
# [8] 첫 번째 장고 프로그램 완성!
# 이제 /pybo/ 페이지에 접속하면 웹 브라우저에 "안녕하세요 pybo에 오신것을 환영합니다."라는 문자열이 출력된다.
# [/pybo/에서 볼 수 있는 첫 번째 화면]
# 축하한다. 여러분의 첫 번째 장고 프로그램이 완성되었다!
# 장고 개발 흐름 정리하기
# 지금까지 여러분이 경험한 개발 과정은 모든 실습 과정에서 여러 번 반복될 것이다. 그만큼 이 과정은 중요하다! 다음 그림으로 개발 과정을 정리해 보자.
# 1)웹 브라우저 주소창에 localhost:8000/pybo 입력(장고 개발 서버에 /pybo 페이지 요청).
# 2)config/urls.py 파일에서 URL을 해석해 pybo/views.py 파일의 index 함수 호출.
# 3)pybo/views.py 파일의 index 함수를 실행하고 그 결과를 웹 브라우저에 전달.
# 4)사용자가 /pybo 페이지를 요청하면 장고 개발 서버가 URL을 분석해, URL에 매핑된 함수를 호출하고, 함수 실행 결과를 웹 브라우저 화면에 전달한다.
#   이 과정을 기억하며 실습을 진행하자.
# URL 분리하기
# [1] config/urls.py 다시 살펴보기
# config/urls.py 파일을 다시 한번 살펴보자. 아까 얘기했듯이 pybo 앱 관련 파일은 대부분 pybo 디렉터리에 있다. 하지만 매핑을 위한 urls.py 
# 파일은 pybo 디렉터리에 없다. 그러므로 pybo 앱에 URL 매핑을 추가하려면 pybo 디렉터리가 아닌 config 디렉터리에 있는 urls.py 파일을 수정해야 한다.
# [파일이름: C:/projects/mysite/config/urls.py]
# from django.contrib import admin
# from django.urls import path
# from pybo import views
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('pybo/', views.index),
# ]
# 이 방식은 프로젝트의 짜임새를 전혀 고려하지 않은 것이다. pybo 앱 관련 urls.py 파일을 따로 구성할 방법은 없을까? 물론 있다.
# [2] config/urls.py 수정하기
# include 함수를 임포트해 pybo/의 URL 매핑을 path('pybo/', views.index)에서 path('pybo/', include('pybo.urls'))로 수정하자.
# [파일이름: c:\projects\mysite\config\urls.py]
# from django.contrib import admin
# # ---------------------------------- [edit] ---------------------------------- #
# from django.urls import path, include
# # ---------------------------------------------------------------------------- #
# urlpatterns = [
#     path('admin/', admin.site.urls),
# # ---------------------------------- [edit] ---------------------------------- #
#     path('pybo/', include('pybo.urls')),
# # ---------------------------------------------------------------------------- #    
# ]
# path('pybo/', include('pybo.urls'))는 pybo/로 시작되는 페이지 요청은 모두 pybo/urls.py 파일에 있는 URL 매핑을 참고하여 처리하라는 의미이다. 
# 다시 말해 pybo 앱과 관련된 URL 요청은 앞으로 pybo/urls.py 파일에서 관리하라는 뜻이다. 다음 예와 같이 pybo/로 시작하는 요청은 
# config/urls.py 파일이 아닌 pybo/urls.py 파일을 통해 처리하게 된다.
# URL 요청	요청 처리 파일
# pybo/question/create/	pybo/urls.py
# pybo/answer/create/	pybo/urls.py
# 그외	config/urls.py
# [3] pybo/urls.py 생성하기
# pybo 앱 디렉터리에 urls.py 파일을 생성하자. [pybo → 마우스 오른쪽 클릭 → New → File]을 한 다음 파일명으로 urls.py를 입력하자. 
# 이때 파일명에는 반드시 확장자 .py가 포함되어야 한다.
# [pybo/에 새 파일 만들기]
# [반드시 확장자명 포함하여 새 파일 만들기]
# [4] pybo/urls.py 수정하기
# pybo/urls.py 파일을 다음과 같이 수정하자.
# [파일이름: C:\projects\mysite\pybo\urls.py]
# # ---------------------------------- [edit] ---------------------------------- #
# from django.urls import path
# from . import views
# urlpatterns = [
#     path('', views.index),
# ]
# # ---------------------------------------------------------------------------- #
# 코드 내용은 기존 config/urls.py 파일과 다르지 않다. 다만 path('', views.index) 입력 부분만 다르다. config/urls.py 파일에서
# pybo/에 대한 처리를 한 상태에서 pybo/urls.py 파일이 실행되므로 첫 번째 매개변수에 pybo/가 아닌 빈 문자열('')을 인자로 넘겨준 것이다.
# config/urls.py		pybo/urls.py		최종 URL
# 'pybo/'	+	''	=	'pybo/'
# 다시 /pybo/에 접속해 보자. 다음 화면이 나오면 잘 접속된 것이다.
# [/pybo/ 접속 시 볼 수 있는 화면]
# 다음 그림은 장고가 config/urls.py, pybo/urls.py 파일 순서로 살펴보며 URL 매핑을 찾는 과정을 보여준다.
# 이 과정을 이해하는 것은 무척 중요하므로 다른 예로도 설명해 보겠다. 만약 pybo/urls.py 파일에 path('question/create/', ...)가 추가 된다면
# config/urls.py 파일과 pybo/urls.py 파일에 의해 최종 매핑되는 URL은 pybo/question/create/가 될 것이다.



# [1장 장고 개발 준비!]
# ‘시작이 반이다.’ 여러분은 이미 장고를 향해 첫걸음을 내디뎠으니 성공을 절반 이룬 셈이다. 축하한다. 이 책은 처음부터 끝까지
# 모든 내용이 이어진다. 따라서 이 책은 흐름이 중요하며 그중에서도 시작이 가장 중요하다. 이 장에서는 장고를 본격적으로 개발
# 하기 전에 준비해야 할 것을 알아보자. 장고 개발을 시작하기 전에는 무엇을 설치해야 할까? 여기서는 파이썬과 장고, 파이참 
# 에디터를 설치한다. 파이참 에디터는 장고 개발을 한결 편리하게 만들어 주는 도구이다. 모든 준비를 마치면 새로운 장고 프로젝트도
# 생성해 보자. 참고로 실습 코드가 너무 길어지면 절약과 가독성을 위해 코드 전체를 표시하지 않고 실습에 필요한 부분만
# 표시했다. 더불어 전체 코드를 참고하며 공부할 독자를 위해 각 장 도입부에 소스 보기 링크를 안내했다.
# 이 장의 목표
# - 파이썬과 장고를 설치하고 개발 환경을 준비한다.
# - 장고 프로젝트를 만들어 첫 번째 프로그램을 만든다.
# - 장고 서버를 실행하고 실행 결과를 확인한다.

# [1-05 파이참 설치하고 장고 개발 서버 실행하기]
# [완성 소스] : github.com/pahkey/djangobook/tree/1-05
# 보통 파이썬과 장고 개발에 많이 사용되는 에디터는 비주얼 스튜디오 코드와 파이참이다. 이 책에서는 파이참으로 장고 개발을
# 진행한다.
# 파이참 설치하기
# [1] 파이참 설치 파일 내려받기
# [2] 파이참 실행하기
# 파이참 인터프리터 설정하고 개발 서버 한글로 실행하기
# [1] 현재 파이썬 인터프리터 위치 확인하기
# [2] 파이썬 인터프리터 위치를 가상 환경 위치로 수정하기
# [3] 파이참에서 settings.py 파일 수정하기
# [4] 개발 서버 다시 구동하기
# 파이참 설치하기
# [1] 파이참 설치 파일 내려받기
# 파이참은 다음 주소에 접속하면 내려받을 수 있다.
# 윈도우용 파이참 설치 파일 주소: www.jetbrains.com/ko-kr/pycharm/download/#section=windows
# <Professional>과 <Community> 중 무료 버전인 <Community>를 선택하자. 파이참 설치 파일을 내려받은 후 설치를 진행하자. 
# 설치할 때 특별히 주의할 점은 없으므로 끝까지 <Next>를 선택하여 설치하면 된다.
# [2] 파이참 실행하기
# [윈도우 키]를 누르고 프로그램 목록에서 [JetBrains → PyCharm Community Edition]을 선택하면 파이참이 실행된다. 파이참을
# 처음 실행하는 독자라면 다음과 같은 설정 창이 나타날 것이다. 테마, 플러그인 등의 옵션은 기본값으로 선택하고 넘어가자. 
# 필자는 책에 담을 화면을 갈무리하고자 다음과 같이 바탕이 흰색인 Light 테마를 설정했다.
# 이어서 다음과 같은 창이 나오면 두 번째 메뉴인 <Open>을 선택하여 앞에서 우리가 생성한 장고 프로젝트인 C:/projects/mysite를
# 선택하자.
# 여기까지 문제없이 진행했다면 다음과 같이 파이참이 정상으로 실행된다.
# 처음 프로젝트를 만들면 mysite 디렉터리 안에 main.py 파일이 자동으로 생성될 수 있다. 파일이 있다면 삭제 후 실습을 진행하자.
# 파이참 인터프리터 설정하고 개발 서버 한글로 실행하기
# 파이참으로 장고 프로젝트를 불러온 후 가장 먼저 해야 할 일은 장고 프로젝트가 바라봐야 할 파이썬 인터프리터 위치를 설정하는
# 것이다.
# [1] 현재 파이썬 인터프리터 위치 확인하기
# 파이참 메뉴에서 [File → Settings]를 눌러 설정 창을 열고 [Project: mysite → Project Interpreter]를 순서대로 눌러 파이썬 
# 인터프리터 위치를 설정할 수 있는 창을 열자. 그런 다음 오른쪽 위에 보이는 Python Interpreter를 보자. 아마도 파이썬을 
# 설치한 디렉터리로 설정되어 있을 것이다.
# [2] 파이썬 인터프리터 위치를 가상 환경 위치로 수정하기
# 하지만 지금은 가상 환경을 사용하므로 파이썬 인터프리터 위치를 가상 환경 위치로 수정해 야 한다. 다음처럼
# Python Interpreter 오른쪽에 보이는 톱니바퀴 모양 아이콘을 누른 다음 <Add>를 누르자.
# 톱니바퀴 모양 아이콘이 가려져 있으므로 그림 참고 시 주의!
# 다음처럼 파이썬 인터프리터 위치를 설정할 수 있는 'Add Python Interpreter' 창이 나타난다. 여기서
# <Existing environment>를 누른 다음 Interpreter 오른쪽에 보이는 <...>을 누르자.
# 그리고 다음처럼 C:/venvs/mysite/Scripts/python.exe를 선택한 후 <OK>를 누른다.
# 나머지 창도 를 눌러 설정을 마치면 파이참이 mysite 가상 환경에 있는 파이썬 인터프리터를 인식하기 시작한다.
# [3] 파이참에서 settings.py 파일 수정하기
# 이제 파이참으로 장고를 개발할 준비가 완료되었다. 장고 개발을 맛보는 차원에서 장고의 설정값이 들어 있는 settings.py 
# 파일을 수정해 보자. 파이참에서 settings.py 파일을 열어 LANGUAGE_CODE와 TIME_ZONE 설정값을 수정하자. LANGUAGE_CODE를 
# en-us에서 ko-kr로 수정하고 TIME_ZONE을 UTC에서 Asia/Seoul로 수정했다. 언어와 시간을 한국 값으로 바꾼 것이다.
# [파일이름: C:/projects/mysite/config/settings.py]
# (... 생략 ...)
# # ---------------------------------- [edit] ---------------------------------- #
# LANGUAGE_CODE = 'ko-kr'
# TIME_ZONE = 'Asia/Seoul'
# # ---------------------------------------------------------------------------- #
# (... 생략 ...)
# [중요] 파일명과 소스코드
# 앞으로 소스코드는 항상 다음과 같은 규칙으로 표시된다. 먼저 파일이름의 전체경로를 표시하고 그 바로 아래에 소스의 내용을
# 표시한다.
# [파일이름: C:/projects/mysite/config/settings.py]
# (... 생략 ...)
# # ---------------------------------- [edit] ---------------------------------- #
# LANGUAGE_CODE = 'ko-kr'
# TIME_ZONE = 'Asia/Seoul'
# # ---------------------------------------------------------------------------- #
# (... 생략 ...)
# 소스코드에서 생략된 부분은 위와 같이 (... 생략 ...) 으로 표시한다.
# 그리고 소스코드에서 신규로 추가되거나 변경된 부분은 다음처럼 [edit] 문단으로 표시한다.
# # --------------------------------- [edit] ---------------------------------- #
# 변경되거나 추가된 부분은 여기에
# # --------------------------------------------------------------------------- #
# ※ 만약 신규로 추가된 파일인 경우는 파일의 처음과 끝이 [edit] 문단으로 감싸여 진다.
# [4] 개발 서버 다시 구동하기
# 앞의 실습을 잘 진행했다면 개발 서버가 종료된 상태일 것이다. 개발 서버를 다시 구동하자. localhost:8000으로 접속하면
# 초기 화면이 영어에서 한글로 바뀌어 있다.
# python manage.py runserver로 서버 구동!

# [1-04 장고 프로젝트 생성하기]
# 장고에는 프로젝트라는 개념이 있는데, 장고의 프로젝트는 하나의 웹 사이트라고 생각하면 된다. 즉, 장고 프로젝트를 생성하면
# 한 개의 웹 사이트를 생성하는 것과 같다. 프로젝트 안에는 여러 개의 앱이 존재한다. 이 앱들이 모여 웹 사이트를 구성한다.
# 여기서 앱이란 관리자 앱, 인증 앱 등과 같이 장고가 기본으로 제공하는 앱과 개발자가 직접 만든 앱을 칭한다.
# 장고에서 말하는 앱은 일반적으로 여러분이 알고 있는 안드로이드 앱, iOS 앱과는 성격이 다르다. 안드로이드 앱이 하나의
# 프로그램이라면, 장고의 앱은 프로젝트를 구성하는 작은 단위의 기능이다.
# 프로젝트 디렉터리 생성하기
# [1] 프로젝트 루트 디렉터리 생성하기
# [2] 프로젝트 루트 디렉터리 안에서 가상 환경에 진입하기
# [3] 장고 프로젝트를 담을 디렉터리 생성하고 이동하기
# [4] 장고 프로젝트 생성하기
# [5] 장고 프로젝트 내용물 확인하기
# 개발 서버 구동하고 웹 사이트에 접속해 보기
# [1] 개발 서버 구동하기
# [2] 개발 서버 종료하기
# mysite 가상 환경에 간단히 진입하기
# [1] mysite.cmd 배치 파일 생성하기
# [2] 배치 파일 위치를 PATH 환경 변수에 추가하기
# [3] PATH 환경 변수 확인하기
# [4] 배치 파일 실행하여 가상 환경에 진입하기
# 프로젝트 디렉터리 생성하기
# [1] 프로젝트 루트 디렉터리 생성하기
# 장고 프로젝트는 여러 개가 될 수 있으므로 프로젝트를 모아 둘 프로젝트 루트 디렉터리 생성은 필수다. 여기서는 프로젝트
# 루트 디렉터리 이름을 projects로 지었다.
# 여기서는 C 드라이브에 프로젝트를 담을 루트 디렉터리를 생성했다.
# [명령 프롬프트]
# C:\Users\pahke>cd \
# C:\>mkdir projects
# C:\>cd projects
# C:\projects>
# [2] 프로젝트 루트 디렉터리 안에서 가상 환경에 진입하기
# 프로젝트 루트 디렉터리 안에서 다음 명령어를 입력해 앞에서 만든 mysite 가상 환경에 진입한다. 가상 환경 진입 명령어가 
# 길어서 좀 불편하겠지만, 지금은 이 방법으로 가상 환경에 진입하겠다.
# 가상 환경 진입 명령어를 간단하게 만드는 팁은 이 절의 마지막에서 설명한다.
# [명령 프롬프트]
# C:\projects>C:\venvs\mysite\Scripts\activate
# (mysite) C:\projects>
# [3] 장고 프로젝트를 담을 디렉터리 생성하고 이동하기
# 장고 프로젝트를 담을 mysite 디렉터리를 생성하고 이동하자.
# [명령 프롬프트]
# (mysite) C:\projects>mkdir mysite
# (mysite) C:\projects>cd mysite
# (mysite) C:\projects\mysite>
# [4] 장고 프로젝트 생성하기
# mysite 디렉터리에서 django-admin이라는 도구로 장고 프로젝트를 생성하자. 이때 config 다음에 점 기호(.)가 있음에 주의하자.
# 점 기호는 '현재 디렉터리를 프로젝트 디렉터리로 만들라'는 의미이다.
# [명령 프롬프트]
# (mysite) C:\projects\mysite>django-admin startproject config .
# [5] 장고 프로젝트 내용물 확인하기
# 위 단계들이 완료되면 다음과 같은 구조로 디렉터리가 구성되어 있는지, 파일이 잘 생성되어 있는지 확인해 보자.
# [디렉터리 구조와 파일]
# C:\projects\mysite
# ├── config/
# │      ├─ asgi.py
# │      ├─ settings.py
# │      ├─ urls.py
# │      ├─ wsgi.py
# │      └─ __init__.py
# └── manage.py
# 개발 서버 구동하고 웹 사이트에 접속해 보기
# 이제 웹 사이트를 생성한 것과 다름없다. 개발 서버를 구동하고 웹 사이트에 접속해 보자.
# [1] 개발 서버 구동하기
# python manage.py runserver 명령을 실행하면 개발 서버가 구동된다. 맨 아랫줄에는 'Quit the server with CTRL-BREAK'이라는
# 개발 서버 종료 방법도 안내되어 있다. 개발 서버를 종료하려면 <Ctrl+C>를 누르란 뜻이다.
# [명령 프롬프트]
# (mysite) C:\projects\mysite>python manage.py runserver
# Watching for file changes with StatReloader
# Performing system checks...
# System check identified no issues (0 silenced).
# You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): 
# admin, auth, contenttypes, sessions.
# Run 'python manage.py migrate' to apply them.
# April 21, 2020 - 21:51:03
# Django version 3.1.3, using settings 'config.settings'
# Starting development server at http://127.0.0.1:8000/
# Quit the server with CTRL-BREAK.
# 개발 서버가 구동된 상태를 유지하고 웹 브라우저를 이용하여 127.0.0.1:8000에 접속해 보자. 그러면 장고가 기본으로 만든
# 웹 사이트 화면을 볼 수 있다.
# - 개발 서버는 127.0.0.1, 즉 로컬호스트localhost로 실행되므로 로컬 서버라 부르기도 한다. 필자는 개발을 위해 실행된 개발
#   서버를 '개발 서버'라 부르겠다.
# - 127.0.0.1:8000 대신 localhost:8000이라고 입력해도 같은 화면을 볼 수 있다. 127.0.0.1과 localhost는 현재 컴퓨터를 
#   가리키는 아이피 주소다.
# 아쉽게도 아직은 개발 서버 환경에서 사이트가 실행되고 있으므로 개발 서버 환경을 실행한 컴퓨터(여러분의 컴퓨터)에서만 
# 사이트에 접속할 수 있다. 즉, 아직은 다른 사람이 접속할 수 있는 상태가 아니다. 다른 사람이 접속할 수 있는 기능은 파이보를
# 멋지게 만든 후에 추가할 것이다.
# [2] 개발 서버 종료하기
# <Ctrl+C> 를 눌러 개발 서버를 종료해 보자. 개발 서버가 종료되면 localhost:8000으로 mysite에 접속할 수 없다.
# 웹 브라우저에서 새로고침을 눌러 정말 그런지 확인해 보자.
# 로컬 아이피 주소로 다른 사람이 접속할 수 없는 이유
# 앞에서 '아직은 여러분이 만든 사이트에 다른 사람이 접속할 수 없다'고 이야기했다. 왜 그럴까? 다른 사람이 여러분이 만든
# 사이트에 접속하려면 localhost나 127.0.0.1이라는 로컬 아이피 주소가 아닌 15.165.210.240과 같은 인터넷 세상 속의 아이피
# 주소 또는 pybo.kr과 같은 도메인이 필요하기 때문이다. 로컬 아이피 주소의 '로컬'은 지역이라는 뜻이며, 이는 곧 '내 PC'를
# 의미한다. 내 PC의 아이피 주소이므로 친구가 접속할 수 없다. 4장에서 인터넷 세상 속의 아이피 주소로 여러분이 만든 사이트에
# 접속하는 방법을 소개하므로 우선은 파이보 기능을 완성하는 데 집중하자.
# mysite 가상 환경에 간단히 진입하기
# mysite 가상 환경에 진입하려면 매번 명령 프롬프트를 실행하고 C:/venvs/mysite/Scripts 디렉터리로 이동하여 activate 명령을
# 수행해야 한다. 이런 일련의 과정을 한 번에 수행할 수 있는 배치 프로그램을 만들어 귀찮음을 덜어 보자.
# [1] mysite.cmd 배치 파일 생성하기
# mysite.cmd 파일을 venvs 디렉터리에 만들고 다음과 같이 작성하여 저장하자. 확장자 .cmd가 붙은 파일은 배치(batch) 파일이라
# 부르며, 명령어 입력과 실행을 한 번에 해주는 파일이라 생각하면 된다.
# [파일 이름: C:/venvs/mysite.cmd]
# @echo off
# cd c:/projects/mysite
# c:/venvs/mysite/scripts/activate
# 배치 파일의 내용은 C:/projects/mysite 디렉터리로 이동한 다음, C:/venvs/mysite/scripts/activate 명령을 수행하라는 뜻이다.
# [2] 배치 파일 위치를 PATH 환경 변수에 추가하기
# 이 배치 파일이 명령 프롬프트 어느 곳에서나 수행될 수 있도록 C:/venvs 디렉터리를 시스템의 환경 변수 PATH에 추가해야 한다. 
# 먼저 <윈도우키+R> 키를 입력하여 다음처럼 sysdm.cpl 명령을 입력한 다음 <확인>을 누르자.
# 그러면 다음과 같은 '시스템 속성' 창이 나타난다. 여기서 <고급> 탭을 선택하고 <환경 변수> 버튼을 누르자.
# 그러면 다음과 같은 '환경 변수' 창이 나타난다. 여기서 사용자 변수 중 <Path>를 선택하고 <편집> 버튼을 누르자.
# 그러면 다음과 같은 '환경 변수 편집' 창이 나타난다. 여기서 <새로 만들기> 버튼을 누르자.
# 그리고 다음 그림처럼 C:/venvs라는 디렉터리를 추가하고 <확인> 버튼을 누르자.
# 마지막으로 다음 '환경 변수' 창에서 <확인> 버튼을 누르자.
# [3] PATH 환경 변수 확인하기
# 이렇게 하면 환경 변수 PATH에 C:/venvs 디렉터리가 추가되어 mysite.cmd 명령을 어디서든 실행할 수 있다. 
# 명령 프롬프트를 다시 시작하자(그래야 변경된 환경 변수 PATH가 제대로 반영된다). 그리고 set path 명령을 실행하여 
# 변경된 환경 변수 PATH의 내용을 확인해 보자. C:/venvs라는 디렉터리가 환경 변수 PATH에 포함되어 있으면 된다.
# [명령 프롬프트]
# C:\Users\pahkey>set path
# Path=C:\Windows\system32; (... 생략 ...) ;C:\venvs
# PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC
# [4] 배치 파일 실행하여 가상 환경에 진입하기
# 이제 지금까지 만든 mysite 명령(배치 파일 이름)을 실행하여 가상 환경에 잘 진입하는지 확인해 보자. 
# 참고로 윈도우에서 확장자가 .cmd인 파일은 확장자를 빼고 입력해도 된다.
# [명령 프롬프트]
# C:\Users\pahkey> mysite
# (mysite) C:\projects\mysite>
# 맥 OS에서 가상 환경 진입하기
# 맥을 사용할 경우 mysite.cmd 대신 다음처럼 mysite.sh을 작성한다.
# [파일 이름: /Users/pahkey/venvs/mysite.sh]
# #!/bin/bash
# cd /Users/pahkey/projects/mysite
# source /Users/pahkey/venvs/mysite/bin/activate
# 그리고 맥 터미널에서 mysite.sh을 다음과 같이 수행하자.
# $ /Users/pahkey/venvs/mysite.sh

# [1-03 장고 개발 환경 준비하기]
# 이제 본격적으로 장고 개발 환경을 준비해 보자. 그전에 여러분이 알아야 할 중요한 개념이 하나 있다. 
# 바로 파이썬 가상 환경이다. 우리는 장고를 파이썬 가상 환경에 설치할 것이다.
# 파이썬 가상 환경 알아보기
# 파이썬 가상 환경 사용해 보기
# [1] 가상 환경 디렉터리 생성하기
# [2] 가상 환경 만들기
# [3] 가상 환경에 진입하기
# [4] 가상 환경에서 벗어나기
# 장고 설치하기
# [1] 가상 환경인지 확인하기
# [2] 가상 환경에서 장고 설치하기
# [3] pip 최신 버전으로 설치하기
# 파이썬 가상 환경 알아보기
# 파이썬 가상 환경은 파이썬 프로젝트를 진행할 때 독립된 환경을 만들어 주는 고마운 도구다. 예를 들어 파이썬 개발자 A가
# 2개의 파이썬 프로젝트를 개발하고 관리한다고 가정하자. 파이썬 프로젝트를 각각 P-1, P-2라고 부르겠다. 이때 P-1, P-2에
# 필요한 파이썬 또는 파이썬 라이브러리의 버전이 다를 수 있다. 이를테면 P-1에는 파이썬 2.7 버전이, P-2에는 파이썬 3.8
# 버전이 필요할 수 있다. 이때 하나의 데스크톱에 서로 다른 버전의 파이썬을 설치해야 하는 문제가 생긴다.
# 이러한 개발 환경은 구축하기도 어렵고 사용하기도 힘들다. 가상 환경이 없던 예전에는 그런 고생을 감수할 수밖에 없었다.
# 하지만 파이썬 가상 환경을 이용하면 하나의 데스크톱 안에 독립된 가상 환경을 여러 개 만들 수 있다. 즉, 프로젝트 P-1을 
# 위해 가상 환경 V-1을 만들어 파이썬 2.7 버전을 설치하고, 프로젝트 P-2를 위해 가상 환경 V-2를 만들어 파이썬 3.8 버전을
# 설치해서 사용할 수 있다.
# 이처럼 가상 환경을 이용하면 하나의 데스크톱에 서로 다른 버전의 파이썬과 라이브러리를 쉽게 설치해 사용할 수 있다. 
# 물론 이 책에서는 '파이보'라는 하나의 프로젝트만 진행할 것이므로 가상 환경이 필수는 아니다. 하지만 앞으로 웹 프로그래밍을
# 계속하고 싶다면 가상 환경의 개념을 익히고 실제로 사용해 보는 것이 좋다.
# 파이썬 가상 환경 사용해 보기
# [1] 가상 환경 디렉터리 생성하기
# 윈도우에서 명령 프롬프트를 실행하고 다음 명령어를 입력해 C:/venvs라는 디렉터리를 만들자.
# 루트 디렉터리를 반드시 C:/venvs로 해야 하는 것은 아니지만 실습 편의를 위해 이대로 지정하자.
# [명령 프롬프트]
# C:\Users\pahkey> cd \
# C:\> mkdir venvs
# C:\> cd venvs
# [2] 가상 환경 만들기
# 파이썬 가상 환경을 만드는 다음 명령어를 입력해 실행하자.
# [명령 프롬프트]
# C:\venvs> python -m venv mysite
# 명령에서 python -m venv는 파이썬 모듈 중 venv라는 모듈을 사용한다는 의미다. 그 뒤의 mysite는 여러분이 생성할 가상 환경의
# 이름이다. 가상 환경의 이름을 반드시 mysite로 지을 필요는 없다. 만약 가상 환경의 이름을 awesomesite와 같이 지정했다면
# 책에 등장하는 mysite라는 가상 환경 이름을 awesomesite로 대체하여 읽으면 된다.
# 하지만 실습 진행의 편의를 위해 가상 환경 이름을 동일하게 하기를 권장한다.
# 명령을 잘 수행했다면 C:/venvs 디렉터리 아래에 mysite라는 디렉터리가 생성되었을 것이다. 이 디렉터리를 가상 환경이라 
# 생각하면 된다. 그런데 가상 환경을 만들었다 해서 바로 가상 환경을 사용할 수는 없다. 가상 환경을 사용하려면 가상 환경에
# 진입해야 한다.
# [3] 가상 환경에 진입하기
# 가상 환경에 진입하려면 우리가 생성한 mysite 가상 환경에 있는 Scripts 디렉터리의 activate 명령을 수행해야 한다.
# 다음 명령을 입력하여 mysite 가상 환경에 진입해 보자.
# [명령 프롬프트]
# C:\venvs>cd C:\venvs\mysite\Scripts
# C:\venvs\mysite\Scripts> activate
# (mysite) C:\venvs\mysite\Scripts>
# 그러면 C:/ 왼쪽에 (mysite)라는 프롬프트를 확인할 수 있다. 이름에서 볼 수 있듯 현재 여러분이 진입한 가상 환경을 의미한다.
# [4] 가상 환경에서 벗어나기
# 현재 진입한 가상 환경에서 벗어나려면 deactivate라는 명령을 실행하면 된다. 이 명령은 어느 위치에서 실행해도 상관없다.
# [명령 프롬프트]
# (mysite) C:\venvs\mysite\Scripts> deactivate
# 가상 환경에서 벗어났다면 C:/ 왼쪽에 있던 (mysite)라는 프롬프트가 사라졌을 것이다. 지금까지 가상 환경의 개념과 실습을 진행해 보았다.
# 가상 환경이라는 개념이 조금은 생소하겠지만 익혀 두면 여러분의 웹 프로그래밍 경험에 도움이 될 것이다.
# 장고 설치하기
# 드디어 장고를 설치할 차례가 왔다. 앞에서 만든 mysite 가상 환경에 장고를 설치해 보자.
# [1] 가상 환경인지 확인하기
# 명령 프롬프트 왼쪽에 (mysite) 프롬프트가 보이는지 확인하자. 만약 명령 프롬프트 왼쪽에 (mysite) 프롬프트가 보이지 않는다면
# 바로 이전의 실습을 참고하여 가상 환경에 진입한 상태에서 장고 설치를 진행하자.
# [명령 프롬프트]
# C:\venvs\mysite\Scripts> activate
# (mysite) C:\venvs\mysite\Scripts>
# [2] 가상 환경에서 장고 설치하기
# mysite 가상 환경에 진입한 상태에서 pip install django==3.1.3 명령을 입력하자. pip은 파이썬 라이브러리를 설치하고 관리해
# 주는 파이썬 도구이다. pip install django==3.1.3는 pip으로 장고 3.1.3 버전을 설치하는 명령이라고 생각하면 된다. 
# 다음 화면이 나오면 장고 설치가 잘 된 것이다.
# - 가상 환경 진입은 바로 이전 실습에서 공부했다.
# - pip은 '핍'이라 읽는다.
# [명령 프롬프트]
# (mysite) C:\venvs\mysite\Scripts> pip install django==3.1.3
# Collecting django
#   Using cached https://files.pythonhosted.org/packages/01/a5/fb3dad18422fcd4241d18460a1fe17542bfdeadcf74e3861d1a2dfc9e459/Django-3.1.3-py3-none-any.whl
# Collecting asgiref~=3.2.10 (from django)
#   Using cached https://files.pythonhosted.org/packages/d5/eb/64725b25f991010307fd18a9e0c1f0e6dff2f03622fc4bcbcdb2244f60d6/asgiref-3.2.10-py3-none-any.whl
# Collecting sqlparse>=0.2.2 (from django)
#   Using cached https://files.pythonhosted.org/packages/85/ee/6e821932f413a5c4b76be9c5936e313e4fc626b33f16e027866e1d60f588/sqlparse-0.3.1-py2.py3-none-any.whl
# Collecting pytz (from django)
#   Using cached https://files.pythonhosted.org/packages/4f/a4/879454d49688e2fad93e59d7d4efda580b783c745fd2ec2a3adf87b0808d/pytz-2020.1-py2.py3-none-any.whl
# Installing collected packages: asgiref, sqlparse, pytz, django
# Successfully installed asgiref-3.2.10 django-3.1.3 pytz-2020.1 sqlparse-0.3.1
# WARNING: You are using pip version 19.2.3, however version 20.2.3 is available.
# You should consider upgrading via the 'python -m pip install --upgrade pip' command.
# 그런데 마지막에 경고(WARNING) 문구가 보인다. pip이 최신 버전이 아니라는 내용이다.
# 개발자가 되고 싶다면 이런 경고 문구에 익숙해져야 한다.
# [3] pip 최신 버전으로 설치하기
# 경고 메시지에 따라 python -m pip install --upgrade pip 명령을 입력해 pip을 최신 버전으로 설치하자.
# [명령 프롬프트]
# (mysite) C:\venvs\mysite\Scripts> python -m pip install --upgrade pip
# Collecting pip
#   Downloading https://files.pythonhosted.org/packages/54/0c/d01aa759fdc501a58f431eb594a17495f15b88da142ce14b5845662c13f3/pip-20.0.2-py2.py3-none-any.whl (1.4MB)
#      |================================| 1.4MB 226kB/s
# Installing collected packages: pip
#   Found existing installation: pip 19.2.3
#     Uninstalling pip-19.2.3:
#       Successfully uninstalled pip-19.2.3
# Successfully installed pip-20.0.2

# [1-02 파이썬 설치하기]
# 앞에서 언급했듯 장고는 파이썬으로 만들어진 웹 프레임워크이다. 그래서 장고를 실행하기 위해서는 파이썬 설치가 필수이다.
# 파이썬은 파이썬 공식 홈페이지에서 설치 프로그램을 내려받아 설치하면 된다.
# 윈도우에서 파이썬 설치하기
# [1] 최신 파이썬 설치 파일 내려받기
# [2] 주의! 파이썬 설치 시 파이썬 경로 추가하기
# [3] 파이썬 설치 확인하기
# 윈도우에서 파이썬 설치하기
# [1] 최신 파이썬 설치 파일 내려받기
# 파이썬 공식 홈페이지에서 [Downloads] 메뉴를 누르고 윈도우용 파이썬 설치 파일을 내려받자. 다음 화면에서 <Python 3.8.x>을
# 누르면 된다. 참고로 이 책을 집필하는 시점의 파이썬 최신 버전은 3.8.5이다.
# 파이썬 공식 홈페이지 주소: www.python.org
# [2] 주의! 파이썬 설치 시 파이썬 경로 추가하기
# 방금 내려받은 설치 파일을 실행한다. 파이썬 설치 화면이 열리면 본격적으로 설치 작업을 하기 전에 반드시 아래쪽에 있는 
# <Add Python 3.8 to PATH> 옵션을 선택하자. 그다음 <Install Now>를 선택하면 바로 설치가 진행된다. 설치를 완료하면 
# <close>를 눌러 설치 프로그램을 종료한다.
# 파이썬이 설치된 경로를 시스템이 인식해야 명령 프롬프트 어느 위치에서나 python 명령을 실행할 수 있다. 그러나 많은 사람이
# 경로 추가 옵션을 선택하지 않아 오류가 발생한다. <Add Python 3.8 to PATH> 옵션을 체크했는지 반드시 확인하고 설치하기
# 바란다.
# [3] 파이썬 설치 확인하기
# 파이썬이 제대로 설치됐는지 확인하기 위해 명령 프롬프트를 열자. 윈도우 작업 표시줄에 있는 검색란에 cmd를 입력 후
# <Enter> 를 누르자. 명령 프롬프트가 열리면 다음 명령을 입력해 자신의 컴퓨터에 설치된 파이썬 버전을 확인해 보자. 
# 오류 없이 파이썬 버전이 제대로 출력되면 설치에 성공한 것이다.
# [명령 프롬프트]
# C:\Users\pahkey> python -V
# Python 3.8.5
# 만약 명령어를 제대로 입력했는데도 파이썬 버전이 나타나지 않고 '찾을 수 없는 명령'이라는 오류 메시지가 출력된다면 
# 앞의 설치 과정에서 경로 설정에 문제가 있을 가능성이 크다. 이때는 1단계에서 내려받은 설치 파일을 다시 실행해 
# <Uninstall>을 눌러 삭제한 후 2단계부터 다시 설치하자.

# [1-01 필자가 생각하는 장고란?]
# 장고 홈페이지에 가 보면 가장 먼저 다음과 같은 로고를 볼 수 있다.
# The web framework for perfectionists with deadlines. (마감에 쫓기는 완벽주의자를 위한 웹 프레임워크)
# 필자는 로고에 쓰여 있는 이 문구가 장고를 정말 잘 표현하는 슬로건이라 생각한다. 이 말은 '장고를 사용하면 웹 프로그램을
# 마감에 쫓기지 않을 정도로 빠르게 만들 수 있으면서도 완성도가 완벽에 가깝다' 정도로 해석할 수 있을 것 같다. 장고를 사용해
# 본 적이 없거나 웹 프로그래밍이 처음인 사람에게는 허황된 말처럼 들릴 수도 있을 것이다. 하지만 이 말만큼은 10년 이상 
# 장고를 사용한 필자의 말을 믿어 주면 좋겠다. 그러면 장고의 특징과 장점은 무엇일까?
# 장고는 웹 프로그램을 쉽고 빠르게 만들 수 있도록 도와주는 웹 프레임워크이다. 웹 프레임워크라는 표현을 처음 듣는 사람을 
# 위해 잠시 웹 프레임워크를 설명해 보겠다.
# 웹 프레임워크란?
# 웹 프로그램을 만들어 본 경험이 있는가? 만약 그런 경험이 있다면 웹 프로그램을 위해 얼마 나 많은 기능을 만들어야 하는지 
# 잘 알고 있을 것이다.
# 예를 들어 쿠키나 세션 처리, 로그인/로그아웃 처리, 권한 처리, 데이터베이스 처리 등 웹 프로그램을 위해 만들어야 할 기능이
# 정말 산더미처럼 많다. 하지만 웹 프레임워크를 사용하면 이런 기능들을 여러분이 일일이 만들 필요가 없다. 왜냐하면 웹 
# 프레임워크에는 그런 기능들이 이미 만들어져 있기 때문이다. 그저 웹 프레임워크에 있는 기능을 익혀서 사용하기만 하면 된다. 
# 쉽게 말해 웹 프레임워크는 웹 프로그램을 만들기 위한 스타터 키트라고 생각하면 된다. 그리고 파이썬으로 만들어진 웹
# 프레임워크 중 하나가 바로 장고이다.
# 얼마나 빨리 만들 수 있나?
# 장고의 몇 가지 규칙만 익히면 누구나 빠르게 웹 프로그램을 만들 수 있다. 웹 브라우저에 'Hello World'를 출력하려면 장고가
# 요구하는 간단한 url 규칙을 정의하고 다음과 같은 함수 하나만 작성하면 된다.
# [장고의 빠른 개발 속도를 보여 주는 예]
# def index(request):
#     return HttpResponse("Hello World")
# 장고는 튼튼한 웹 프레임워크이다
# 개발자가 웹 프로그램을 만들 때 가장 어렵게 느끼는 기능 중 하나는 바로 보안 기능이다. 이 세상에는 기상천외한 방법으로
# 웹 사이트를 괴롭히는 사람들이 있다. 이런 공격에 개발자 홀로 신속하게 대응하기는 무척 어려운 일이다. 하지만 걱정하지 마라.
# 장고는 이런 보안 공격을 기본으로 아주 잘 막아 준다. 그만큼 장고는 튼튼한 웹 프레임워크다. 예를 들어 SQL 인젝션, 
# XSS(cross-site scripting), CSRF(cross-site request forgery), 클릭재킹(clickjacking)과 같은 보안 공격을 기본으로 막아 준다.
# 즉, 장고를 사용하면 이런 보안 공격에 대한 코드를 여러분이 짤 필요가 없다.
# - SQL 인젝션은 악의적인 SQL을 주입하여 공격하는 방법이다.
# - XSS는 자바스크립트를 삽입해 공격하는 방법이다.
# - CSRF는 위조된 요청을 보내는 공격 방법이다.
# - 클릭재킹은 사용자의 의도하지 않은 클릭을 유도하는 공격 방법이다.
# 장고에는 여러 기능이 준비되어 있다
# 장고는 2005년에 등장하여 10년 이상의 세월을 감내한 베테랑 웹 프레임워크이다. 그동안 정말 무수히 많은 기능이 추가되고 또
# 다듬어졌다. 혹시 로그인 기능을 원하는가? 관리자 기능을 원하는가? 이미 장고에 있다. 이미 있을 뿐 아니라 너무나도 잘 
# 만들어져 있다. 한마디로 장고에는 여러분이 필요로 하는 웹 프로그램 개발을 위한 도구와 기능이 대부분 준비되어 있다.
# 필자는 장고를 공부할 여러분에게 '이미 만들어져 있는 기능을 새로 만드느라 애써 고생하지 말라'는 이야기를 꼭 해 주고 싶다.
# 장고는 재미있다
# 장고로 웹 프로그램을 만드는 것이 게임을 하는 것보다 재밌다고 하면 믿겠는가? 약간 과장이긴 하지만 무언가에 홀린 듯이
# 코딩을 하고 있는 필자 자신을 발견할 때가 있었는데, 그때가 바로 장고로 웹 프로그램을 만들고 있을 때였다. 정말이니
# 의심하지 말고 지금 당장 장고로 웹 프로그래밍을 시작해 보자.



# [0장 들어가기 전에]

# [0-01 머리말]
# 《Do it! 점프 투 파이썬》으로 파이썬 기초를 공부한 많은 사람들이 "이제 무엇을 공부해야 할까요?", "파이썬으로 무엇을 해볼 수 있나요?"와
# 같은 질문을 많이 한다. 그래서《Do it! 점프 투 장고》를 준비했다.
# 프로그래머로서 파이썬을 더 능숙하게 다루고 싶다면 이 책을!
# 파이썬을 공부하는 방법은 무척 다양하지만 필자는 웹 프로그래밍을 추천한다. 
# 보통 '웹 프로그래밍'이라 하면 사이트나 게시판 만들기를 생각하기 쉽다.
# 웹 프로그래밍은 웹 사이트 개발 외에도 게임이나 인공지능 분야에도 적용할 수 있으므로 한번 공부해 두면 여러분의 미래에 큰
# 도움이 될 것이다. 물론 웹 프로그래밍은 웹 개념, 데이터베이스, 모델링, 네트워크, 서버 등 관련 지식을 많이 배워야 하고, 
# 또 이런 지식이 어떻게 조합되어 동작하는지도 알아야 하므로 짧은 시간에 습득하기란 쉽지 않다. 그렇지만 웹 프로그래밍을 
# 공부한다면 분명 많은 프로그래밍 지식을 얻을 수 있을 것이다.



# [서론]
# "점프 투 장고"는 "파이보"라는 이름의 파이썬 게시판(Python Board) 서비스를 만들어가는 과정을 설명한 장고 입문서이다. 
# 파이썬 설치부터 시작하여 서비스 운영까지 웹 프로그래밍의 처음부터 끝까지 모든 것을 알 수 있도록 구성하였다.
# 이 책을 따라하다 보면 다음과 같은 웹 사이트가 만들어진다. (최종 결과물)
# http://django.pybo.kr
# 필자는 2008년부터 장고(Django)를 사용해 왔다. 필자가 운영하고 있는 위키독스(wikidocs.net)와 코딩도장(codingdojang.com)이 
# 바로 장고로 만들어진 웹 서비스이다. 오랜기간 장고를 운영하며 알게 된 지식과 경험들을 이 책을 통해 공유할 수 있도록
# 노력하였다.
# 책을 따라하다 생기는 질문은 파이보의 완성형인 아래사이트를 활용하도록 하자.
# 파이보 (파이썬 질문과 답변 게시판) - https://pybo.kr