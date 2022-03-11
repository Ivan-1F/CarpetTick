from typing import TYPE_CHECKING

from mcdreforged.api.all import *

if TYPE_CHECKING:
    from carpet_tick.config import Configure

server_inst = ServerInterface.get_instance().as_plugin_server_interface()
metadata = server_inst.get_self_metadata()
config: 'Configure'


def load_common():
    from carpet_tick.config import Configure
    global config
    config = Configure.load()


def tr(key: str, *args, **kwargs):
    return server_inst.tr('{}.{}'.format(metadata.id, key), *args, **kwargs)
