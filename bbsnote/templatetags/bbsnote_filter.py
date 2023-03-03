#만들고자 하는 게시물 번호 공식은 일련번호=전체 게시물 개수 - 시작인덱스 - 현재 인덱스 + 1
from django import template #장고로부터 템플릿 정보 모듈을 가져오겠다.(우리 템플릿 폴더 안 파일 가져오는 것 아님!)

register = template.Library()

@register.filter
#filter에 - 내장함수가 없어서, 방금 -기능을 가진 sub함수를 만들어준것!
def sub(value, arg):
    return value - arg 