from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Achievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    order = models.IntegerField(default=0)
    has_finished = models.BooleanField(default=False)
    aggregate = models.DecimalField(default=0.00,max_digits=3,decimal_places=2)

    class Meta:
        ordering = ['-order']

def create_achievements(sender, instance, created, **kwargs):
    if created:
        storyteller = Achievement.objects.create(user=instance,name="Storyteller Achievement",description=" To achieve this achievement, users need to share at least 15 personal stories on the website. They can do this by creating a profile on the website and submitting their stories through the post submission form. The more stories they share, the higher their chances of achieving this achievement.",order=1)
        bookworm = Achievement.objects.create(user=instance,name="Bookworm Achievement",description="To achieve this achievement, users need to buy and read a minimum of 5 books on the website. They can do this by exploring the different categories on the website and buying and reading books that interest them. They can then leave reviews that offer constructive criticism and feedback.",order=2)
        empathy_champion = Achievement.objects.create(user=instance,name="Empathy Champion Achievement",description="To achieve this achievement, users need to show empathy and support towards others by commenting on at least 20 stories or posts. They can do this by reading other people's stories and leaving supportive comments that show they understand and care about the person's experience. The more comments they leave, the higher their chances of achieving this achievement.",order=3)
        top_supporter = Achievement.objects.create(user=instance,name="Top Supporter Achievement",description="To achieve this achievement, users need to support the website by sharing it with others and promoting it on social media. They can do this by sharing links to the website on their social media accounts and encouraging others to check it out. Users can also support by following me on any of my social media accounts or donating to the site.",order=4)
        active_learner = Achievement.objects.create(user=instance,name="Active Learner Achievement",description="To achieve this achievement, users must read and learn from at least 10 books and 10 articles on the website. They can accomplish this by exploring the different categories on the website and reading books and articles that interest them. The more they read, the higher their chances of achieving this achievement.",order=5)
        mentor = Achievement.objects.create(user=instance,name="Mentor Achievement",description="To achieve this achievement, users need to leave 20 comments on the website providing guidance and advice to others based on their own life experiences. They can do this by reading other people's stories and leaving comments that offer advice and support.The more replies or likes they get, the higher their chances of achieving this achievement.",order=6)
        inspirational_speaker = Achievement.objects.create(user=instance,name="Inspirational Speaker Achievement",description="To achieve this achievement, users need to share stories that inspire others to make positive changes in their own lives. They can do this by sharing their own personal stories of overcoming challenges and achieving success. The more inspiring their stories and comments or likes they get, the higher their chances of achieving this achievement.",order=7)
        expert_contributor = Achievement.objects.create(user=instance,name="Expert Contributor Achievement",description="To achieve this achievement, users need to provide expert advice and insights on a particular topic. They can do this by sharing their knowledge and expertise through articles and books on the website. The more valuable their contributions, the higher their chances of achieving this achievement.",order=8)
        reviewer = Achievement.objects.create(user=instance,name="Reviewer Achievement",description="To achieve this achievement, users need to read and provide helpful feedback and reviews on at least 10 books and 10 articles on the website. They can do this by exploring the different categories on the website and reading books and articles on the website and leaving reviews that offer constructive criticism and feedback.",order=9)
        community_contributor = Achievement.objects.create(user=instance,name="Community Contributor Achievement",description="To achieve this achievement, users need to contribute to the community by participating in discussions and forums on the website. They can do this by answering 10 of other people's questions, sharing their own experiences, and offering advice and support to others. The more questions they answer, the higher their chances of achieving this achievement.",order=10)
        explorer = Achievement.objects.create(user=instance,name="Explorer Achievement",description="To achieve this achievement, users need to explore at least 10 different emotional phases and 10 life experiences. They can do this by reading and liking stories and articles that interest them in these different categories and exploring different perspectives. The more phases they explore, the higher their chances of achieving this achievement.",order=11)

        storyteller.save()
        bookworm.save()
        empathy_champion.save()
        top_supporter.save()
        active_learner.save()
        mentor.save()
        inspirational_speaker.save()
        expert_contributor.save()
        reviewer.save()
        community_contributor.save()
        explorer.save()

post_save.connect(create_achievements, sender=User)


