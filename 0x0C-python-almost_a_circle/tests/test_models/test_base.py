#!/usr/bin/python3
"""Defines unittests for base.py.

Unittest classes:
    TestBase_instantiation
    TestBase_to_json_string
    TestBase_save_to_file
    TestBase_from_json_string
    TestBase_create
    TestBase_load_from_file
    TestBase_save_to_file_csv
    TestBase_load_from_file_csv
"""
import os
import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_nb_instances_after_unique_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id_public(self):
        """
        Test the public ID setter method of the Base class.

        This method creates an instance of the Base class with an initial ID of 12.
        It then sets the ID attribute of the instance to 15 and asserts that the value
        of the ID attribute is indeed 15.

        Parameters:
        - self: The instance of the test class.

        Returns:
        - None
        """
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_nb_instances_private(self):
        """
        Test the private attribute __nb_instances raises an AttributeError.

        This function uses the `assertRaises` context manager to check if accessing the private attribute `__nb_instances` of an instance of the `Base` class raises an `AttributeError`. The value `12` is passed as an argument to the `Base` class constructor.

        Parameters:
            self: The instance of the class.

        Returns:
            None.
        """
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)
    def test_float_id(self):
        """
        Test the `id` attribute of the `Base` class when a float is passed as the argument.

        Parameters:
        - self: The instance of the `TestClass` class.

        Returns:
        - None
        """
        self.assertEqual(5.5, Base(5.5).id)

    def test_str_id(self):
        """
        Test the `id` attribute of the Base class with a string input.

        This function creates an instance of the Base class with the string input "hello" and
        asserts that the `id` attribute of the created instance is equal to "hello".

        Parameters:
            self (TestBase): The current instance of the TestBase class.

        Returns:
            None
        """
        self.assertEqual("hello", Base("hello").id)

    def test_complex_id(self):
        """
        Test the complex id of the Base class.

        Asserts that the id of an instance of the Base class initialized with a complex number
        is equal to the id of the complex number itself.

        Parameters:
            self: The instance of the test class.

        Returns:
            None
        """
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_dict_id(self):
        """
        Test the function `id` of the `Base` class.

        This function checks if calling the `id` function of the `Base` class with a dictionary as a parameter returns the expected result.

        Parameters:
            self: The instance of the `Base` class.
        
        Returns:
            None
        
        Raises:
            AssertionError: If the result of the `id` function is not equal to `{"a": 1, "b": 2}`.
        """
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_list_id(self):
        """
        Test the `id` attribute of the `Base` class.
        
        This function creates a new instance of the `Base` class with a list as a parameter.
        It then asserts that the `id` attribute of the instance is equal to the provided list.
        If the assertion fails, an `AssertionError` will be raised.
        """
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_set_id(self):
        """
        Test the set_id method of the Base class.

        This method tests whether the set_id method correctly sets the id attribute of the Base class instance. It does this by creating a Base instance with a set of numbers as the input and asserting that the id attribute of the instance is equal to the input set.

        Parameters:
        - self: The instance of the Base class.

        Return:
        - None
        """
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)
    
    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)


    def test_frozenset_id(self):
        """
        Test the `id` property of the `Base` class when instantiated with a `frozenset` object.

        This test case checks if the `id` property of the `Base` class returns the correct value
        when instantiated with a `frozenset` object. It uses the `assertEqual` method from the
        `unittest.TestCase` class to compare the expected value with the actual value obtained
        from the `id` property.

        Parameters:
            self (TestCase): The test case instance.

        Returns:
            None
        """
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)


