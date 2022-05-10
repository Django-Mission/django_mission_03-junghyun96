from tabnanny import verbose
from django.contrib import admin
from .models import Faq, Inquiry , Answer

@admin.register(Faq)
class FaqModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'update_at')
    list_filter = ('category', )
    search_fields =('title', )
    search_help_text = ('제목으로 검색이 가능합니다.')
    


class AnswerInlines(admin.TabularInline):
    model = Answer
    extra = 1
    max_num = 10
    verbose_name = '답변'
    verbose_name_plural = '문의 답변'

@admin.register(Inquiry)
class InquiryModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'create_at', 'writer')
    list_filter = ('category', )
    search_fields =('title', 'email', 'phoneNum', )
    search_help_text = ('제목, 이메일, 전화번호 로 검색이 가능합니다.')
    inlines = [ AnswerInlines ]


