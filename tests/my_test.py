# -*- coding: utf-8 -*-
import pytest
from utils import *
from json import JSONDecodeError

posts_parameters = [
    ([{'content': 'Привет я тут делаю #тест #функции на #pyton'}], 'content',
     [{'content': 'Привет я тут делаю #тест #функции на #pyton', 'teg_words': ['тест', 'функции', 'pyton']}]),
    ([{'content': 'Привет я тут делаю тест функции на pyton'}], 'content',
     [{'content': 'Привет я тут делаю тест функции на pyton', 'teg_words': []}]),
    ([{'content': 'Привет я тут делаю тест функ#ции на pyton'}], 'content',
     [{'content': 'Привет я тут делаю тест функ#ции на pyton', 'teg_words': []}]),
    (
        [{'content': 'Привет я тут делаю #тест функции на pyton'},
         {'content': 'Привет я тут делаю тест функции на #pyton'},
         {'content': 'Привет я тут делаю #тест #функции на #pyton'}], 'content',
        [{'content': 'Привет я тут делаю #тест функции на pyton', 'teg_words': ['тест']},
         {'content': 'Привет я тут делаю тест функции на #pyton', 'teg_words': ['pyton']},
         {'content': 'Привет я тут делаю #тест #функции на #pyton', 'teg_words': ['тест', 'функции', 'pyton']}]),
    ([{'content': 'Привет я тут делаю тест функ#ции на pyton'}, {'content': 'Привет я тут делаю тест функции на pyton'},
      {'content': 'Привет я тут делаю #тест #функции на #pyton'}], 'content',
     [{'content': 'Привет я тут делаю тест функ#ции на pyton', 'teg_words': []},
      {'content': 'Привет я тут делаю тест функции на pyton', 'teg_words': []},
      {'content': 'Привет я тут делаю #тест #функции на #pyton', 'teg_words': ['тест', 'функции', 'pyton']}]),
    ([{'text': 'Привет я тут делаю #тест #функции на #pyton'}], 'text',
     [{'text': 'Привет я тут делаю #тест #функции на #pyton', 'teg_words': ['тест', 'функции', 'pyton']}]),
]


@pytest.mark.parametrize("posts, key, posts_tag", posts_parameters)
def test_posts_wish_teg(posts, key, posts_tag):
    assert posts_wish_teg(posts, key) == posts_tag


posts_exceptions = [
    ([{'content': 'Привет я тут делаю #тест #функции на #pyton'}], 'text', KeyError),
    ('Привет я тут делаю #тест #функции на #pyton', 'pk', TypeError),
]


@pytest.mark.parametrize("posts, key, exception", posts_exceptions)
def test_posts_wish_teg_exceptions(posts, key, exception):
    with pytest.raises(exception):
        posts_wish_teg(posts, key)


file_name_parameters = [
    ('data/post.json', {'poster_name': 'leo', 'poster_avatar': 'https://randus.org/avatars/w/c1819dbdffffff18.png',
                        'pic': 'https://images.unsplash.com/photo-1525351326368-efbb5cb6814d?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80',
                        'content': 'Ага, опять еда! Квадратная тарелка в квадратном кадре. А на тарелке, наверное, пирог! Мне было так жаль, что я не могу ее съесть. Я боялась, что они заметят, и если я не съем это, то, значит, они все подумают, что я плохая девочка... Но потом мне вспомнилось, как они на меня смотрели. Когда я была маленькой, на кухне всегда были родители, бабушка, дедушка, дядя Борис... Все вместе. И всегда одна я, потому что все остальные приходили туда лишь изредка. Мне казалось, если бы все ходили на работу, как и я, в этот свой офис, было бы совсем неинтересно.',
                        'views_count': 376, 'likes_count': 154, 'pk': 1}),
    ('data/comments.json', [{
        "post_id": 1,
        "commenter_name": "hanna",
        "comment": "Очень здорово!",
        "pk": 1
    },
        {
            "post_id": 1,
            "commenter_name": "jlia",
            "comment": ":)",
            "pk": 2
        },
        {
            "post_id": 2,
            "commenter_name": "leo",
            "comment": "Часть вижу такие фото у друзей! Это новый тренд?",
            "pk": 8
        },
        {
            "post_id": 3,
            "commenter_name": "johnny",
            "comment": "Выглядит неплохо )",
            "pk": 9
        }]),
]


@pytest.mark.parametrize("file_name, content", file_name_parameters)
def test_read_file(file_name, content):
    assert read_file(file_name) == content


file_name_exceptions = [
    ('data/post1.json', FileNotFoundError),
    ('data/data.txt', JSONDecodeError),
]


@pytest.mark.parametrize("file_name, exception", file_name_exceptions)
def test_read_file_exceptions(file_name, exception):
    with pytest.raises(exception):
        read_file(file_name)


