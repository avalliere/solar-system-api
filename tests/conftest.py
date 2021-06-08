import pytest
from app import create_app
from app import db
from app.models.planet import Planet

@pytest.fixture
def app():
    app = create_app({'Testing': True})
    
    with app.app_context():
        db.create_all()
        yield app
   
    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def two_saved_planets(app):
    # Arrange
    first_planet = Planet(
        name='Mercury',
        description = 'It is the first planet in our solar system', 
        fun_fact='It is not that hot')
    second_planet = Planet(
        name = 'Venus',
        description = 'It is the second planet in our solar system',
        fun_fact = 'It is hotter than Mercury')
    
    db.session.add_all([first_planet, second_planet])
    db.session.commit()