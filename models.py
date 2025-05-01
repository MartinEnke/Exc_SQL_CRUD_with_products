from sqlalchemy import Column, Integer, String, Float
from setup_database import Base


class Products(Base):

    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False, default=0)


