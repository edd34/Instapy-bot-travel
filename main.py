from instapy import InstaPy
from instapy import smart_run
from parameters.comments import param_comments
from parameters.dont_likes import dont_likes
import os
from dotenv import load_dotenv
load_dotenv()

session = InstaPy(username=os.getenv("USERNAME") , password=os.getenv("PASSWORD"))

# let's go! :>
with smart_run(session):
    # settings
    session.set_user_interact(amount=3, randomize=True, percentage=100,
                              media='Photo')
    session.set_relationship_bounds(enabled=False)
    session.set_simulation(enabled=False)
    session.set_comments(param_comments)
    session.set_do_like(enabled=True, percentage=100)
    session.set_do_comment(enabled=True, percentage=50)
    session.set_do_follow(enabled=True, percentage=100)
    session.set_ignore_if_contains(dont_likes)

    # activity
    list_tags = ['travel', 'travelphotography', "traveladdict", "triplovers", "travelphotography", "travelgram"]
    session.like_by_tags(list_tags, amount=25)
    session.follow_by_tags(list_tags, amount=25)