class TestBase_to_json_string(unittest.TestCase):
    """Unittests for testing to_json_string method of Base class."""

    def test_to_json_string_rectangle_type(self):
        """
        Test the to_json_string method of the Rectangle class with two dictionaries.

        This function creates two instances of the Rectangle class, r1 and r2, with 
        different dimensions and positions. It then creates a list, list_dicts, 
        containing the dictionaries generated from r1 and r2 using the to_dictionary 
        method. Finally, it asserts that the length of the string returned by the 
        Base class's to_json_string method is equal to 106.

        Parameters:
        - self: The instance of the test class.

        Return:
        - None
        """
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_rectangle_one_dict(self):
        """
        Test the to_json_string method of the Rectangle class with two dictionaries.

        This function creates two instances of the Rectangle class, r1 and r2, with 
        different dimensions and positions. It then creates a list, list_dicts, 
        containing the dictionaries generated from r1 and r2 using the to_dictionary 
        method. Finally, it asserts that the length of the string returned by the 
        Base class's to_json_string method is equal to 106.

        Parameters:
        - self: The instance of the test class.

        Return:
        - None
        """
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)

    def test_to_json_string_rectangle_two_dicts(self):
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def test_to_json_string_square_type(self):
        """
        Generates a function comment for the given function body.

        Parameters:
            None

        Returns:
            None
        """
        s = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_square_one_dict(self):
        """
        Test the 'to_json_string' method when called on a single Square object.
        The method should return a JSON string representation of the Square object's dictionary.
        """
        s = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([s.to_dictionary()])) == 39)


    def test_to_json_string_empty_list(self):
        """Tests empty list"""
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_square_two_dicts(self):
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)

    def test_to_json_string_none(self):
        """
        Test the `to_json_string` method when the input is None.
        The expected behavior is to return "[]".

        Parameters:
            self (TestClass): An instance of the TestClass.
        
        Returns:
            None
        """
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        """
        Test the function `to_json_string()` when called with no arguments.

        :param self: The test case object.
        :return: None.
        """
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        """
        Test case for the `to_json_string` method when there are more than one argument.

        This test ensures that the `to_json_string` method raises a `TypeError` when called with more than one argument.

        Parameters:
            self: An instance of the test class.

        Returns:
            None
        """
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class TestBase_save_to_file(unittest.TestCase):
    """Unittests for testing save_to_file method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_one_rectangle(self):
        """
        Generate a test case to verify the 'save_to_file' method of the Rectangle class.

        Parameters:
            self (TestCase): The current test case.
        
        Returns:
            None
        """
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_two_rectangles(self):
        
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)

    def test_save_to_file_two_squares(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 77)

    def test_save_to_file_one_square(self):
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_cls_name_for_filename(self):
        s = Square(10, 7, 2, 8)
        Base.save_to_file([s])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_overwrite(self):
        s = Square(9, 2, 39, 2)
        Square.save_to_file([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)

    def test_save_to_file_with_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()


class TestBase_from_json_string(unittest.TestCase):
    """Unittests for testing from_json_string method of Base class."""

    def test_from_json_string_type(self):
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_only_one_rectangle(self):
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_rectangles(self):
        list_input = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_one_square(self):
        list_input = [{"id": 89, "size": 10, "height": 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_squares(self):
        list_input = [
            {"id": 89, "size": 10, "height": 4},
            {"id": 7, "size": 1, "height": 7}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_args(self):
        """
        Test the behavior of the `from_json_string` method when called with no arguments.

        This test verifies that the `from_json_string` method raises a `TypeError` when called with no arguments.

        Parameters:
        - self: The instance of the test class.

        Returns:
        - None
        """
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_one_arg(self):
        """
        Test the behavior of the function when more than one argument is passed to `from_json_string`.

        This test case verifies that a `TypeError` is raised when the `from_json_string` function is called
        with more than one argument. The function is expected to raise a `TypeError` since it only accepts
        a single argument.

        Parameters:
            self (TestCase): The test case instance.
        
        Raises:
            TypeError: If more than one argument is passed to `from_json_string`.
        """
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)


class TestBase_create(unittest.TestCase):
    """Unittests for testing create method of the Base class."""

    def test_create_rectangle_original(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r1))

    def test_create_rectangle_new(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r2))

    def test_create_rectangle_is(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_create_rectangle_equals(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_create_square_original(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s1))

    def test_create_new_square(self):
        """
        Test case for the `create_square_new` method.

        This test case checks if the `create_square_new` method correctly creates a new Square object using the `create` method and verifies if the generated object has the expected properties.

        Parameters:
            self: The test case instance.

        Returns:
            None
        """
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s2))

    def test_create_square_is(self):
        """
        Create a square object using the provided dictionary representation.

        Parameters:
            **kwargs (dict): A dictionary representing the attributes of the square object.

        Returns:
            Square: The created square object.

        Raises:
            None

        Examples:
            s1 = Square(3, 5, 1, 7)
            s1_dictionary = s1.to_dictionary()
            s2 = Square.create(**s1_dictionary)
        """
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)

    def test_create_square_equals(self):
        """
        Test if creating a square using the 'create' method and passing a dictionary of square attributes
        produces a square object that is not equal to the original square object.

        Parameters:
        - self: The test case object.

        Returns:
        - None
        """
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)


class TestBase_load_from_file(unittest.TestCase):
    """Unittests for testing load_from_file_method of the Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_from_file_first_rectangle(self):
        """
        Test case for loading a rectangle from a file.
        
        This test case creates two rectangle objects and saves them to a file using the `save_to_file` method of the Rectangle class. It then loads the rectangles from the file using the `load_from_file` method and compares the loaded rectangle with the original rectangle.

        Parameters:
        - self: The test case instance.

        Returns:
        - None
        """
        r1 = Rectangle(7, 2, 8, 1)
        r2 = Rectangle(4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_rectangle_types(self):
        """
        Test function for loading rectangle types from a file.

        param self: The instance of the test case.
        Return: None
        """
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_second_square(self):
        """
        Test the load_from_file method of the Square class for the scenario where the second square in the list is asserted to be equal to the second square in the loaded list of squares.

        Parameters:
            self (TestCase): The current test case.
        
        Returns:
            None
        """
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_square_types(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_no_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_more_than_one_arg(self):
        """
        Test case for the `load_from_file` method when more than one argument is provided.

        Parameters:
            self (object): The current instance of the test case.
        
        Returns:
            None
        """
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


if __name__ == "__main__":
    unittest.main()
