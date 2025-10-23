import curses

def battle_menu(stdscr, menu=None):
    """
    Displays a horizontal battle menu using curses and returns the selected option.
    
    Args:
        stdscr: The curses screen object (provided automatically by curses.wrapper)
        menu (list[str]): Optional list of menu options. Defaults to standard battle actions.
    
    Returns:
        str: The option the player selected.
    """
    if menu is None:
        menu = ["Attack", "Skill", "Guard", "Item", "Run"]

    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    stdscr.keypad(True)
    stdscr.nodelay(False)

    selected = 0

    while True:
        stdscr.clear()
        stdscr.addstr(0, 2, "== Battle Menu ==")

        # draw menu horizontally
        x_offset = 4
        y_pos = 2

        for i, option in enumerate(menu):
            if i == selected:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y_pos, x_offset, f"[{option}]")
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y_pos, x_offset, f" {option} ")
            x_offset += len(option) + 4  # spacing between options

        key = stdscr.getch()

        if key == curses.KEY_LEFT:
            selected = (selected - 1) % len(menu)
        elif key == curses.KEY_RIGHT:
            selected = (selected + 1) % len(menu)
        elif key in [curses.KEY_ENTER, 10, 13]:
            return menu[selected]

        stdscr.refresh()


def get_battle_choice(menu=None):
    """
    Wrapper to easily call the battle menu from anywhere in your game.
    Handles curses initialization and returns the result.
    """
    return curses.wrapper(battle_menu, menu)

if __name__ == "__main__":
    choice = get_battle_choice()
    print(f"You selected: {choice}")

