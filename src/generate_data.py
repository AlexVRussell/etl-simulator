import json
import random
import uuid
from datetime import datetime, timedelta

random.seed(42)

TRANSACTION_TYPES = []
STATUSES = []
CURRENCIES = ["USD", "CAD", "EUR"]
COUNTRIES = ["US", "CA", "GB"]
MERCHANTS = [
    "Amazon", "eBay", "Walmart", "Target", "Best Buy", "Apple", "Google", "Microsoft", "Netflix", "Spotify"
]