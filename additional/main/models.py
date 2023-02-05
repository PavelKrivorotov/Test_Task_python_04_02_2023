from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import select

from .db import Base, session


class RocketSQL(Base):
    __tablename__ = "rockets"

    id = Column(
        String(24),
        primary_key=True,
        nullable=False,
    )

    name = Column(
        String(255),
    )

    country = Column(
        String(255),
    )

    company = Column(
        String(255),
    )
    
    type = Column(
        String(255),
    )

    launch = relationship(
        "LaunchSQL",
    )


class LaunchSQL(Base):
    __tablename__ = "launches"

    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
    )

    rocket_id = Column(
        String(24),
        ForeignKey("rockets.id"),
    )

    details = Column(
        Text(),
    )

    mission = relationship("MissionSQL")


class MissionSQL(Base):
    __tablename__ = "missions"

    id = Column(
        String(24),
        primary_key=True,
        nullable=False,
    )

    launc_id = Column(
        String(24),
        ForeignKey("launches.id"),
    )

    name = Column(
        String(255),
    )


def make_insertion(
        model: RocketSQL | LaunchSQL | MissionSQL,
        **kwargs
    ) -> object | None:
    
    obj = model(**kwargs)
    obj_exists = session.execute(
        select(model).where(model.id==obj.id)
    )

    if not obj_exists:
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return obj

    return obj_exists