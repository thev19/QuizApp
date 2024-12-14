from django.db import models

class Question(models.Model):
    text = models.TextField()
    
    def __str__(self):
        return self.text[:50]

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    
    def __str__(self):
        return self.text

class QuizSession(models.Model):
    total_questions = models.IntegerField(default=0)
    correct_answers = models.IntegerField(default=0)
    incorrect_answers = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def update_stats(self, is_correct):
        self.total_questions += 1
        if is_correct:
            self.correct_answers += 1
        else:
            self.incorrect_answers += 1
        self.save()