file_name_parameters = [
    ('data/posts.json',
     [
         {
             "poster_name": "leo",
             "poster_avatar": "https://randus.org/avatars/w/c1819dbdffffff18.png",
             "pic": "https://images.unsplash.com/photo-1525351326368-efbb5cb6814d?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80",
             "content": "Ага, опять еда! Квадратная тарелка в квадратном кадре. А на тарелке, наверное, пирог! Мне было так жаль, что я не могу ее съесть. Я боялась, что они заметят, и если я не съем это, то, значит, они все подумают, что я плохая девочка... Но потом мне вспомнилось, как они на меня смотрели. Когда я была маленькой, на кухне всегда были родители, бабушка, дедушка, дядя Борис... Все вместе. И всегда одна я, потому что все остальные приходили туда лишь изредка. Мне казалось, если бы все ходили на работу, как и я, в этот свой офис, было бы совсем неинтересно.",
             "views_count": 376,
             "likes_count": 154,
             "pk": 1
         },
         {
             "poster_name": "johnny",
             "poster_avatar": "https://randus.org/avatars/m/00183c7e3c382499.png",
             "pic": "https://images.unsplash.com/photo-1592660716763-09efba6db4e3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80",
             "content": "Вышел погулять днем, пока все на работе. На улице странные штуки, похожие на колонны, которые кто-то сгрыз – незаметно и аккуратно, так, что даже мусора не осталось. И еще много странного: например, почему-то все птицы летают, как птицы, и, похоже, им это совершенно не мешает. Или вот еще: в траве – как будто следы от чьих-то ног, хотя вроде бы я ходил довольно тихо... На следующий день было совсем пусто. Я вышел и почувствовал себя очень одиноко. Пошел к остановке. Вокруг было много народу – и все одинаковые. Как будто все они приехали сюда из одного дома и вышли на этом перекрестке после работы, чтобы не возвращаться в свои квартиры.",
             "views_count": 233,
             "likes_count": 101,
             "pk": 2
         }]
     ),
    ('data/post.json',
     {
         "poster_name": "leo",
         "poster_avatar": "https://randus.org/avatars/w/c1819dbdffffff18.png",
         "pic": "https://images.unsplash.com/photo-1525351326368-efbb5cb6814d?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80",
         "content": "Ага, опять еда! Квадратная тарелка в квадратном кадре. А на тарелке, наверное, пирог! Мне было так жаль, что я не могу ее съесть. Я боялась, что они заметят, и если я не съем это, то, значит, они все подумают, что я плохая девочка... Но потом мне вспомнилось, как они на меня смотрели. Когда я была маленькой, на кухне всегда были родители, бабушка, дедушка, дядя Борис... Все вместе. И всегда одна я, потому что все остальные приходили туда лишь изредка. Мне казалось, если бы все ходили на работу, как и я, в этот свой офис, было бы совсем неинтересно.",
         "views_count": 376,
         "likes_count": 154,
         "pk": 1
     }
     )
]


@pytest.mark.parametrize("file_name, content", file_name_parameters)
def test_write_file_json(file_name, content):
    write_file_json(file_name, content)
    assert read_file(file_name) == content


file_name_parameters = [
    ({
         "poster_name": "johnny",
         "poster_avatar": "https://randus.org/avatars/m/00183c7e3c382499.png",
         "pic": "https://images.unsplash.com/photo-1592660716763-09efba6db4e3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80",
         "content": "Вышел погулять днем, пока все на работе. На улице странные штуки, похожие на колонны, которые кто-то сгрыз – незаметно и аккуратно, так, что даже мусора не осталось. И еще много странного: например, почему-то все птицы летают, как птицы, и, похоже, им это совершенно не мешает. Или вот еще: в траве – как будто следы от чьих-то ног, хотя вроде бы я ходил довольно тихо... На следующий день было совсем пусто. Я вышел и почувствовал себя очень одиноко. Пошел к остановке. Вокруг было много народу – и все одинаковые. Как будто все они приехали сюда из одного дома и вышли на этом перекрестке после работы, чтобы не возвращаться в свои квартиры.",
         "views_count": 233,
         "likes_count": 101,
         "pk": 2
     },
     'data/bookmarks.json',
     [
         {
             "poster_name": "leo",
             "poster_avatar": "https://randus.org/avatars/w/c1819dbdffffff18.png",
             "pic": "https://images.unsplash.com/photo-1525351326368-efbb5cb6814d?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80",
             "content": "Ага, опять еда! Квадратная тарелка в квадратном кадре. А на тарелке, наверное, пирог! Мне было так жаль, что я не могу ее съесть. Я боялась, что они заметят, и если я не съем это, то, значит, они все подумают, что я плохая девочка... Но потом мне вспомнилось, как они на меня смотрели. Когда я была маленькой, на кухне всегда были родители, бабушка, дедушка, дядя Борис... Все вместе. И всегда одна я, потому что все остальные приходили туда лишь изредка. Мне казалось, если бы все ходили на работу, как и я, в этот свой офис, было бы совсем неинтересно.",
             "views_count": 376,
             "likes_count": 154,
             "pk": 1
         },
         {
             "poster_name": "johnny",
             "poster_avatar": "https://randus.org/avatars/m/00183c7e3c382499.png",
             "pic": "https://images.unsplash.com/photo-1592660716763-09efba6db4e3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80",
             "content": "Вышел погулять днем, пока все на работе. На улице странные штуки, похожие на колонны, которые кто-то сгрыз – незаметно и аккуратно, так, что даже мусора не осталось. И еще много странного: например, почему-то все птицы летают, как птицы, и, похоже, им это совершенно не мешает. Или вот еще: в траве – как будто следы от чьих-то ног, хотя вроде бы я ходил довольно тихо... На следующий день было совсем пусто. Я вышел и почувствовал себя очень одиноко. Пошел к остановке. Вокруг было много народу – и все одинаковые. Как будто все они приехали сюда из одного дома и вышли на этом перекрестке после работы, чтобы не возвращаться в свои квартиры.",
             "views_count": 233,
             "likes_count": 101,
             "pk": 2
         }]
    ),
    ({
         "poster_name": "johnny",
         "poster_avatar": "https://randus.org/avatars/m/00183c7e3c382499.png",
         "pic": "https://images.unsplash.com/photo-1592660716763-09efba6db4e3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80",
         "content": "Вышел погулять днем, пока все на работе. На улице странные штуки, похожие на колонны, которые кто-то сгрыз – незаметно и аккуратно, так, что даже мусора не осталось. И еще много странного: например, почему-то все птицы летают, как птицы, и, похоже, им это совершенно не мешает. Или вот еще: в траве – как будто следы от чьих-то ног, хотя вроде бы я ходил довольно тихо... На следующий день было совсем пусто. Я вышел и почувствовал себя очень одиноко. Пошел к остановке. Вокруг было много народу – и все одинаковые. Как будто все они приехали сюда из одного дома и вышли на этом перекрестке после работы, чтобы не возвращаться в свои квартиры.",
         "views_count": 233,
         "likes_count": 101,
         "pk": 2
     },
     'data/bookmarks2.json',
     [
         {
             "poster_name": "johnny",
             "poster_avatar": "https://randus.org/avatars/m/00183c7e3c382499.png",
             "pic": "https://images.unsplash.com/photo-1592660716763-09efba6db4e3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80",
             "content": "Вышел погулять днем, пока все на работе. На улице странные штуки, похожие на колонны, которые кто-то сгрыз – незаметно и аккуратно, так, что даже мусора не осталось. И еще много странного: например, почему-то все птицы летают, как птицы, и, похоже, им это совершенно не мешает. Или вот еще: в траве – как будто следы от чьих-то ног, хотя вроде бы я ходил довольно тихо... На следующий день было совсем пусто. Я вышел и почувствовал себя очень одиноко. Пошел к остановке. Вокруг было много народу – и все одинаковые. Как будто все они приехали сюда из одного дома и вышли на этом перекрестке после работы, чтобы не возвращаться в свои квартиры.",
             "views_count": 233,
             "likes_count": 101,
             "pk": 2
         }]
    )

]


