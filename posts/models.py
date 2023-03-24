from django.db import models


class TimeStampedModel(models.Model):
    """TimeStamped Abstract 모델"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimeStampedModel):
    title = models.CharField(verbose_name="게시글 제목", max_length=50)
    content = models.TextField(verbose_name="게시글 내용")
    image = models.ImageField(verbose_name="게시글 사진", upload_to="posts")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "posts"


class Comment(TimeStampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment_post")
    comment = models.TextField(verbose_name="댓글 내용")

    def __str__(self):
        return self.comment

    class Meta:
        db_table = "comments"