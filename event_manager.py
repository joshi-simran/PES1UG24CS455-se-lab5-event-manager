import json
import secrets
from datetime import date

events = {}


def createEvent(eventName, venue, capacity=50, guests=[]):
    events[eventName] = {"venue": venue, "capacity": capacity,
                         "guests": guests}
    return events[eventName]


def registerGuest(eventName, guest):
    event = events.get(eventName)
    if event is None:
        print("No such event:", eventName)
        return False
    if len(event["guests"]) >= event["capacity"]:
        print(eventName, "is full, cannot add", guest)
        return False
    event["guests"].append(guest)
    return True


def seatsLeft(eventName):
    event = events[eventName]
    return event["capacity"] - len(event["guests"])


def eventStatus(eventDate):
    if eventDate >= date.today():
        return "Upcoming"
    else:
        return "Completed"


def guestReport(eventName, sortOrder):
    names = sorted(events[eventName]["guests"])
    return ", ".join(names)


def save_events(file_name="events.json"):
    """Save event data to a JSON file."""
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(events, file, indent=4)


def load_events(file_name="events.json"):
    """Load event data from a JSON file."""
    with open(file_name, "r", encoding="utf-8") as file:
        return json.load(file)

def print_badges(event_name):
    """Return the badge filename for an event."""
    if not event_name or not event_name.replace(" ", "").isalnum():
        raise ValueError("Invalid event name")
    return f"badges_{event_name}.txt"


def main():
    createEvent("Tech Meetup", "Hall A", 3)
    createEvent("Alumni Dinner", "Rooftop",2)
    registerGuest("Tech Meetup", "Asha")
    registerGuest("Tech Meetup", "Ravi")
    registerGuest("Alumni Dinner", "Meena")
    registerGuest("Workshop", "Kiran")
    left=seatsLeft("Tech Meetup")
    print("Seats left at Tech Meetup:", left)
    print("Seats left at Alumni Dinner:", seatsLeft("Alumni Dinner"))
    print("Tech Meetup guests:", guestReport("Tech Meetup", "name"))
    print("Tech Meetup is", eventStatus(date(2099, 1, 15)))
    print("Alumni Dinner is", eventStatus(date(2020, 5, 1)))
    winner = secrets.choice(events["Tech Meetup"]["guests"])
    print("Lucky draw winner:", winner)
    save_events()
    restored = load_events() # reload to confirm the save worked
    print("Events restored from file:", len(restored))
    print("Venues:", [e["venue"] for e in restored.values()])

main()