from fastapi import APIRouter, Response
from app.worker import celery

router = APIRouter()


@router.get("/{id}")
async def get_user_info(id: int):
    task = celery.send_task('create_task', [int(id)])
    worker_result = task.get(timeout=30)
    return Response(status_code=200, content=worker_result)
    
