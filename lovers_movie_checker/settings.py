from .metaconfig.types import ConfigRoot, StrField, IntField, BoolField, Fieldset
from .metaconfig.io import YAMLFileConfigIO


class Config(ConfigRoot):
    __io_class__ = YAMLFileConfigIO('settings.yaml')

    port = IntField(label='Application Port', default=5000)


class DevConfig(ConfigRoot):
    __io_class__ = YAMLFileConfigIO('dev.env')

    in_dev = BoolField(label='In Development', default=False)