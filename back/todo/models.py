from django.db import models


class BaseModel(models.Model):
    created = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=False,
        verbose_name='생성 일시',
        help_text='데이터가 생성된 날짜입니다.'
    )
    updated = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=False,
        verbose_name='수정 일시',
        help_text='데이터가 수정된 날짜입니다.'
    )

    class Meta:
        abstract = True


class Todo(models.Model):
    title = models.CharField(
        max_length=64,
        verbose_name='TODO 제목',
        help_text='TODO 제목입니다.'
    )
    description = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        verbose_name='TODO 설명',
        help_text='TODO 설명입니다.'
    )
    author = models.CharField(
        max_length=16,
        verbose_name='TODO 작성자',
        help_text='TODO 작성자를 나타냅니다.'
    )
    due_date = models.DateTimeField(
        verbose_name='TODO 마감일',
        help_text='TODO 마감일을 나타냅니다.'
    )
    completed = models.BooleanField(
        default=False,
        verbose_name='TODO 완료 여부',
        help_text='TODO 완료 여부를 나타냅니다.'
    )

    class Meta:
        verbose_name = 'TODO 리스트'
        verbose_name_plural = 'TODO 리스트(들)'

    def __str__(self):
        return f'Todo-{self.author}'
