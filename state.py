import tcod
import tcod.event

import gamemap


class GameState(tcod.event.EventDispatch):

    MOVE_KEYS = {
        tcod.event.K_LEFT: (-1, 0),
        tcod.event.K_RIGHT: (1, 0),
        tcod.event.K_UP: (0, -1),
        tcod.event.K_DOWN: (0, 1),
        tcod.event.K_HOME: (-1, -1),
        tcod.event.K_END: (-1, 1),
        tcod.event.K_PAGEUP: (1, -1),
        tcod.event.K_PAGEDOWN: (1, 1),
        tcod.event.K_KP_1: (-1, 1),
        tcod.event.K_KP_2: (0, 1),
        tcod.event.K_KP_3: (1, 1),
        tcod.event.K_KP_4: (-1, 0),
        tcod.event.K_KP_6: (1, 0),
        tcod.event.K_KP_7: (-1, -1),
        tcod.event.K_KP_8: (0, -1),
        tcod.event.K_KP_9: (1, -1),
        tcod.event.K_h: (-1, 0),
        tcod.event.K_j: (0, 1),
        tcod.event.K_k: (0, -1),
        tcod.event.K_l: (1, 0),
        tcod.event.K_y: (-1, -1),
        tcod.event.K_u: (1, -1),
        tcod.event.K_b: (-1, 1),
        tcod.event.K_n: (1, 1),
    }

    def __init__(self, active_map: gamemap.GameMap):
        self.active_map = active_map

    def on_draw(self, console: tcod.console.Console) -> None:
        console.clear()
        self.active_map.render(console)
        tcod.console_flush()

    def ev_quit(self, event: tcod.event.Quit) -> None:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> None:
        if event.sym == tcod.event.K_ESCAPE:
            raise SystemExit()
        elif event.sym in self.MOVE_KEYS:
            self.cmd_move(*self.MOVE_KEYS[event.sym])

    def cmd_move(self, x: int, y: int) -> None:
        player = self.active_map.player
        if not self.active_map.is_blocked(*player.relative(x, y)):
            player.move_by(x, y)