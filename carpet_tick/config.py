from mcdreforged.api.all import *

from carpet_tick import common


class Configure(Serializable):
    permission: int = PermissionLevel.PHYSICAL_SERVER_CONTROL_LEVEL

    @staticmethod
    def get_psi() -> PluginServerInterface:
        return common.server_inst

    @classmethod
    def load(cls) -> 'Configure':
        return cls.get_psi().load_config_simple(target_class=cls)

    def save(self):
        self.get_psi().save_config_simple(self)
