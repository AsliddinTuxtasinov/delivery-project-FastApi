# from sqlalchemy.dialects.postgresql import UUID  # Change to the appropriate database dialect

from sqlalchemy import Column, Integer, Boolean, Text, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType, EmailType

from db.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, unique=True)
    username = Column(String(50), unique=True)
    email = Column(String(100), unique=True)
    password = Column(String, nullable=True)  # Changed to String for password
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)

    # Establish the one-to-many relationship with "Order" model
    orders = relationship("Order", back_populates="user")  # Changed "users" to "user" here

    def __repr__(self):
        return f"user: {self.username}"


class Order(Base):
    ORDER_STATUSES = (
        ("PENDING", "pending"),
        ("IN_TRANSIT", "in_transit"),
        ("DELIVERED", "delivered"),
        ("CANCEL", "cancel")
    )

    __tablename__ = "order"

    id = Column(Integer, primary_key=True, unique=True)
    quantity = Column(Integer)
    order_statuses = Column(ChoiceType(choices=ORDER_STATUSES), default="PENDING")

    user_id = Column(Integer, ForeignKey("user.id"))  # Establish the foreign key relationship
    # Establish the many-to-one relationship with "User" model
    user = relationship("User", back_populates="orders")  # Use "user" here

    product_id = Column(Integer, ForeignKey("product.id"))
    product = relationship("Product", back_populates="products")

    def __repr__(self):
        return f"order id: {self.id}"


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    price = Column(Integer)

    # product = relationship("Order", back_populates="orders")

    def __repr__(self):
        return f"product: {self.name}"
