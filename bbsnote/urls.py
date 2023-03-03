#config 아래에만 url을 주구창창 넣으면 너무 복잡해지니! bbsnote관련 url은 쪼개서 여기서 작업하자.

from django.urls import path
from . import views

app_name = 'bbsnote'

urlpatterns = [
    path('',views.index, name='index'), #config/urls -> bbsnote/urls -> bbsnote/views.py 실행!
    path('<int:board_id>/',views.detail, name='detail'),
    # url을 정의해주고, views 아래 detail함수를 불러온다 -> 
    # int는 path_converter라 부르는 기능. board_id는 컨버터를 통해 반환 받은 값(int는 board_id에 숫자가 매핑되었음을 의미)
    # <type: name>으로 작성됨. 지정한 타입의 name변수를 view함수로 넘기는 역할이다.
    # converter를 쓰는 이유는, board_id가 게시글별로 바뀌기 때문이다.
    # 이런 path_converter는 str, int, slug(영문대소문자,숫자,-,_), uuid(모든 문자 소문자, - 포함), path(str + /) 가 있다.
    path('comment/create/<int:board_id>/', views.comment_create, name='comment_create'),
    # 해당 게시글의 댓글임을 표시하기 위해 commnet url에도 board_id를 넣어줌!
    path('board/create/', views.board_create, name='board_create'),
]
