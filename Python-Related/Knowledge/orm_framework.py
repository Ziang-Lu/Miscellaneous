#!usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Simple ORM framework implementation.

For more information about ORM, check out:
https://github.com/Ziang-Lu/Database-Learning-Notes/blob/master/1-Relational%20Database/3-Python%20DB-API/Python%20DB-API.md
"""

__author__ = 'Ziang Lu'

from abc import ABC


class Column(ABC):
    """
    Abstract Column class representing a column in a table.
    """

    def __init__(self, name: str, data_type: str):
        """
        Constructor with parameter.
        :param name: str
        :param data_type: str
        """
        self._name = name
        self._data_type = data_type

    @property
    def name(self) -> str:
        """
        Accessor of name.
        :return: str
        """
        return self._name

    def __repr__(self):
        return f'<{self.__class__.__name__}:{self._name}({self._data_type})>'


class IntegerColumn(Column):
    """
    IntegerColumn class representing a column with data type "integer".
    """

    def __init__(self, name: str):
        """
        Constructor with parameter.
        :param name: str
        """
        super().__init__(name, 'integer')


class TextColumn(Column):
    """
    TextColumn class representing a column with data type "text".
    """

    def __init__(self, name: str):
        """
        Constructor with parameter.
        :param name: str
        """
        super().__init__(name, 'text')


class ModelMetaclass(type):
    """
    ModelMetaclass used to create classes (models / tables).
    """

    def __new__(cls, name, bases, attrs):
        # Constructor
        # This method is called when a new type (model / table) is created.

        if name == 'Model':  # Creating the base type for all the models / tables (Model)
            # No need to define the columns
            # Continue to call the super constructor
            return type.__new__(cls, name, bases, attrs)

        # Creating a new type (model / table)
        print(f'Creating model / table: {name}')
        # Define the columns
        columns = {}
        for k, v in attrs.items():
            if isinstance(v, Column):
                print(f'Defining column: {k} -> {v}')
                columns[k] = v
        # Remove the class attribute from the class, since the same-name
        # instance attribute will override the corresponding class attribute
        for k in columns:
            attrs.pop(k)
        attrs['__columns__'] = columns
        # Continue to call the super constructor
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    """
    When the base type for all the models / tables "Model" is created, Python
    interpreter will call ModelMetaclass.__new__() to create the base type
    "Model".
    """

    def __init__(self, **kwargs):
        """
        Constructor with parameter.
        :param kwargs: dict
        """
        super().__init__(**kwargs)

    def __getattr__(self, item):
        # This method is defined to make "Model" dict work like a class.
        try:
            return self[item]
        except KeyError:
            raise AttributeError(f"'Model' type has no attribute '{item}'")

    def __setattr__(self, key, value):
        self[key] = value

    def save(self) -> bool:
        """
        Saves an object (writes a record) to the DB.
        :return: bool
        """
        columns = []
        values = []
        for attr_name, column in self.__columns__.items():
            columns.append(column.name)
            values.append(getattr(self, attr_name, None))

        sql = '''
        insert into %s (%s)
        values (%s)
        '''
        print('SQL statement to execute:')
        print(sql)

        # Format values so that it can be passed as arguments to SQL statements
        values = map(lambda x: f"'{str(x)}'", values)
        sql_args = [self.__tablename__, ','.join(columns), ','.join(values)]
        print(f'Arguments to the SQL statement: {sql_args}')

        # ... (Code to execute this SQL statement)
        return True


# Test the ORM framework

class User(Model):
    """
    When the type (model / table) "User" is created, Python interpreter will
    call ModelMetaclass.__new__() to create the type (model / table) "User"
    """
    __tablename__ = 'users'

    id = IntegerColumn(name='id')
    name = TextColumn(name='name')
    email = TextColumn(name='email')
    password = TextColumn(name='password')


user = User(id=12345, name='Michael', email='user@gmail.com', password='abc')
user.save()

# Output:
# Creating model / table: User
# Defining column: id -> <IntegerColumn:id(integer)>
# Defining column: name -> <TextColumn:name(text)>
# Defining column: email -> <TextColumn:email(text)>
# Defining column: password -> <TextColumn:password(text)>
# SQL statement to execute:
#
#         insert into %s (%s)
#         values (%s)
#
# Arguments to the SQL statement: ['users', 'id,name,email,password',
# "'12345','Michael','user@gmail.com','abc'"]
