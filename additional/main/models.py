from sqlalchemy import Column, String, Text, ForeignKey
from sqlalchemy.orm import relationship

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
        String(24),
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
    ) -> bool:
    
    obj = model(**kwargs)

    try:
        session.add(obj)
        session.commit()
        session.refresh(obj)
    except Exception:
        return False

    return True