@pytest.mark.parametrize("content, file_name, content2", file_name_parameters)
def test_add_post_in_bookmarks(content, file_name, content2):
    add_post_in_bookmarks(content, file_name)
    assert read_file(file_name) == content2


file_name_exceptions = [
    ({
         "poster_name": "johnny",
         "poster_avatar": "https://randus.org/avatars/m/00183c7e3c382499.png",
         "pic": "https://images.unsplash.com/photo-1592660716763-09efba6db4e3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80",
         "content": "Вышел погулять днем, пока все на работе. На улице странные штуки, похожие на колонны, которые кто-то сгрыз – незаметно и аккуратно, так, что даже мусора не осталось. И еще много странного: например, почему-то все птицы летают, как птицы, и, похоже, им это совершенно не мешает. Или вот еще: в траве – как будто следы от чьих-то ног, хотя вроде бы я ходил довольно тихо... На следующий день было совсем пусто. Я вышел и почувствовал себя очень одиноко. Пошел к остановке. Вокруг было много народу – и все одинаковые. Как будто все они приехали сюда из одного дома и вышли на этом перекрестке после работы, чтобы не возвращаться в свои квартиры.",
         "views_count": 233,
         "likes_count": 101,
         "pk": 2
     },
     'data/post.json',
     TypeError
    ),
    ({
         "poster_name": "johnny",
         "poster_avatar": "https://randus.org/avatars/m/00183c7e3c382499.png",
         "pic": "https://images.unsplash.com/photo-1592660716763-09efba6db4e3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80",
         "content": "Вышел погулять днем, пока все на работе. На улице странные штуки, похожие на колонны, которые кто-то сгрыз – незаметно и аккуратно, так, что даже мусора не осталось. И еще много странного: например, почему-то все птицы летают, как птицы, и, похоже, им это совершенно не мешает. Или вот еще: в траве – как будто следы от чьих-то ног, хотя вроде бы я ходил довольно тихо... На следующий день было совсем пусто. Я вышел и почувствовал себя очень одиноко. Пошел к остановке. Вокруг было много народу – и все одинаковые. Как будто все они приехали сюда из одного дома и вышли на этом перекрестке после работы, чтобы не возвращаться в свои квартиры.",
         "views_count": 233,
         "likes_count": 101,
         "pk": 2
     },
     'data/data.txt',
     JSONDecodeError
    ),
    ({
         "poster_name": "johnny",
         "poster_avatar": "https://randus.org/avatars/m/00183c7e3c382499.png",
         "pic": "https://images.unsplash.com/photo-1592660716763-09efba6db4e3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80",
         "content": "Вышел погулять днем, пока все на работе. На улице странные штуки, похожие на колонны, которые кто-то сгрыз – незаметно и аккуратно, так, что даже мусора не осталось. И еще много странного: например, почему-то все птицы летают, как птицы, и, похоже, им это совершенно не мешает. Или вот еще: в траве – как будто следы от чьих-то ног, хотя вроде бы я ходил довольно тихо... На следующий день было совсем пусто. Я вышел и почувствовал себя очень одиноко. Пошел к остановке. Вокруг было много народу – и все одинаковые. Как будто все они приехали сюда из одного дома и вышли на этом перекрестке после работы, чтобы не возвращаться в свои квартиры.",
         "views_count": 233,
         "likes_count": 101,
         "post_id": 2
     },
     'data/post.json',
     KeyError
    )
]


@pytest.mark.parametrize("content, file_name, exception", file_name_exceptions)
def test_add_post_in_bookmarks(content, file_name, exception):
    with pytest.raises(exception):
        add_post_in_bookmarks(content, file_name)


file_name_parameters = [
    (2,
     'data/bookmarks.json',
     [
         {
             "poster_name": "leo",
             "poster_avatar": "https://randus.org/avatars/w/c1819dbdffffff18.png",
             "pic": "https://images.unsplash.com/photo-1525351326368-efbb5cb6814d?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80",
             "content": "Ага, опять еда! Квадратная тарелка в квадратном кадре. А на тарелке, наверное, пирог! Мне было так жаль, что я не могу ее съесть. Я боялась, что они заметят, и если я не съем это, то, значит, они все подумают, что я плохая девочка... Но потом мне вспомнилось, как они на меня смотрели. Когда я была маленькой, на кухне всегда были родители, бабушка, дедушка, дядя Борис... Все вместе. И всегда одна я, потому что все остальные приходили туда лишь изредка. Мне казалось, если бы все ходили на работу, как и я, в этот свой офис, было бы совсем неинтересно.",
             "views_count": 376,
             "likes_count": 154,
             "pk": 1
         }]
    ),
    (3,
     'data/bookmarks2.json',
     [
         {
             "poster_name": "johnny",
             "poster_avatar": "https://randus.org/avatars/m/00183c7e3c382499.png",
             "pic": "https://images.unsplash.com/photo-1592660716763-09efba6db4e3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80",
             "content": "Вышел погулять днем, пока все на работе. На улице странные штуки, похожие на колонны, которые кто-то сгрыз – незаметно и аккуратно, так, что даже мусора не осталось. И еще много странного: например, почему-то все птицы летают, как птицы, и, похоже, им это совершенно не мешает. Или вот еще: в траве – как будто следы от чьих-то ног, хотя вроде бы я ходил довольно тихо... На следующий день было совсем пусто. Я вышел и почувствовал себя очень одиноко. Пошел к остановке. Вокруг было много народу – и все одинаковые. Как будто все они приехали сюда из одного дома и вышли на этом перекрестке после работы, чтобы не возвращаться в свои квартиры.",
             "views_count": 233,
             "likes_count": 101,
             "pk": 2
         }]
    )

]


