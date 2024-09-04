
import datetime
import sqlalchemy.types
import sqlalchemy.schema
import sqlalchemy.orm

meta = sqlalchemy.schema.MetaData()
sqlalchemy.orm.DeclarativeBase

class Model(sqlalchemy.orm.DeclarativeBase):
    ...

class Recipe(Model):
    __tablename__ = "recipe"
    name: sqlalchemy.orm.Mapped[str] = sqlalchemy.orm.mapped_column(primary_key = True)
    date: sqlalchemy.orm.Mapped[datetime.date] = sqlalchemy.orm.mapped_column()
    reviews: sqlalchemy.orm.Mapped[list[int]] = sqlalchemy.orm.relationship(back_populates="recipe", cascade="all")
    ingredients: sqlalchemy.orm.Mapped[list["Ingredient"]] = sqlalchemy.orm.relationship(back_populates="recipe")


class Ingredient(Model):
    __tablename__ = "ingredient"
    id: sqlalchemy.orm.Mapped[int] = sqlalchemy.orm.mapped_column(primary_key=True)

    recipe_name = sqlalchemy.orm.mapped_column(sqlalchemy.schema.ForeignKey("recipe.name"))
    recipe: sqlalchemy.orm.Mapped["Recipe"] = sqlalchemy.orm.relationship(back_populates = "ingredients")

    ingredient_name = sqlalchemy.orm.mapped_column(sqlalchemy.schema.ForeignKey("ingredient_type.name"))
    ingredient_type: sqlalchemy.orm.Mapped["IngredientType"] = sqlalchemy.orm.relationship()

    amount: sqlalchemy.orm.Mapped[int] = sqlalchemy.orm.mapped_column()

class IngredientType(Model):
    __tablename__ = "ingredient_type"
    name: sqlalchemy.orm.Mapped[str] = sqlalchemy.orm.mapped_column(primary_key = True)
    measurement_type_name: sqlalchemy.orm.Mapped[str] = sqlalchemy.orm.mapped_column(sqlalchemy.schema.ForeignKey("measurement_type.name"))

class Review(Model):
    __tablename__ = "review"
    id: sqlalchemy.orm.Mapped[int] = sqlalchemy.orm.mapped_column(primary_key=True)
    recipe_name: sqlalchemy.orm.Mapped[str] = sqlalchemy.orm.mapped_column(sqlalchemy.schema.ForeignKey("recipe.name"))
    description: sqlalchemy.orm.Mapped[str] = sqlalchemy.orm.mapped_column()
    score: sqlalchemy.orm.Mapped[int] = sqlalchemy.orm.mapped_column()

class MeasurementType(Model):
    __tablename__ = "measurement_type"
    name: sqlalchemy.orm.Mapped[str] = sqlalchemy.orm.mapped_column(primary_key = True)

if __name__ == "__main__":
    engine = sqlalchemy.engine.create_engine("sqlite:///db.sqlite")
    con = engine.connect()
    Model.metadata.create_all(con)
