def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_planet_by_id(client, two_saved_planets):
    response = client.get('/planets/1')
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        'id': 1,
        'name': 'Mercury',
        'description': 'It is the first planet in our solar system',
        'fun_fact': 'It is not that hot'
    }

