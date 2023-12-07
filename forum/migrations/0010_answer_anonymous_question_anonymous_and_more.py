# Generated by Django 4.2.2 on 2023-08-10 19:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("forum", "0009_question_followers_delete_follow"),
    ]

    operations = [
        migrations.AddField(
            model_name="answer",
            name="anonymous",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="question",
            name="anonymous",
            field=models.BooleanField(default=False),
        ),
        migrations.RemoveField(
            model_name="answercomment",
            name="likes",
        ),
        migrations.DeleteModel(
            name="AnswerCommentLike",
        ),
        migrations.AddField(
            model_name="answercomment",
            name="likes",
            field=models.ManyToManyField(
                blank=True,
                related_name="answer_comment_likes",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]