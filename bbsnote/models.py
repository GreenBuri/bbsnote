from django.db import models

# 게시판 모델 만들기 : 아래와 같이 두개의 클래스를 만들었다는 것은, 2개의 테이블을 만든 것과 같음. 이대로 DB에 올릴것!
# Create your models here.
class Board(models.Model): #게시글 모델, Model은 DB에서 가져오는것 => DB에 테이블을 가져올 것!
    subject = models.CharField(max_length=200) #게시글 제목임! 최대 문자열 길이를 200으로.
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self): 
        #이 객체(Board=self)를 호출했을 때 리턴하고자 하는 값을 세팅해주는 함수. : 여기선 제목 호출해주는!!
        return self.subject

class Comment(models.Model): #댓글 모델, Model은 DB에서 가져오는것
    board = models.ForeignKey(Board, on_delete=models.CASCADE)#해당하는 게시글의 댓글이란 의미로 Foreign키 속성 부여
    #on_delete, CACADE면! => 같이 지워지라는 것. 게시글이 사라지면 댓글도 사라지도록!!
    #이렇게 Foreign키 지정이 가능한 이유는 migrate하면서 장고에서 자동으로 migrations 아래에 Board와 Comment에 대한 id를 만들고, PK 지정을 해주기 때문.
    content = models.TextField()
    create_date = models.DateTimeField()