@pytest.mark.parametrize("post_id, file_name, content", file_name_parameters)
def test_del_post_from_bookmarks(post_id, file_name, content):
    del_post_from_bookmarks(post_id, file_name)
    assert read_file(file_name) == content


values_parameters = [
    ([{'poster_name': 'leo', 'poster_avatar': 'https://randus.org/avatars/w/c1819dbdffffff18.png',
       'pic': 'https://images.unsplash.com/photo-1525351326368-efbb5cb6814d?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80',
       'content': 'Ага, опять еда! Квадратная тарелка в квадратном кадре. А на тарелке, наверное, пирог! Мне было так жаль, что я не могу ее съесть. Я боялась, что они заметят, и если я не съем это, то, значит, они все подумают, что я плохая девочка... Но потом мне вспомнилось, как они на меня смотрели. Когда я была маленькой, на кухне всегда были родители, бабушка, дедушка, дядя Борис... Все вместе. И всегда одна я, потому что все остальные приходили туда лишь изредка. Мне казалось, если бы все ходили на работу, как и я, в этот свой офис, было бы совсем неинтересно.',
       'views_count': 376, 'likes_count': 154, 'pk': 1},
      {'poster_name': 'johnny', 'poster_avatar': 'https://randus.org/avatars/m/00183c7e3c382499.png',
       'pic': 'https://images.unsplash.com/photo-1592660716763-09efba6db4e3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80',
       'content': 'Вышел погулять днем, пока все на работе. На улице странные штуки, похожие на колонны, которые кто-то сгрыз – незаметно и аккуратно, так, что даже мусора не осталось. И еще много странного: например, почему-то все птицы летают, как птицы, и, похоже, им это совершенно не мешает. Или вот еще: в траве – как будто следы от чьих-то ног, хотя вроде бы я ходил довольно тихо... На следующий день было совсем пусто. Я вышел и почувствовал себя очень одиноко. Пошел к остановке. Вокруг было много народу – и все одинаковые. Как будто все они приехали сюда из одного дома и вышли на этом перекрестке после работы, чтобы не возвращаться в свои квартиры.',
       'views_count': 233, 'likes_count': 101, 'pk': 2},
      {'poster_name': 'hank', 'poster_avatar': 'https://randus.org/avatars/m/383c7e7e3c3c1818.png',
       'pic': 'https://images.unsplash.com/photo-1612450632008-22c2a5437dc1?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80',
       'content': 'Смотрите-ка – ржавые елки! Раньше на этом месте была свалка старых машин, а потом все засыпали песком. Теперь тут ничего не растет – только ржавые елки , кусты и грязь. Да и не может тут ничего расти: слишком много пыли и песка. Зато теперь стало очень красиво – все-таки это не свалка.',
       'views_count': 187, 'likes_count': 67, 'pk': 3},
      {'poster_name': 'larry', 'poster_avatar': 'https://randus.org/avatars/m/81898dbdbdffdb18.png',
       'pic': 'https://images.unsplash.com/photo-1581235854265-41981cb85c88?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=880&q=80',
       'content': 'Утром проснулся раньше всех – вижу у бассейна на вешалке висит оранжевое пальто. О, думаю – как это мое пальто за мной забралось так далеко – за целых 5000 километров. Присмотрелся – а это зонтик. И как только успел его сюда притащить! За завтраком сижу напротив своего попутчика, и все не решаюсь спросить его: «Может быть, мы все-таки не попутчики? Может, нам надо разъехаться в разные стороны? Вы не боитесь, что я сейчас сбегу?». Он не боится. Он вообще ничего не боится, кроме одного – когда у него в машине не работает сигнализация. А если она не работает, то он садится в машину и продолжает идти своим путем.',
       'views_count': 366, 'likes_count': 198, 'pk': 4},
      {'poster_name': 'leo', 'poster_avatar': 'https://randus.org/avatars/w/c1819dbdffffff18.png',
       'pic': 'https://images.unsplash.com/photo-1570427968906-5a309bfd7de3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=880&q=80',
       'content': 'Пурр-пурр! типичная инстарамная фотка с котом , книжкой и едой. Но не буду скрывать, что это я: а то вдруг у вас кот тоже такой, тогда вы не увидите этого в своих фото. #кот #котики #инста #инстаграм #любовькживотным #любимыйкот ... Как же я люблю этот момент, когда ты понимаешь, что ты ничего толком не умеешь делать и даже не знаешь, что с этим делать.',
       'views_count': 287, 'likes_count': 99, 'pk': 5},
      {'poster_name': 'johnny', 'poster_avatar': 'https://randus.org/avatars/m/00183c7e3c382499.png',
       'pic': 'https://images.unsplash.com/photo-1482112252853-a77ee8d9a8cc?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=867&q=80',
       'content': 'Вот обычная лампочка, которая может стать для тебя новым смыслом жизни.', 'views_count': 299,
       'likes_count': 134, 'pk': 6},
      {'poster_name': 'hank', 'poster_avatar': 'https://randus.org/avatars/m/383c7e7e3c3c1818.png',
       'pic': 'https://images.unsplash.com/photo-1494548162494-384bba4ab999?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=880&q=80',
       'content': 'Очень красивый закат. Стоило выбраться из дома, чтобы посмотреть на него! а где ты был?',
       'views_count': 166, 'likes_count': 76, 'pk': 7},
      {'poster_name': 'larry', 'poster_avatar': 'https://randus.org/avatars/m/81898dbdbdffdb18.png',
       'pic': 'https://images.unsplash.com/photo-1494952200529-3ceb822a75e2?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=880&q=80',
       'content': 'Утром отправились на катере обследовать ближайшие острова – острова в основном каменные, бесполезные и необитаемые. На обратном пути попали в бурю, и нас чуть не унесло в океан. В течение 10 минут наш катер несся к отмели, а потом мы стали дрейфовать между скал, держась за трос. Наконец погода наладилась и мы смогли совершить обратный путь. Когда уже прибыли домой, я попросил, чтобы на следующий день нам устроили на катере экскурсию по морю. Нас провели по морскому дну от одного острова к другому, показали различные интересные объекты, которые встречаются в этом районе.',
       'views_count': 141, 'likes_count': 45, 'pk': 8}], 'poster_name', {'hank', 'leo', 'larry', 'johnny'}),
    ([{'poster_name': 'leo', 'poster_avatar': 'https://randus.org/avatars/w/c1819dbdffffff18.png',
       'pic': 'https://images.unsplash.com/photo-1525351326368-efbb5cb6814d?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80',
       'content': 'Ага, опять еда! Квадратная тарелка в квадратном кадре. А на тарелке, наверное, пирог! Мне было так жаль, что я не могу ее съесть. Я боялась, что они заметят, и если я не съем это, то, значит, они все подумают, что я плохая девочка... Но потом мне вспомнилось, как они на меня смотрели. Когда я была маленькой, на кухне всегда были родители, бабушка, дедушка, дядя Борис... Все вместе. И всегда одна я, потому что все остальные приходили туда лишь изредка. Мне казалось, если бы все ходили на работу, как и я, в этот свой офис, было бы совсем неинтересно.',
       'views_count': 376, 'likes_count': 154, 'pk': 1},
      {'poster_name': 'johnny', 'poster_avatar': 'https://randus.org/avatars/m/00183c7e3c382499.png',
       'pic': 'https://images.unsplash.com/photo-1592660716763-09efba6db4e3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80',
       'content': 'Вышел погулять днем, пока все на работе. На улице странные штуки, похожие на колонны, которые кто-то сгрыз – незаметно и аккуратно, так, что даже мусора не осталось. И еще много странного: например, почему-то все птицы летают, как птицы, и, похоже, им это совершенно не мешает. Или вот еще: в траве – как будто следы от чьих-то ног, хотя вроде бы я ходил довольно тихо... На следующий день было совсем пусто. Я вышел и почувствовал себя очень одиноко. Пошел к остановке. Вокруг было много народу – и все одинаковые. Как будто все они приехали сюда из одного дома и вышли на этом перекрестке после работы, чтобы не возвращаться в свои квартиры.',
       'views_count': 233, 'likes_count': 101, 'pk': 2},
      {'poster_name': 'hank', 'poster_avatar': 'https://randus.org/avatars/m/383c7e7e3c3c1818.png',
       'pic': 'https://images.unsplash.com/photo-1612450632008-22c2a5437dc1?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80',
       'content': 'Смотрите-ка – ржавые елки! Раньше на этом месте была свалка старых машин, а потом все засыпали песком. Теперь тут ничего не растет – только ржавые елки , кусты и грязь. Да и не может тут ничего расти: слишком много пыли и песка. Зато теперь стало очень красиво – все-таки это не свалка.',
       'views_count': 187, 'likes_count': 67, 'pk': 3},
      {'poster_name': 'larry', 'poster_avatar': 'https://randus.org/avatars/m/81898dbdbdffdb18.png',
       'pic': 'https://images.unsplash.com/photo-1581235854265-41981cb85c88?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=880&q=80',
       'content': 'Утром проснулся раньше всех – вижу у бассейна на вешалке висит оранжевое пальто. О, думаю – как это мое пальто за мной забралось так далеко – за целых 5000 километров. Присмотрелся – а это зонтик. И как только успел его сюда притащить! За завтраком сижу напротив своего попутчика, и все не решаюсь спросить его: «Может быть, мы все-таки не попутчики? Может, нам надо разъехаться в разные стороны? Вы не боитесь, что я сейчас сбегу?». Он не боится. Он вообще ничего не боится, кроме одного – когда у него в машине не работает сигнализация. А если она не работает, то он садится в машину и продолжает идти своим путем.',
       'views_count': 366, 'likes_count': 198, 'pk': 4},
      {'poster_name': 'leo', 'poster_avatar': 'https://randus.org/avatars/w/c1819dbdffffff18.png',
       'pic': 'https://images.unsplash.com/photo-1570427968906-5a309bfd7de3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=880&q=80',
       'content': 'Пурр-пурр! типичная инстарамная фотка с котом , книжкой и едой. Но не буду скрывать, что это я: а то вдруг у вас кот тоже такой, тогда вы не увидите этого в своих фото. #кот #котики #инста #инстаграм #любовькживотным #любимыйкот ... Как же я люблю этот момент, когда ты понимаешь, что ты ничего толком не умеешь делать и даже не знаешь, что с этим делать.',
       'views_count': 287, 'likes_count': 99, 'pk': 5},
      {'poster_name': 'johnny', 'poster_avatar': 'https://randus.org/avatars/m/00183c7e3c382499.png',
       'pic': 'https://images.unsplash.com/photo-1482112252853-a77ee8d9a8cc?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=867&q=80',
       'content': 'Вот обычная лампочка, которая может стать для тебя новым смыслом жизни.', 'views_count': 299,
       'likes_count': 134, 'pk': 6},
      {'poster_name': 'hank', 'poster_avatar': 'https://randus.org/avatars/m/383c7e7e3c3c1818.png',
       'pic': 'https://images.unsplash.com/photo-1494548162494-384bba4ab999?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=880&q=80',
       'content': 'Очень красивый закат. Стоило выбраться из дома, чтобы посмотреть на него! а где ты был?',
       'views_count': 166, 'likes_count': 76, 'pk': 7},
      {'poster_name': 'larry', 'poster_avatar': 'https://randus.org/avatars/m/81898dbdbdffdb18.png',
       'pic': 'https://images.unsplash.com/photo-1494952200529-3ceb822a75e2?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=880&q=80',
       'content': 'Утром отправились на катере обследовать ближайшие острова – острова в основном каменные, бесполезные и необитаемые. На обратном пути попали в бурю, и нас чуть не унесло в океан. В течение 10 минут наш катер несся к отмели, а потом мы стали дрейфовать между скал, держась за трос. Наконец погода наладилась и мы смогли совершить обратный путь. Когда уже прибыли домой, я попросил, чтобы на следующий день нам устроили на катере экскурсию по морю. Нас провели по морскому дну от одного острова к другому, показали различные интересные объекты, которые встречаются в этом районе.',
       'views_count': 141, 'likes_count': 45, 'pk': 8}], 'pk', {1, 2, 3, 4, 5, 6, 7, 8}),
]


