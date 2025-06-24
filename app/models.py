from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(20), nullable=False)
    tipo = Column(String(20), nullable=False)  # Ej: "Mayores", "Menores"

    torneos = relationship("Tournament", back_populates="categoria")


class Tournament(Base):
    __tablename__ = "tournaments"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    anio = Column(Integer)
    categoria_id = Column(Integer, ForeignKey("categories.id"))

    categoria = relationship("Category", back_populates="torneos")
    fases = relationship("Phase", back_populates="torneo")


class Phase(Base):
    __tablename__ = "phases"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50))  # "Apertura", "Clausura", "Anual"
    inicio = Column(Date)
    fin = Column(Date)
    torneo_id = Column(Integer, ForeignKey("tournaments.id"))

    torneo = relationship("Tournament", back_populates="fases")
    zonas = relationship("Zone", back_populates="fase")


class Zone(Base):
    __tablename__ = "zones"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(10))  # A1, B2, etc.
    fase_id = Column(Integer, ForeignKey("phases.id"))

    fase = relationship("Phase", back_populates="zonas")
    equipos = relationship("ZoneTeam", back_populates="zona")
    partidos = relationship("Match", back_populates="zona")


class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)

    jugadores = relationship("Player", back_populates="equipo")
    zone_teams = relationship("ZoneTeam", back_populates="equipo")


class ZoneTeam(Base):
    __tablename__ = "zone_teams"

    id = Column(Integer, primary_key=True, index=True)
    zona_id = Column(Integer, ForeignKey("zones.id"))
    equipo_id = Column(Integer, ForeignKey("teams.id"))

    zona = relationship("Zone", back_populates="equipos")
    equipo = relationship("Team", back_populates="zone_teams")


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    dorsal = Column(Integer)
    posicion = Column(String(50))
    equipo_id = Column(Integer, ForeignKey("teams.id", ondelete="SET NULL"))

    equipo = relationship("Team", back_populates="jugadores")
    stats = relationship("BasketballStats", back_populates="jugador")


class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True, index=True)
    zona_id = Column(Integer, ForeignKey("zones.id"))
    fecha = Column(Date, default=datetime.utcnow)
    local_team_id = Column(Integer, ForeignKey("teams.id"))
    away_team_id = Column(Integer, ForeignKey("teams.id"))
    resultado = Column(String(20))
    estado = Column(String(20), default="pendiente")

    zona = relationship("Zone", back_populates="partidos")
    local_team = relationship("Team", foreign_keys=[local_team_id])
    away_team = relationship("Team", foreign_keys=[away_team_id])
    stats = relationship("BasketballStats", back_populates="match")


class BasketballStats(Base):
    __tablename__ = "basketball_stats"

    id = Column(Integer, primary_key=True, index=True)
    match_id = Column(Integer, ForeignKey("matches.id", ondelete="CASCADE"))
    jugador_id = Column(Integer, ForeignKey("players.id", ondelete="CASCADE"))
    team_id = Column(Integer, ForeignKey("teams.id"))

    minutos = Column(String(10))
    puntos = Column(Integer, default=0)
    two_pt_attempts = Column(Integer, default=0)
    two_pt_made = Column(Integer, default=0)
    three_pt_attempts = Column(Integer, default=0)
    three_pt_made = Column(Integer, default=0)
    fta = Column(Integer, default=0)
    ftm = Column(Integer, default=0)
    asistencias = Column(Integer, default=0)
    robos = Column(Integer, default=0)
    tapones = Column(Integer, default=0)
    turnovers = Column(Integer, default=0)
    offensive_rebounds = Column(Integer, default=0)
    defensive_rebounds = Column(Integer, default=0)

    jugador = relationship("Player", back_populates="stats")
    match = relationship("Match", back_populates="stats")
    team = relationship("Team")
