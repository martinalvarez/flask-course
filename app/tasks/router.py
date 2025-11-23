from flask import Blueprint, jsonify, request
from .service import TaskService

tasks_bp = Blueprint("tasks", __name__, url_prefix="/tasks")
service = TaskService()

@tasks_bp.get("/")
def get_all_tasks():
    return jsonify(service.get_all())


@tasks_bp.post("/")
def create_task():

    data = request.get_json()
    task = service.create(data)
    return jsonify(task), 201  


@tasks_bp.get("<int:task_id>")
def get_task(task_id):
    task = service.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task)


@tasks_bp.put("<int:task_id>")
def update_task(task_id):
    data = request.get_json()
    task = service.update(task_id, data)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task)
    
@tasks_bp.delete("<int:task_id>")
def delete_task(task_id):
    deleted = service.delete(task_id)
    if not deleted:
        return jsonify({"error": "Task not found"}), 404
    return "", 204