@pytest.mark.parametrize("posts, key, unique", values_parameters)
def test_unique_values(posts, key, unique):
    assert unique_values(posts, key) == unique


values_exceptions = [
    ([{'poster_name': 'leo', 'poster_avatar': 'https://randus.org/avatars/w/c1819dbdffffff18.png',
       'pic': 'https://images.unsplash.com/photo-1525351326368-efbb5cb6814d?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80',
       'content': 'Ага, опять еда! Квадратная тарелка в квадратном кадре. А на тарелке, наверное, пирог! Мне было так жаль, что я не могу ее съесть. Я боялась, что они заметят, и если я не съем это, то, значит, они все подумают, что я плохая девочка... Но потом мне вспомнилось, как они на меня смотрели. Когда я была маленькой, на кухне всегда были родители, бабушка, дедушка, дядя Борис... Все вместе. И всегда одна я, потому что все остальные приходили туда лишь изредка. Мне казалось, если бы все ходили на работу, как и я, в этот свой офис, было бы совсем неинтересно.',
       'views_count': 376, 'likes_count': 154, 'pk': 1},
      {'poster_name': 'johnny', 'poster_avatar': 'https://randus.org/avatars/m/00183c7e3c382499.png',
       'pic': 'https://images.unsplash.com/photo-1592660716763-09efba6db4e3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80',
       'content': 'Вышел погулять днем, пока все на работе. На улице странные штуки, похожие на колонны, которые кто-то сгрыз – незаметно и аккуратно, так, что даже мусора не осталось. И еще много странного: например, почему-то все птицы летают, как птицы, и, похоже, им это совершенно не мешает. Или вот еще: в траве – как будто следы от чьих-то ног, хотя вроде бы я ходил довольно тихо... На следующий день было совсем пусто. Я вышел и почувствовал себя очень одиноко. Пошел к остановке. Вокруг было много народу – и все одинаковые. Как будто все они приехали сюда из одного дома и вышли на этом перекрестке после работы, чтобы не возвращаться в свои квартиры.',
       'views_count': 233, 'likes_count': 101, 'pk': 2},
      {'poster_name': 'hank', 'poster_avatar': 'https://randus.org/avatars/m/383c7e7e3c3c1818.png',
       'pic': 'https://images.unsplash.com/photo-1612450632008-22c2a5437dc1?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80',
       'content': 'Смотрите-ка – ржавые елки! Раньше на этом месте была свалка старых машин, а потом все засыпали песком. Теперь тут ничего не растет – только ржавые елки , кусты и грязь. Да и не может тут ничего расти: слишком много пыли и песка. Зато теперь стало очень красиво – все-таки это не свалка.',
       'views_count': 187, 'likes_count': 67, 'pk': 3},
      {'poster_name': 'larry', 'poster_avatar': 'https://randus.org/avatars/m/81898dbdbdffdb18.png',
       'pic': 'https://images.unsplash.com/photo-1581235854265-41981cb85c88?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=880&q=80',
       'content': 'Утром проснулся раньше всех – вижу у бассейна на вешалке висит оранжевое пальто. О, думаю – как это мое пальто за мной забралось так далеко – за целых 5000 километров. Присмотрелся – а это зонтик. И как только успел его сюда притащить! За завтраком сижу напротив своего попутчика, и все не решаюсь спросить его: «Может быть, мы все-таки не попутчики? Может, нам надо разъехаться в разные стороны? Вы не боитесь, что я сейчас сбегу?». Он не боится. Он вообще ничего не боится, кроме одного – когда у него в машине не работает сигнализация. А если она не работает, то он садится в машину и продолжает идти своим путем.',
       'views_count': 366, 'likes_count': 198, 'pk': 4},
      {'poster_name': 'leo', 'poster_avatar': 'https://randus.org/avatars/w/c1819dbdffffff18.png',
       'pic': 'https://images.unsplash.com/photo-1570427968906-5a309bfd7de3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=880&q=80',
       'content': 'Пурр-пурр! типичная инстарамная фотка с котом , книжкой и едой. Но не буду скрывать, что это я: а то вдруг у вас кот тоже такой, тогда вы не увидите этого в своих фото. #кот #котики #инста #инстаграм #любовькживотным #любимыйкот ... Как же я люблю этот момент, когда ты понимаешь, что ты ничего толком не умеешь делать и даже не знаешь, что с этим делать.',
       'views_count': 287, 'likes_count': 99, 'pk': 5},
      {'poster_name': 'johnny', 'poster_avatar': 'https://randus.org/avatars/m/00183c7e3c382499.png',
       'pic': 'https://images.unsplash.com/photo-1482112252853-a77ee8d9a8cc?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=867&q=80',
       'content': 'Вот обычная лампочка, которая может стать для тебя новым смыслом жизни.', 'views_count': 299,
       'likes_count': 134, 'pk': 6},
      {'poster_name': 'hank', 'poster_avatar': 'https://randus.org/avatars/m/383c7e7e3c3c1818.png',
       'pic': 'https://images.unsplash.com/photo-1494548162494-384bba4ab999?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=880&q=80',
       'content': 'Очень красивый закат. Стоило выбраться из дома, чтобы посмотреть на него! а где ты был?',
       'views_count': 166, 'likes_count': 76, 'pk': 7},
      {'poster_name': 'larry', 'poster_avatar': 'https://randus.org/avatars/m/81898dbdbdffdb18.png',
       'pic': 'https://images.unsplash.com/photo-1494952200529-3ceb822a75e2?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=880&q=80',
       'content': 'Утром отправились на катере обследовать ближайшие острова – острова в основном каменные, бесполезные и необитаемые. На обратном пути попали в бурю, и нас чуть не унесло в океан. В течение 10 минут наш катер несся к отмели, а потом мы стали дрейфовать между скал, держась за трос. Наконец погода наладилась и мы смогли совершить обратный путь. Когда уже прибыли домой, я попросил, чтобы на следующий день нам устроили на катере экскурсию по морю. Нас провели по морскому дну от одного острова к другому, показали различные интересные объекты, которые встречаются в этом районе.',
       'views_count': 141, 'likes_count': 45, 'pk': 8}], 'text', KeyError),
    ([1, 2, 3, 3, 4, 9], 'pk', TypeError),
]


