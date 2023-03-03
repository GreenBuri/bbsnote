from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Board, Comment
from django.utils import timezone
from .forms import BoardForm
from django.core.paginator import Paginator #게시판 페이징 적용하기

# Create your views here.
def index(request): #index 함수 정의 : 매개변수는 request(요청)/ 요청이 들어오게 되면 index를 실행시켜라!
    #입력 인자
    page = request.GET.get('page', 1)
    #조회
    board_list = Board.objects.order_by('-create_date') #-create_date를 기준으로 Board 내 데이터 정리.
    #페이징 처리 : 전체 데이터를 기준으로 해서 페이징을 잡아야 한다.
    paginator = Paginator(board_list, 5) #board_list를 1페이지에 5개씩 끊어서 보겠다
    page_obj = paginator.get_page(page) #page_obj 변수에 paginator의 페이지 정보를 가져와 넣겠다.
    #context에 board_list를 그대로 넣는 게 아닌 page_obj를 넣겠다.->여기까지 하면 1페이지(5개)만 보이고 짤린다!
    #이제 프론트 단에서 이후 페이지도 출력되도록 해줘야 한다!(board_list.html에 작성)
    context = {'board_list': page_obj} # context(키는 보드리스트, 값은 위에 정의한 board_list)를 딕셔너리로 정의. 
    #return HttpResponse("bbsnote에 오신 것을 환영합니다!");
    return render(request, 'bbsnote/board_list.html', context) 
    #render 함수! request 정보 기준으로 board_list.html 템플릿에 context 딕셔너리 데이터를 바인딩 시켜서 넘겨주겠다!
    #그러면 bbsnote/ url로 리퀘스트 왔을 때 => views아래 index 함수를 실행하게 되고 => models 아래 Board 모델을 불러옴.
    #=> Board 문서를 불러온 뒤 -create_date(앞에 - 가 붙어서 desc로 create_date 기준하여 불러옴)를 기준으로 불러왔고
    #=> render 함수를 통해 이 정보를 board_list.html로 context 정보를 바인딩해준 뒤, board_list 안 내용대로 완성해
    #=> 클라이언트한테 다시 보내준 것이다.



#상세 페이지 기능 구현하기
def detail(request, board_id):
    board = Board.objects.get(id=board_id) #요청 정보를 가지고옴. SELECT * FROM bbsnote_Board WHERE id=3 과 같다.(3은 유동적)
    context = {'board':board}
    return render(request,'bbsnote/board_detail.html',context) #detail함수에 context에 담긴 정보를 담아 바인딩한다!

def comment_create(request, board_id):
    board =Board.objects.get(id=board_id)
    # comment = Comment(board=board, content=request.POST.get('content'), create_data=timezone.now())
    # comment.save()
    board.comment_set.create(content=request.POST.get('content'), create_date=timezone.now())
    #위 표현이나 위 두줄 표현이나 같다!
    return redirect('bbsnote:detail', board_id=board.id)
#redirect 는 render하고 다르게 데이터를 바인딩 해 보내는 것이 아니라, 현재 받은 함수 안의 board 정보의 id 값을 그대로 받아서 넘김.
#그리고 models 에 Comment 클래스를 넣어놓긴 했지만, 기능만 구현해 둔 것으로 아직 댓글남기는 기능은 추가해두지 않았다!

def board_create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST) #form을 POST방식으로 들어온 리퀘스트 전부다 BoardForm으로!
        if form.is_valid(): #위 조건에 만족한다면
            board = form.save(commit=False) #데이터를 저장은 하겠지만, 커밋은 아직 안하겠다!
            board.create_date = timezone.now() #제목과 내용이 등록될 때, 작성시점도 저장되도록!(이때문에 위에 커밋을 안한것)
            board.save() #세이브하고 커밋해줘. save의 기본값이 commit=True임!
            return redirect('bbsnote:index')
    #위 큰 if문은 데이터가 있으면 그대로 보내고.. else의 경우! 입력할 수 있는 창을 띄우도록 하는 것!
    else:
        form = BoardForm()
    return render(request, 'bbsnote/board_form.html', {'form':form})
    # 즉 board_create함수에 form(프론트에서 데이터 작성..)에 작성된 데이터를 바인딩한다(subject, content, timezone)