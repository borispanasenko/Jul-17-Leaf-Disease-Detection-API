from sqlalchemy import Integer, Float, String, Text, ForeignKey, DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from datetime import datetime


class Base(DeclarativeBase):
    pass


class Plant(Base):
    __tablename__ = 'plant'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    type: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)


class Disease(Base):
    __tablename__ = 'disease'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(Text)
    treatment: Mapped[str] = mapped_column(Text)


class Detection(Base):
    __tablename__ = 'detection'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    image_path: Mapped[str] = mapped_column(String(200))
    disease_id: Mapped[int] = mapped_column(Integer, ForeignKey('disease.id'), index=True, nullable=True)
    disease: Mapped['Disease'] = relationship('Disease', backref='detections')
    confidence: Mapped[float] = mapped_column(Float)
    timestamp: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), index=True)
    plant_id: Mapped[int] = mapped_column(Integer, ForeignKey('plant.id'), index=True, nullable=True)
    plant: Mapped['Plant'] = relationship('Plant', backref='detections')