@pytest.mark.parametrize("values, key, exception", values_exceptions)
def test_unique_values(values, key, exception):
    with pytest.raises(exception):
        unique_values(values, key)


posts_wish_tag_parameters = [
    ([{'content': 'Привет я тут делаю #тест функции на pyton', 'teg_words': ['тест']},
      {'content': 'Привет я тут делаю тест функции на #pyton', 'teg_words': ['pyton']},
      {'content': 'Привет я тут делаю #тест #функции на #pyton', 'teg_words': ['тест', 'функции', 'pyton']}], 'pyton',
     [{'content': 'Привет я тут делаю тест функции на #pyton', 'teg_words': ['pyton']},
      {'content': 'Привет я тут делаю #тест #функции на #pyton', 'teg_words': ['тест', 'функции', 'pyton']}]),
    ([{'content': 'Привет я тут делаю #тестики функции на pyton', 'teg_words': ['тестики']},
      {'content': 'Привет я тут делаю тест функции на #pyton', 'teg_words': ['pyton']},
      {'content': 'Привет я тут делаю #тест #функции на #pyton', 'teg_words': ['тест', 'функции', 'pyton']}], 'тест',
     [{'content': 'Привет я тут делаю #тест #функции на #pyton', 'teg_words': ['тест', 'функции', 'pyton']}]),
    ([{'content': 'Привет я тут делаю #тестики функции на pyton', 'teg_words': ['тестики']},
      {'content': 'Привет я тут делаю тест функции на #pyton', 'teg_words': ['pyton']},
      {'content': 'Привет я тут делаю #тест #функции на #pyton', 'teg_words': ['тест', 'функции', 'pyton']}], 'лапки',
     []),

]


