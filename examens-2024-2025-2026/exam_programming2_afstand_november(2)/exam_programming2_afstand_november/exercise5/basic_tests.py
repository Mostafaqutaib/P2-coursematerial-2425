import inspect
import pytest
import event


def if_class_exists(class_name):
    return pytest.mark.skipif(class_name not in dir(event), reason=f'Skipped because {class_name} has not been defined')


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
    assert 'Util' in dir(event), 'Util class has not been defined'

@if_class_exists('Util')
@pytest.mark.parametrize('kwargs', [
    {
        'method_name': 'is_valid_sabam_id',
        'parameter_names': ['sabam_id'],
        'abstract': False,
        'static': True,
    },
])
def test_util_methods(kwargs):
    assert has_method(
        event.Util,
        **kwargs), f"Util's method {kwargs['method_name']} is missing or incorrect"

#######
#
# ARTIST
#
#######

def test_artist_class_is_defined():
    assert 'Artist' in dir(event), 'Artist class has not been defined'


@if_class_exists('Artist')
@pytest.mark.parametrize('property_name', [
    'sabam_id',
])
def test_artist_properties(property_name):
    assert has_property(
        event.Artist,
        property_name=property_name
        ), f"Artist must have property {property_name}"


@if_class_exists('Artist')
@pytest.mark.parametrize('kwargs', [
    {
        'method_name': '__init__',
        'parameter_names': ['self', 'sabam_id', 'name','wage'],
        'abstract': False,
    },
    {
        'method_name': '__str__',
        'parameter_names': ['self'],
        'abstract': False,
    },
])
def test_artist_methods(kwargs):
    assert has_method(
        event.Artist,
        **kwargs), f"Artist's method {kwargs['method_name']} is missing or incorrect"

#######
#
# EVENT
#
#######

def test_event_class_is_defined():
    assert 'Event' in dir(event), 'Event class has not been defined'


@if_class_exists('Event')
def test_event_class_is_abstract():
    assert is_class_abstract(event.Event)

@if_class_exists('Event')
@pytest.mark.parametrize('kwargs', [
    {
        "property_name": 'number_of_artists',
        'abstract': False,
    },
    {
        "property_name": 'maximum_artists',
        'abstract': False,
    },
    {
        "property_name": 'sum_wages_of_artists',
        'abstract': False,
    },
])
def test_event_properties(kwargs):
    assert has_property(event.Event, **kwargs), f"Event's property {kwargs['property_name']} is missing or incorrect"


@if_class_exists('Event')
@pytest.mark.parametrize('kwargs', [
    {
        'method_name': '__init__',
        'parameter_names': ['self', 'name', 'number_of_stages', 'number_of_slots'],
        'abstract': False,
    },
    {
        'method_name': 'add_artist',
        'parameter_names': ['self','artist'],
        'abstract': False,
    },
    {
        'method_name': 'remove_artist',
        'parameter_names': ['self','artist'],
        'abstract': False,
    },
    {
        'method_name': 'sort_artists_by_name',
        'parameter_names': ['self'],
        'abstract': False,
    },
    {
        'method_name': 'calculate_profit',
        'parameter_names': ['self'],
        'abstract': True,
    },
])
def test_event_methods(kwargs):
    assert has_method(
        event.Event,
        **kwargs), f"Event's method {kwargs['method_name']} is missing or incorrect"

#######
#
# FESTIVAL
#
#######

def test_festival_class_is_defined():
    assert 'Festival' in dir(event), 'Festival class has not been defined'


@if_class_exists('Festival')
def test_festival_class_is_not_abstract():
    assert not is_class_abstract(event.Festival)


@if_class_exists('Festival')
@pytest.mark.parametrize('kwargs', [
    {
        'method_name': '__init__',
        'parameter_names': ['self', 'name', 'number_of_stages','number_of_slots', 'number_of_attendees', 'ticket_price'],
        'abstract': False,
    },
    {
        'method_name': 'calculate_profit',
        'parameter_names': ['self'],
        'abstract': False,
    },
])
def test_festival_methods(kwargs):
    assert has_method(
        event.Festival,
        **kwargs), f"Festival's method {kwargs['method_name']} is missing or incorrect"

#######
#
# FREECONCERT
#
#######

def test_freeconcert_class_is_defined():
    assert 'FreeConcert' in dir(event), 'FreeConcert class has not been defined'


@if_class_exists('FreeConcert')
def test_freeconcert_class_is_not_abstract():
    assert not is_class_abstract(event.FreeConcert)


@if_class_exists('FreeConcert')
@pytest.mark.parametrize('kwargs', [
    {
        'method_name': '__init__',
        'parameter_names': ['self', 'name', 'number_of_slots'],
        'abstract': False,
    },
    {
        'method_name': 'calculate_profit',
        'parameter_names': ['self'],
        'abstract': False,
    },
    {
        'method_name': 'add_artist',
        'parameter_names': ['self', 'artist'],
        'abstract': False,
    },
])
def test_freeconcert_methods(kwargs):
    assert has_method(
        event.FreeConcert,
        **kwargs), f"FreeConcert's method {kwargs['method_name']} is missing or incorrect"