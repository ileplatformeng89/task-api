from fastapi.testclient import TestClient


def create_task(client: TestClient, title: str = "Test task"):
    response = client.post(
        "/tasks",
        json={
            "title": title,
            "description": "Integration test",
            "completed": False,
            "priority": 1,
        },
    )

    assert response.status_code == 200
    return response.json()


def test_create_task(client: TestClient):
    data = create_task(client)

    assert data["title"] == "Test task"
    assert data["completed"] is False
    assert data["priority"] == 1
    assert "id" in data


def test_get_tasks(client: TestClient):
    create_task(client, "Task 1")
    create_task(client, "Task 2")

    response = client.get("/tasks")

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 2


def test_get_task(client: TestClient):
    task = create_task(client)

    response = client.get(f"/tasks/{task['id']}")

    assert response.status_code == 200
    assert response.json()["id"] == task["id"]


def test_get_task_not_found(client: TestClient):
    response = client.get("/tasks/999999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found"}


def test_update_task(client: TestClient):
    task = create_task(client)

    response = client.put(
        f"/tasks/{task['id']}",
        json={
            "title": "Updated task",
            "description": "Updated description",
            "completed": True,
            "priority": 2,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "Updated task"
    assert data["completed"] is True
    assert data["priority"] == 2


def test_patch_task(client: TestClient):
    task = create_task(client)

    response = client.patch(
        f"/tasks/{task['id']}",
        json={
            "completed": True,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == task["title"]
    assert data["completed"] is True


def test_delete_task(client: TestClient):
    task = create_task(client)

    response = client.delete(f"/tasks/{task['id']}")

    assert response.status_code == 200

    response = client.get(f"/tasks/{task['id']}")

    assert response.status_code == 404