@pytest.mark.parametrize("posts, tag, posts_with_tag", posts_wish_tag_parameters)
def test_search_posts_for_tag(posts, tag, posts_with_tag):
    assert search_posts_for_tag(posts, tag) == posts_with_tag


class TestPosts:

    def test_get_posts_all(self):
        posts = Posts('data/posts.json')
        assert posts.get_posts_all() == [
            {'poster_name': 'leo', 'poster_avatar': 'https://randus.org/avatars/w/c1819dbdffffff18.png',
             'pic': 'https://images.unsplash.com/photo-1525351326368-efbb5cb6814d?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80',
             'content': 'Ага, опять еда! Квадратная тарелка в квадратном кадре. А на тарелке, наверное, пирог! Мне было так жаль, что я не могу ее съесть. Я боялась, что они заметят, и если я не съем это, то, значит, они все подумают, что я плохая девочка... Но потом мне вспомнилось, как они на меня смотрели. Когда я была маленькой, на кухне всегда были родители, бабушка, дедушка, дядя Борис... Все вместе. И всегда одна я, потому что все остальные приходили туда лишь изредка. Мне казалось, если бы все ходили на работу, как и я, в этот свой офис, было бы совсем неинтересно.',
             'views_count': 376, 'likes_count': 154, 'pk': 1},
            {'poster_name': 'johnny', 'poster_avatar': 'https://randus.org/avatars/m/00183c7e3c382499.png',
             'pic': 'https://images.unsplash.com/photo-1592660716763-09efba6db4e3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80',
             'content': 'Вышел погулять днем, пока все на работе. На улице странные штуки, похожие на колонны, которые кто-то сгрыз – незаметно и аккуратно, так, что даже мусора не осталось. И еще много странного: например, почему-то все птицы летают, как птицы, и, похоже, им это совершенно не мешает. Или вот еще: в траве – как будто следы от чьих-то ног, хотя вроде бы я ходил довольно тихо... На следующий день было совсем пусто. Я вышел и почувствовал себя очень одиноко. Пошел к остановке. Вокруг было много народу – и все одинаковые. Как будто все они приехали сюда из одного дома и вышли на этом перекрестке после работы, чтобы не возвращаться в свои квартиры.',
             'views_count': 233, 'likes_count': 101, 'pk': 2}]

    def test_get_posts_by_user(self):
        posts = Posts('data/posts.json')
        assert posts.get_posts_by_user('leo') == [
            {'poster_name': 'leo', 'poster_avatar': 'https://randus.org/avatars/w/c1819dbdffffff18.png',
             'pic': 'https://images.unsplash.com/photo-1525351326368-efbb5cb6814d?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80',
             'content': 'Ага, опять еда! Квадратная тарелка в квадратном кадре. А на тарелке, наверное, пирог! Мне было так жаль, что я не могу ее съесть. Я боялась, что они заметят, и если я не съем это, то, значит, они все подумают, что я плохая девочка... Но потом мне вспомнилось, как они на меня смотрели. Когда я была маленькой, на кухне всегда были родители, бабушка, дедушка, дядя Борис... Все вместе. И всегда одна я, потому что все остальные приходили туда лишь изредка. Мне казалось, если бы все ходили на работу, как и я, в этот свой офис, было бы совсем неинтересно.',
             'views_count': 376, 'likes_count': 154, 'pk': 1}]

    def test_get_posts_by_user_error(self):
        posts = Posts('data/posts.json')
        with pytest.raises(ValueError):
            posts.get_posts_by_user('lea')

    def test_search_for_posts_1(self):
        posts = Posts('data/posts.json')
        assert posts.search_for_posts('погулять') == [{
            "poster_name": "johnny",
            "poster_avatar": "https://randus.org/avatars/m/00183c7e3c382499.png",
            "pic": "https://images.unsplash.com/photo-1592660716763-09efba6db4e3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80",
            "content": "Вышел погулять днем, пока все на работе. На улице странные штуки, похожие на колонны, которые кто-то сгрыз – незаметно и аккуратно, так, что даже мусора не осталось. И еще много странного: например, почему-то все птицы летают, как птицы, и, похоже, им это совершенно не мешает. Или вот еще: в траве – как будто следы от чьих-то ног, хотя вроде бы я ходил довольно тихо... На следующий день было совсем пусто. Я вышел и почувствовал себя очень одиноко. Пошел к остановке. Вокруг было много народу – и все одинаковые. Как будто все они приехали сюда из одного дома и вышли на этом перекрестке после работы, чтобы не возвращаться в свои квартиры.",
            "views_count": 233,
            "likes_count": 101,
            "pk": 2
        }]

    def test_search_for_posts_2(self):
        posts = Posts('data/posts.json')
        assert posts.search_for_posts('зяблик') == []

    def test_search_for_posts_3(self):
        posts = Posts('data/posts.json')
        assert posts.search_for_posts('а') == [{
            "poster_name": "leo",
            "poster_avatar": "https://randus.org/avatars/w/c1819dbdffffff18.png",
            "pic": "https://images.unsplash.com/photo-1525351326368-efbb5cb6814d?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80",
            "content": "Ага, опять еда! Квадратная тарелка в квадратном кадре. А на тарелке, наверное, пирог! Мне было так жаль, что я не могу ее съесть. Я боялась, что они заметят, и если я не съем это, то, значит, они все подумают, что я плохая девочка... Но потом мне вспомнилось, как они на меня смотрели. Когда я была маленькой, на кухне всегда были родители, бабушка, дедушка, дядя Борис... Все вместе. И всегда одна я, потому что все остальные приходили туда лишь изредка. Мне казалось, если бы все ходили на работу, как и я, в этот свой офис, было бы совсем неинтересно.",
            "views_count": 376,
            "likes_count": 154,
            "pk": 1
        },
            {
                "poster_name": "johnny",
                "poster_avatar": "https://randus.org/avatars/m/00183c7e3c382499.png",
                "pic": "https://images.unsplash.com/photo-1592660716763-09efba6db4e3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80",
                "content": "Вышел погулять днем, пока все на работе. На улице странные штуки, похожие на колонны, которые кто-то сгрыз – незаметно и аккуратно, так, что даже мусора не осталось. И еще много странного: например, почему-то все птицы летают, как птицы, и, похоже, им это совершенно не мешает. Или вот еще: в траве – как будто следы от чьих-то ног, хотя вроде бы я ходил довольно тихо... На следующий день было совсем пусто. Я вышел и почувствовал себя очень одиноко. Пошел к остановке. Вокруг было много народу – и все одинаковые. Как будто все они приехали сюда из одного дома и вышли на этом перекрестке после работы, чтобы не возвращаться в свои квартиры.",
                "views_count": 233,
                "likes_count": 101,
                "pk": 2
            }]

    def test_get_post_by_pk_1(self):
        posts = Posts('data/posts.json')
        assert posts.get_post_by_pk(1) == {
            "poster_name": "leo",
            "poster_avatar": "https://randus.org/avatars/w/c1819dbdffffff18.png",
            "pic": "https://images.unsplash.com/photo-1525351326368-efbb5cb6814d?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80",
            "content": "Ага, опять еда! Квадратная тарелка в квадратном кадре. А на тарелке, наверное, пирог! Мне было так жаль, что я не могу ее съесть. Я боялась, что они заметят, и если я не съем это, то, значит, они все подумают, что я плохая девочка... Но потом мне вспомнилось, как они на меня смотрели. Когда я была маленькой, на кухне всегда были родители, бабушка, дедушка, дядя Борис... Все вместе. И всегда одна я, потому что все остальные приходили туда лишь изредка. Мне казалось, если бы все ходили на работу, как и я, в этот свой офис, было бы совсем неинтересно.",
            "views_count": 376,
            "likes_count": 154,
            "pk": 1
        }

    def test_get_post_by_pk_2(self):
        posts = Posts('data/posts.json')
        assert posts.get_post_by_pk(3) == None


