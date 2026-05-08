# Nyancat terminal animation — renders 12-frame loop with ANSI colour to stdout.
import argparse
import datetime
import os
import random
import signal
import sys
import time

from frame import frames
from schemes import ColourScheme, SCHEMES


FRAME_HEIGHT = 64
FRAME_WIDTH = 64

# ANSI terminal control sequences
ANSI_HIDE_CURSOR = '\033[?25l'
ANSI_SHOW_CURSOR = '\033[?25h'
ANSI_CLEAR_SCREEN = '\033[2J'
ANSI_CURSOR_HOME = '\033[H'
ANSI_RESET = '\033[0m'

# Pixel rendering
PIXEL_CHAR = ' '  # single space rendered with a background colour

# Frame timing
FRAME_DELAY_SECS = 0.06  # ~17 fps

# Rainbow geometry — row range within the 64-row frame where the rainbow trail appears
RAINBOW_START_ROW = 23
RAINBOW_END_ROW = 43
RAINBOW_ROW_OFFSET = 23     # vertical origin for mapping frame rows to rainbow stripe indices
RAINBOW_COL_OFFSET = 2      # horizontal phase shift for the stripe pattern
RAINBOW_STRIPE_PERIOD = 16  # pixel width of one full stripe cycle
RAINBOW_STRIPE_HALF = 8     # half-period — maps a column position to 0 or 1
ANIMATION_SPEED_DIVISOR = 2  # number of frames each stripe phase is held before advancing

PRIDE_MONTH = 6  # June

# Scheme auto-selected on each country's national day (month, day)
NATIONAL_DAYS: dict[tuple[int, int], str] = {
    (3, 8):  'pinks',     # International Women's Day
    (3, 17): 'ireland',   # St. Patrick's Day
    (8, 15): 'india',     # India Independence Day
    (9, 2):  'sealand',   # Sealand founding
    (10, 1): 'cyprus',    # Cyprus Independence Day
    (10, 12): 'spain',    # Fiesta Nacional de España
}


def terminal_size():
    '''Return (rows, cols) of the current terminal.'''
    size = os.get_terminal_size()
    return size.lines, size.columns


def rainbow_color(col, row, frame_idx, scheme: ColourScheme):
    mod_col = ((-col + RAINBOW_COL_OFFSET) % RAINBOW_STRIPE_PERIOD) // RAINBOW_STRIPE_HALF
    if (frame_idx // ANIMATION_SPEED_DIVISOR) % 2:
        mod_col = 1 - mod_col
    rainbow = scheme['rainbow']
    rainbow_row = mod_col + row - RAINBOW_ROW_OFFSET
    if -1 < rainbow_row < len(rainbow):
        return rainbow[rainbow_row]
    return ','


def pixel_color(col, row, frame_idx, min_col, min_row, scheme: ColourScheme):
    actual_col = col + min_col
    actual_row = row + min_row

    if RAINBOW_START_ROW < actual_row < RAINBOW_END_ROW and actual_col < 0:
        return rainbow_color(actual_col, actual_row, frame_idx, scheme)

    if actual_col < 0 or actual_row < 0 or actual_row >= FRAME_HEIGHT or actual_col >= FRAME_WIDTH:
        return ','

    return frames[frame_idx][actual_row][actual_col]


def render_frame(frame_idx, min_row, max_row, min_col, max_col, scheme: ColourScheme):
    colors = scheme['colors']
    last_color = None

    for row in range(max_row - min_row):
        for col in range(max_col - min_col):
            color = pixel_color(col, row, frame_idx, min_col, min_row, scheme)
            if color != last_color and color in colors:
                last_color = color
                sys.stdout.write(colors[color] + PIXEL_CHAR)
            else:
                sys.stdout.write(PIXEL_CHAR)
        sys.stdout.write('\n')
        last_color = None


def compute_viewport(terminal_height, terminal_width):
    min_col = (FRAME_WIDTH - terminal_width // 2) // 2
    max_col = (FRAME_WIDTH + terminal_width // 2) // 2
    min_row = (FRAME_HEIGHT - (terminal_height - 1)) // 2
    max_row = (FRAME_HEIGHT + (terminal_height - 1)) // 2
    return min_col, max_col, min_row, max_row


def select_default_scheme() -> str:
    '''Pick a scheme by date: national days, pride month, or rainbow as fallback.'''
    today = datetime.date.today()
    national_day_scheme = NATIONAL_DAYS.get((today.month, today.day))
    if national_day_scheme:
        return national_day_scheme
    if today.month == PRIDE_MONTH:
        return 'trans'
    return 'rainbow'


def parse_args() -> argparse.Namespace:
    '''Parse command-line arguments.'''
    parser = argparse.ArgumentParser(description='Nyancat terminal animation.')
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '--scheme',
        choices=list(SCHEMES.keys()),
        default=None,
        help='Colour scheme',
    )
    group.add_argument(
        '--random',
        action='store_true',
        help='Pick a random colour scheme',
    )
    return parser.parse_args()


class Nyancat:
    def __init__(self, scheme: ColourScheme):
        self._scheme = scheme
        self._needs_clear = False
        self._update_viewport()
        signal.signal(signal.SIGWINCH, self._on_resize)

    def _update_viewport(self):
        height, width = terminal_size()
        self.min_col, self.max_col, self.min_row, self.max_row = compute_viewport(height, width)

    def _on_resize(self, sig, frame):
        self._update_viewport()
        self._needs_clear = True

    def run(self):
        frame_idx = 0
        sys.stdout.write(ANSI_HIDE_CURSOR)
        sys.stdout.write(ANSI_CLEAR_SCREEN)
        try:
            while True:
                if self._needs_clear:
                    sys.stdout.write(ANSI_CLEAR_SCREEN)
                    self._needs_clear = False
                sys.stdout.write(ANSI_CURSOR_HOME)
                render_frame(frame_idx, self.min_row, self.max_row, self.min_col, self.max_col, self._scheme)

                sys.stdout.flush()

                frame_idx = (frame_idx + 1) % len(frames)
                time.sleep(FRAME_DELAY_SECS)
        finally:
            sys.stdout.write(ANSI_SHOW_CURSOR)
            sys.stdout.write(ANSI_RESET + '\n')


def main():
    args = parse_args()
    if args.random:
        scheme_name = random.choice(list(SCHEMES.keys()))
    else:
        scheme_name = args.scheme or select_default_scheme()
    nyancat = Nyancat(SCHEMES[scheme_name])
    nyancat.run()


if __name__ == '__main__':
    main()
