#!usr/bin/env python3
# -*- coding: utf-8 -*-

"""
pytest demo module by grouping tests into class.
The module name must start with "test_" or end with "_test".
"""

__author__ = 'Ziang Lu'

import sys
import pytest

from my_dict import MyDict


class TestDict:

    # @pytest.mark.skip(
    #     reason='No need to test the constructor for the time being'
    # )
    @pytest.mark.skipif(
        sys.version_info < (3, 4), reason='Too low Python version'
    )
    def test_init(self):
        d = MyDict(a=1, b='test')
        assert isinstance(d, dict)
        assert d.a == 1
        assert d.b == 'test'

    @pytest.mark.skipif(
        sys.version_info < (3, 4), reason='Too low Python version'
    )
    def test_key(self):
        d = MyDict()
        d['key'] = 'value'
        assert d.key == 'value'

    @pytest.mark.skipif(
        sys.version_info < (3, 4), reason='Too low Python version'
    )
    def test_key_error(self):
        d = MyDict()
        with pytest.raises(KeyError):
            d['key']

    @pytest.mark.skipif(
        sys.version_info < (3, 4), reason='Too low Python version'
    )
    def test_attr(self):
        d = MyDict()
        d.key = 'value'
        assert 'key' in d
        assert d['key'] == 'value'

    @pytest.mark.skipif(
        sys.version_info < (3, 4), reason='Too low Python version'
    )
    def test_attrerror(self):
        d = MyDict()
        with pytest.raises(AttributeError):
            d.key
