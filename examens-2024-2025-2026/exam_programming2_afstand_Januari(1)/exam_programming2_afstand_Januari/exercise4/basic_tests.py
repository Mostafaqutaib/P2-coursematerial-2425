import inspect
import pytest
import carshow


def if_class_exists(class_name):
    return pytest.mark.skcarif(class_name not in dir(carshow), reason=f'Skcarped because {class_name} has not been defined')


def is_class_abstract(c):
    return inspect.isabstract(c)


def is_abstract_method(cls, method_name):
    return method_name in cls.__abstractmethods__


def has_property(cls, *, property_name, abstract=False):
    if not hasattr(cls, property_name):
        return False
    prop = getattr(cls, property_name)
    if type(prop) is not property:
        return False
    if prop.__isabstractmethod__ != abstract:
        return False
    return True


def has_method(cls, *, method_name, parameter_names=None, abstract=False, static=False):
    if parameter_names is None:
        parameter_names = []

    if not hasattr(cls, method_name):
        return False
    method = getattr(cls, method_name)
    if not inspect.isfunction(method):
        return False
    if abstract:
        if not is_abstract_method(cls, method_name):
            return False
    is_static = isinstance(inspect.getattr_static(cls, method_name), staticmethod)
    if is_static != static:
        return False
    specs = inspect.getfullargspec(method)
    if specs.args != parameter_names:
        return False
    return True

#######
#
# UTIL
#
#######

def test_util_class_is_defined():
    assert 'Util' in dir(carshow), 'Util class has not been defined'

@if_class_exists('Util')
@pytest.mark.parametrize('kwargs', [
    {
        'method_name': 'is_valid_license_plate',
        'parameter_names': ['license_plate'],
        'abstract': False,
        'static': True,
    },
])
def test_util_methods(kwargs):
    assert has_method(
        carshow.Util,
        **kwargs), f"Util's method {kwargs['method_name']} is missing or incorrect"

#######
#
# CAR
#
#######

def test_car_class_is_defined():
    assert 'Car' in dir(carshow), 'Car class has not been defined'


@if_class_exists('Car')
def test_car_class_is_abstract():
    assert is_class_abstract(carshow.Car)


@if_class_exists('Car')
@pytest.mark.parametrize('kwargs', [
    {
        "property_name": 'license_plate',
        'abstract': False,
    },
])
def test_car_properties(kwargs):
    assert has_property(carshow.Car, **kwargs), f"Car's property {kwargs['property_name']} is missing or incorrect"


@if_class_exists('Car')
@pytest.mark.parametrize('kwargs', [
    {
        'method_name': '__init__',
        'parameter_names': ['self', 'license_plate', 'color', 'amount_wheels'],
        'abstract': False,
    },
    {
        'method_name': 'get_price',
        'parameter_names': ['self'],
        'abstract': True,
    },
])
def test_car_methods(kwargs):
    assert has_method(
        carshow.Car,
        **kwargs), f"Car's method {kwargs['method_name']} is missing or incorrect"

#######
#
# SUPERCAR
#
#######

def test_supercar_class_is_defined():
    assert 'Supercar' in dir(carshow), 'Supercar class has not been defined'


@if_class_exists('Supercar')
def test_supercar_class_is_not_abstract():
    assert not is_class_abstract(carshow.Supercar)


@if_class_exists('Supercar')
@pytest.mark.parametrize('kwargs', [
    {
        'method_name': '__init__',
        'parameter_names': ['self', 'license_plate', 'color', 'top_speed'],
        'abstract': False,
    },
    {
        'method_name': 'get_price',
        'parameter_names': ['self'],
        'abstract': False,
    },

])
def test_supercar_methods(kwargs):
    assert has_method(
        carshow.Supercar,
        **kwargs), f"Supercar's method {kwargs['method_name']} is missing or incorrect"

#######
#
# TRUCK
#
#######

def test_truck_class_is_defined():
    assert 'Truck' in dir(carshow), 'Truck class has not been defined'


@if_class_exists('Truck')
def test_truck_class_is_not_abstract():
    assert not is_class_abstract(carshow.Truck)


@if_class_exists('Truck')
@pytest.mark.parametrize('kwargs', [
    {
        'method_name': '__init__',
        'parameter_names': ['self', 'license_plate', 'color', 'amount_wheels', 'weight_of_load'],
        'abstract': False,
    },
    {
        'method_name': 'get_price',
        'parameter_names': ['self'],
        'abstract': False,
    },

])
def test_truck_methods(kwargs):
    assert has_method(
        carshow.Truck,
        **kwargs), f"Truck's method {kwargs['method_name']} is missing or incorrect"

#######
#
# CARSHOW
#
#######

def test_carshow_class_is_defined():
    assert 'Carshow' in dir(carshow), 'Carshow class has not been defined'


@if_class_exists('Carshow')
@pytest.mark.parametrize('kwargs', [
    {
        "property_name": 'number_of_cars',
        'abstract': False,
    },
    {
        "property_name": 'car_license_plates',
        'abstract': False,
    },
])
def test_carshow_properties(kwargs):
    assert has_property(carshow.Carshow, **kwargs), f"Carshow's property {kwargs['property_name']} is missing or incorrect"


@if_class_exists('Carshow')
@pytest.mark.parametrize('kwargs', [
    {
        'method_name': '__init__',
        'parameter_names': ['self', 'name', 'halls', 'spots'],
        'abstract': False,
    },
    {
        'method_name': 'add_car',
        'parameter_names': ['self', 'car'],
        'abstract': False,
    },
    {
        'method_name': 'remove_car',
        'parameter_names': ['self', 'car'],
        'abstract': False,
    },
    {
        'method_name': 'sort_cars_by_license_plate',
        'parameter_names': ['self'],
        'abstract': False,
    },
    {
        'method_name': 'get_total_price',
        'parameter_names': ['self'],
        'abstract': False,
    },
])
def test_carshow_methods(kwargs):
    assert has_method(
        carshow.Carshow,
        **kwargs), f"Carshow's method {kwargs['method_name']} is missing or incorrect"