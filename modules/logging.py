import logging
import sys
from rich.logging import RichHandler
from rich.console import Console
from rich.text import Text

console = Console()

def setup_logging():
    # Set up logging with Rich
    logger = logging.getLogger("realtime_api")
    logger.setLevel(logging.INFO)
    handler = RichHandler(rich_tracebacks=True, console=console)
    formatter = logging.Formatter("%(message)s", datefmt="[%X]")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.propagate = False
    return logger

logger = setup_logging()

# Function to log WebSocket events
def log_ws_event(direction, event):
    event_type = event.get("type", "Unknown")
    emoji = "|"
    icon = "⬆️ - Out" if direction == "Outgoing" else "⬇️ - In"
    style = "bold cyan" if direction == "Outgoing" else "bold green"
    logger.info(Text(f"{emoji} {icon} {event_type}", style=style))

# def log_tool_call(function_name, args, result):
#     logger.info(Text(f"🛠️ Calling function: {function_name} with args: {args}", style="bold magenta"))
#     logger.info(Text(f"🛠️ Function call result: {result}", style="bold yellow"))

def log_error(message):
    logger.error(Text(message, style="bold red"))

def log_info(message, style="bold white"):
    logger.info(Text(message, style=style))

def log_warning(message):
    logger.warning(Text(message, style="bold yellow"))