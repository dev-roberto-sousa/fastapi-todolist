from dataclasses import asdict

from sqlalchemy import select

from fast_todo.models import User


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        new_user = User(username='juba', password='secret', email='teste@test')
        session.add(new_user)
        session.commit()

    user = session.scalar(select(User).where(User.username == 'juba'))

    assert asdict(user) == {
        'id': 1,
        'username': 'juba',
        'password': 'secret',
        'email': 'teste@test',
        'created_at': time,
    }
