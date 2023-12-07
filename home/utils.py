import nltk
nltk.download('stopwords')
nltk.download('punkt')
from django.shortcuts import render
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from forum.models import Question, Answer
from components.models import Post


def find_similar_posts(request, post_id):
    post = Post.objects.get(id=post_id)
    all_posts = Post.objects.exclude(id=post_id)
   
    # Preprocess the text body of the posts
    stop_words = stopwords.words('english')
    vectorizer = TfidfVectorizer(stop_words=stop_words)
    corpus = [post.body for post in all_posts]
    X = vectorizer.fit_transform(corpus)
   
    # Preprocess the text body of the current post
    current_post_body = post.body
    current_post_tokens = word_tokenize(current_post_body.lower())
    current_post_tokens = [token for token in current_post_tokens if token.isalnum()]
    current_post_body = ' '.join(current_post_tokens)
    current_post_vector = vectorizer.transform([current_post_body])
   
    # Calculate the cosine similarity between the current post and all other posts
    similarities = cosine_similarity(current_post_vector, X).flatten()
   
    # Sort the posts based on similarity in descending order
    posts_and_similarity = sorted(zip(all_posts, similarities), key=lambda x: x[1], reverse=True)

    similar_posts = []
    for post, similarity in posts_and_similarity:
        if similarity > 0.7:  # Define a threshold for similarity
            similar_posts.append(post)
   
    # Rertun the similar posts
    contexio = {
        'similar_posts': similar_posts,
        'post':post,
    }

    return contexio

def find_similar_questions(request, question_id):
    # Get the question with the given question_id
    question = Question.objects.get(id=question_id)
   
    # Get all questions excluding the current question
    all_questions = Question.objects.exclude(id=question_id)
   
    # Preprocess the text title of the questions
    stop_words = stopwords.words('english')
    vectorizer = TfidfVectorizer(stop_words=stop_words)
    corpus = [question.title for question in all_questions]
    X = vectorizer.fit_transform(corpus)
   
    # Preprocess the text title of the current question
    current_question_title = question.title
    current_question_tokens = word_tokenize(current_question_title.lower())
    current_question_tokens = [token for token in current_question_tokens if token.isalnum()]
    current_question_title = ' '.join(current_question_tokens)
    current_question_vector = vectorizer.transform([current_question_title])
   
    # Calculate the cosine similarity between the current question and all other questions
    similarities = cosine_similarity(current_question_vector, X).flatten()

    # Sort the questions based on similarity in descending order
    questions_and_similarity = sorted(zip(all_questions, similarities), key=lambda x: x[1], reverse=True)

    similar_questions = []
    for question, similarity in questions_and_similarity:
        if similarity > 0.7:  # Define a threshold for similarity
            similar_questions.append(question)
   
    # Rertun the similar questions
    contexio = {
        'similar_questions': similar_questions,
    }

    return contexio

def find_similar_answers(request, answer_id):
    # Get the answer with the given answer_id
    answer = Answer.objects.get(id=answer_id)
   
    # Get all answers excluding the current answer
    all_answers = Answer.objects.exclude(id=answer_id)
   
    # Preprocess the text content of the answers
    stop_words = stopwords.words('english')
    vectorizer = TfidfVectorizer(stop_words=stop_words)
    corpus = [answer.content for answer in all_answers]
    X = vectorizer.fit_transform(corpus)
   
    # Preprocess the text content of the current answer
    current_answer_content = answer.content
    current_answer_tokens = word_tokenize(current_answer_content.lower())
    current_answer_tokens = [token for token in current_answer_tokens if token.isalnum()]
    current_answer_content = ' '.join(current_answer_tokens)
    current_answer_vector = vectorizer.transform([current_answer_content])
   
    # Calculate the cosine similarity between the current answer and all other answers
    similarities = cosine_similarity(current_answer_vector, X).flatten()

    # Sort the answers based on similarity in descending order
    answers_and_similarity = sorted(zip(all_answers, similarities), key=lambda x: x[1], reverse=True)

    similar_answers = []
    for answer, similarity in answers_and_similarity:
        if similarity > 0.7:  # Define a threshold for similarity
            similar_answers.append(answer)
   
    # Rertun the similar answers
    contexio = {
        'similar_answers': similar_answers,
    }

    return contexio