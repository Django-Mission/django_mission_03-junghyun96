from tkinter import CASCADE
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# 앱의 자주묻는 질문
class Faq(models.Model):
    #제목 필드
    title= models.CharField(verbose_name='제목', max_length=20, null=True, default=None)
    #카테고리 필드
    CATEGORY_CHOICE = [
        ('1', '상품 문의'),
        ('2', '교환&환불 문의'),
        ('3', '배송 문의'),
    ]
    category = models.CharField(verbose_name='카테고리',max_length=10, choices=CATEGORY_CHOICE, default= 1)
    #최종수정일시 필드
    update_at = models.DateTimeField(verbose_name='최종 수정 일시', auto_now=True)



# 1:1문의
class Inquiry(models.Model):
    #질문제목 필드
    title= models.CharField(verbose_name='제목', max_length=20, null=True, default=None)
    #이메일
    email = models.EmailField(verbose_name='이메일', blank=True)
    #전화번호
    phoneNum = models.CharField(verbose_name='전화번호',max_length=20, null=True ,default=None)
    #카테고리 필드
    CATEGORY_ONE = '1'
    CATEGORY_TWO = '2'
    CATEGORY_THREE = '3'

    CATEGORY_CHOICE = [
        (CATEGORY_ONE, '상품 문의'),
        (CATEGORY_TWO, '교환&환불 문의'),
        (CATEGORY_THREE, '배송 문의'),
    ]
    category = models.CharField(verbose_name='카테고리',max_length=10, choices=CATEGORY_CHOICE, default= 1)
    #생성일 필드
    create_at = models.DateTimeField(verbose_name='최종 수정 일시', auto_now_add=True)
    #생성자 필드
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True , blank=True)


    #검색필드(제목,이메일,전화번호)
    #필터필드(카테고리)
    #인라인모델(답변 Answer)


# 답변
class Answer(models.Model):
#     # 1:1 문의 모델에 인라인모델로 추가
    answer = models.TextField(verbose_name='답변내용')
    create_at = models.DateTimeField(verbose_name='최종 수정 일시', auto_now_add=True)
    inquiry = models.ForeignKey(to=Inquiry, on_delete=models.CASCADE)
