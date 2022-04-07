from mcdreforged.api.all import *

from carpet_tick import info_parser
from carpet_tick import common
from carpet_tick.common import metadata, tr

PREFIX = '!!tick'


def show_help(source: CommandSource):
    source.reply(tr('help_message', name=metadata.name, version=metadata.version, prefix=PREFIX))


def health(source: CommandSource, ticks=100):
    server = source.get_server()
    server.execute('carpet commandTick true')
    server.execute('tick health %s' % ticks)
    server.execute('carpet commandTick false')


def entities(source: CommandSource, ticks=100):
    server = source.get_server()
    server.execute('carpet commandTick true')
    server.execute('tick entities %s' % ticks)
    server.execute('carpet commandTick false')


def register_commands(server: PluginServerInterface):
    server.register_command(
        Literal(PREFIX)
        .requires(lambda src: src.has_permission(common.config.permission), lambda: tr('permission_denied'))
        .runs(show_help)
        .then(Literal('health').runs(lambda src: health(src))
              .then(Integer('ticks').at_min(20).at_max(24000).runs(lambda src, ctx: health(src, ctx['ticks']))))
        .then(Literal('entities').runs(lambda src: entities(src))
              .then(Integer('ticks').at_min(20).at_max(24000).runs(lambda src, ctx: entities(src, ctx['ticks']))))
        .then(Literal('h').runs(lambda src: health(src))
              .then(Integer('ticks').at_min(20).at_max(24000).runs(lambda src, ctx: health(src, ctx['ticks']))))
        .then(Literal('e').runs(lambda src: entities(src))
              .then(Integer('ticks').at_min(20).at_max(24000).runs(lambda src, ctx: entities(src, ctx['ticks']))))
    )


def on_info(server: PluginServerInterface, info: Info):
    if not info.is_user and info_parser.accept(info.content):
        server.say('§7§o' + info.content)


def on_load(server: PluginServerInterface, old):
    common.load_common()
    register_commands(server)
    server.register_help_message(PREFIX, tr("help_summary"))
