from fastapi import APIRouter, Response
from app.worker import celery

router = APIRouter()


@router.get("/")
async def hello():
    return Response(status_code=200, content='hello')


@router.get("/{id}")
async def get_user_info(id: int):
    # task = celery.send_task('create_task', [int(id)])   
    worker_result = celery.send_task('tasks.AnalysisTask', [int(id)], queue='core', expires=60).get(timeout=60)
    return Response(status_code=200, content=worker_result)
    
