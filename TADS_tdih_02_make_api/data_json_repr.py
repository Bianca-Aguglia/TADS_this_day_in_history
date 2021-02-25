"""
JSON representation of events.
This is for reference only.
"""

# single event
{
    "id": 123, # event_id in db
    "day": 1,
    "month": 1,
    "year": 153,
    "bc_ad": "BC",
    "event_type": "events", # 'events', 'birthdays', 'deaths', 'holidays_and_observances'
    "event_description": "For the first time, Roman consuls begin their year in office on January 1.",
    "event_category": "Pre-1600", # this is the data fron <h3> tag (if any)
    "event_relative_score": 120, # score based on all events for day and month of this event (120 is a dummy value for now)
    "event_absolute_score": 8493, # score based on all events in the wikipedia_tdih.db (8493 is a dummy value for now)
    "event_links": [
        {
            "text": "Roman consul",
            "url": "https://en.wikipedia.org/wiki/Roman_consul",
            "is_subject_link": 1 # 1 = True, 0 = False (determines what to use for score, image, and coordinates)
            "created_at": "placeholder for date",
            "coordinates": "placeholder for coordinates"
            }
    ]
    "event_images": [
        {
            "image_file": "https://en.wikipedia.org/wiki/Roman_consul#/media/File:Roman_SPQR_banner.svg",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/9/98/Roman_SPQR_banner.svg",
            "image_repository_type": "shared",
            "image_license": "CC BY 3.0",
            "image_attribution": "Ssolbergj",
            "image_created_at": "placedholder for date"
            }
    ]
    "event_coordinates": "placeholder for coordinates" # same as coordinates for is_subject_link = 1 (extracted here for discoverability
}

# event collections
{
    "items": [
        { ... event resource ... },
        { ... event resource ... },
        ...
    ],
    "_meta": {
        "page": 1,
        "per_page": 10,
        "total_pages": 20,
        "total_items": 195
    },
    "_links": {
        "self": "http://localhost:5000/api/events?page=1",
        "next": "http://localhost:5000/api/events?page=2",
        "prev": null
    }
}

# errors
{
    "error": "short error description",
    "message": "error message (optional)"
}




# virtual fields:
    # event_relative_score (determined after querying the database and ordering results by score)
    # event_absolute score 

# questions
    # 1. have id for collection of events?
    # 2. include image_usage_info?

# reference examples from 
# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xxiii-application-programming-interfaces-apis
    
# single user
{
    "id": 123,
    "username": "susan",
    "password": "my-password",
    "email": "susan@example.com",
    "last_seen": "2017-10-20T15:04:27Z",
    "about_me": "Hello, my name is Susan!",
    "post_count": 7,
    "follower_count": 35,
    "followed_count": 21,
    "_links": {
        "self": "/api/users/123",
        "followers": "/api/users/123/followers",
        "followed": "/api/users/123/followed",
        "avatar": "https://www.gravatar.com/avatar/..."
    }
}

# collections of users
{
    "items": [
        { ... user resource ... },
        { ... user resource ... },
        ...
    ],
    "_meta": {
        "page": 1,
        "per_page": 10,
        "total_pages": 20,
        "total_items": 195
    },
    "_links": {
        "self": "http://localhost:5000/api/users?page=1",
        "next": "http://localhost:5000/api/users?page=2",
        "prev": null
    }
}

# errors
{
    "error": "short error description",
    "message": "error message (optional)"
}

