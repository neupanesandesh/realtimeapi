import functools
import time
import json
import os
import logging
import asyncio
from datetime import datetime
from enum import Enum
import pyaudio



# Audio recording parameters
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 24000



PREFIX_PADDING_MS = 300
SILENCE_THRESHOLD = 0.5
SILENCE_DURATION_MS = 700


