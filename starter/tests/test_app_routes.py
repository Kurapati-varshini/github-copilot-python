import app as app_module


def test_new_game_route_returns_a_9x9_puzzle():
    with app_module.app.test_client() as client:
        response = client.get('/new?clues=35')

    assert response.status_code == 200
    payload = response.get_json()
    assert 'puzzle' in payload

    puzzle = payload['puzzle']
    assert len(puzzle) == 9
    assert all(len(row) == 9 for row in puzzle)
    assert all(cell in range(0, 10) for row in puzzle for cell in row)
    assert any(cell == 0 for row in puzzle for cell in row)


def test_check_route_detects_incorrect_cells():
    with app_module.app.test_client() as client:
        client.get('/new?clues=35')
        solution = [row[:] for row in app_module.CURRENT['solution']]

        if solution[0][0] == 9:
            solution[0][0] = 8
        else:
            solution[0][0] = 9

        response = client.post('/check', json={'board': solution})

    assert response.status_code == 200
    payload = response.get_json()
    assert [0, 0] in payload['incorrect']


def test_check_route_handles_missing_game():
    with app_module.app.test_client() as client:
        app_module.CURRENT['puzzle'] = None
        app_module.CURRENT['solution'] = None

        response = client.post('/check', json={'board': [[0 for _ in range(9)] for _ in range(9)]})

    assert response.status_code == 400
    assert response.get_json()['error'] == 'No game in progress'
