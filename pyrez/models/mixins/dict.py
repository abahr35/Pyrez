
#!/usr/bin/env python
# encoding: utf-8
# -*- coding: utf-8 -*-

class Dict(dict):
  def __init__(self, **kw):
    """It can act both as a dictionary (c['foo']) and as an object (c.foo) to get values."""
    dict.__init__(self, kw or {})
    self.__kwargs__ = kw or []
  '''
  def get(self, key, default=None):
    return self.__kwargs__.get(key, default)
  def __getitem__(self, key):
    try:
        return self.__kwargs__[key]
    except KeyError:
        return None
  '''
  def __str__(self):
    import json
    return json.dumps(self.__kwargs__ or {}, ensure_ascii=False, sort_keys=False, indent=2)