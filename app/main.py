import os.path
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from werkzeug.utils import secure_filename
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy import select
import aiofiles
from config import Config
from app.models import Base, Disease, Detection
from app.ml_model import predict

app = FastAPI()

app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"])

engine = create_async_engine(Config.SQLALCHEMY_DATABASE_URI.replace('sqlite', 'sqlite+aiosqlite'), echo=True)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.on_event('startup')
async def startup():
    await create_tables()


@app.post('/analyze')
async def analyze(image: UploadFile = File(...)):
    if '.' not in image.filename or image.filename.rsplit('.', 1)[1].lower() not in {'jpg', 'jpeg', 'png'}:
        raise HTTPException(status_code=400, detail='Invalid file')

    try:
        filename = secure_filename(image.filename)
        path = os.path.join(Config.UPLOAD_FOLDER, filename)

        async with aiofiles.open(path, 'wb') as f:
            content = await image.read()
            await f.write(content)

        disease_name, confidence = predict(path)

        async with async_session() as session:
            async with session.begin():
                disease = (await session.execute(
                    select(Disease).filter_by(name=disease_name)
                )).scalars().first()

                if not disease:
                    raise HTTPException(status_code=404, detail='Disease not found')

                detection = Detection(
                    image_path=path, disease_id=disease.id, confidence=confidence
                )
                session.add(detection)
                await session.commit()

                return {'disease': disease_name,
                        'disease_id': disease.id, 'confidence': confidence,
                        'description': disease.description, 'treatment': disease.treatment,
                        'detection_id': detection.id}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Server error: {e}')


@app.get('/detections')
async def get_detections():
    async with async_session() as session:
        detections = (await session.execute(select(Detection))).scalars().all()
        return [{'id': d.id, 'disease_id': d.disease_id, 'confidence': d.confidence,
                 'timestamp': d.timestamp} for d in detections]


@app.get('/diseases/{disease_id}')
async def get_diseases(disease_id: int):
    async with async_session() as session:
        disease = (await session.execute(select(Disease).filter_by(id=disease_id))).scalars().first()
        if disease:
            return {'name': disease.name, 'description': disease.description,
                    'treatment': disease.treatment}
        raise HTTPException(status_code=404, detail='Disease not found')
