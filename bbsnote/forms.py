#forms.py를 통해 게시글 등록 기능 만들기.
from django import forms
from bbsnote.models import Board
# BoardForm은 프론트와 백엔드(모델:Board) 간의 중간다리 역할을 해줌!
class BoardForm(forms.ModelForm):
    class Meta:
        model = Board #참조하고자 하는 모델이 Board고!
        fields = ['subject', 'content'] #프론트에 있는 Form에서subject와 content를 넘겨받아 백엔드의 BOARD(모델)로 넘겨주겠다!