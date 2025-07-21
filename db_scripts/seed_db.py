import asyncio
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy import select
from app.models import Disease
from app.config import Config
from data.diseases_data import diseases_data

engine = create_async_engine(Config.SQLALCHEMY_DATABASE_URI.replace('sqlite', 'sqlite+aiosqlite'))
async_session = async_sessionmaker(engine, expire_on_commit=False)


async def seed():
    data_names = [data['name'] for data in diseases_data]
    missing = set(Config.CLASSES) - set(data_names)
    if missing:
        print(f'Missing data for classes: {missing}')

    async with async_session() as session:
        async with session.begin():
            for data in diseases_data:
                if not await session.execute(select(Disease).filter_by(name=data['name'])).scalars().first():
                    disease = Disease(name=data['name'], description=data['description'], treatment=data['treatment'])
                    session.add(disease)
        await session.commit()
        print('Disease table populated!')

if __name__ == '__main__':
    asyncio.run(seed())
