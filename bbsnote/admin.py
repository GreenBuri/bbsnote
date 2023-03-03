from django.contrib import admin
from .models import Board

# Register your models here.
#관리자 페이지에서 모델 관리하기 : 데이터 검색을 위한 항목을 추가한다
class BoardAdmin(admin.ModelAdmin):
    search_fields = ['subject', 'content'] # subject(제목) 과 content(내용)을 검색해주는 검색창 생성
# Board 와 Comment를 어드민 페이지에서 확인하기 위해서 여기 추가한다!
admin.site.register(Board, BoardAdmin)


