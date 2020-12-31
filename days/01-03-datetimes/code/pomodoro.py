"""A script to start a pomodoro timer.
work 25 minute, break five minutes
Durations can be customize. Cycles the indicated number of times."""

from datetime import datetime
from datetime import timedelta
import time
import os
import click


def countdown(x, now=datetime.now):
    """A simple countdown using datetime, timedelta and time.sleep printing the 
    remaining time on console.
    From https://codereview.stackexchange.com/questions/199743/countdown-timer-in-python
    """
    target = now()
    one_second_later = timedelta(seconds=1)
    for remaining in range(x, 0, -1):
        target += one_second_later
        print(timedelta(seconds=remaining), 'remaining', end='\r')
        time.sleep((target - now()).total_seconds())
    os.system('afplay /System/Library/Sounds/Glass.aiff')


def pomodoro_cycle(n=4, w=25, b=5):
    """Cycles the timer n number of times giving feedback

    Args:
        n (int, optional): Number of pomodoro cycles. Defaults to 4.
        w (int, optional): Work period duration. Defaults to 25.
        b (int, optional): Break period duration. Defaults to 5.
    """
    i = 1
    while n:
        click.echo(f"\nStarting session {i}.")
        countdown(w)
        if n > 1:
            click.echo("\nTake a break.")
            countdown(b)
        n -= 1
        i +=1
    click.echo("You're done. Good work!")


@click.command()
@click.argument('n', type=int, default=4)
@click.option('-c', is_flag=True, help="Custumize timer duration")
def main_cli(n, c):
    """Call the pomodoro timer program with arguments\n
        [OPTION] number of repeats\n
        [-c] customize durations
    """
    if c:
        w = int(input("Work duration: "))
        b = int(input("Break duration: "))
        pomodoro_cycle(n, w, b)
    else:
        pomodoro_cycle()


if __name__ == "__main__":
    main_cli()