class TestComments:

    def test_get_comments_all(self):
        comments = Comments('data/comments.json')
        assert comments.get_comments_all() == [{
            "post_id": 1,
            "commenter_name": "hanna",
            "comment": "Очень здорово!",
            "pk": 1
        },
            {
                "post_id": 1,
                "commenter_name": "jlia",
                "comment": ":)",
                "pk": 2
            },
            {
                "post_id": 2,
                "commenter_name": "leo",
                "comment": "Часть вижу такие фото у друзей! Это новый тренд?",
                "pk": 8
            },
            {
                "post_id": 3,
                "commenter_name": "johnny",
                "comment": "Выглядит неплохо )",
                "pk": 9
            }]

    def test_get_comments_by_post_id_1(self):
        comments = Comments('data/comments.json')
        assert comments.get_comments_by_post_id(1, {1, 2, 3}) == [{
            "post_id": 1,
            "commenter_name": "hanna",
            "comment": "Очень здорово!",
            "pk": 1
        },
            {
                "post_id": 1,
                "commenter_name": "jlia",
                "comment": ":)",
                "pk": 2
            }]

    def test_get_comments_by_post_id_2(self):
        comments = Comments('data/comments.json')
        assert comments.get_comments_by_post_id(3, {1, 2, 3}) == [{
            "post_id": 3,
            "commenter_name": "johnny",
            "comment": "Выглядит неплохо )",
            "pk": 9
        }]

    def test_get_comments_by_post_id_error(self):
        comments = Comments('data/comments.json')
        with pytest.raises(ValueError):
            assert comments.get_comments_by_post_id(4, {1, 2, 3})
