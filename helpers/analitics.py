from models import Post
from dotenv import load_dotenv

from mongoengine import connect


load_dotenv()


connect('dark_web',
        host=os.getenv('MONGO_URI'))


def get_total_pastes():
    return Post.objects.count()


def get_pastes_per_date():
    pipeline = [
        {"$group": {"$Author"}},
        {"$count": {"$sum": 1}}
    ]
    return Post.objects.aggregate(pipeline)


def get_pastes_by_author():
    return list(Post.objects().aggregate(
        {"$group": {"_id": "$Author",
                    "Total": {"$sum": 1}}}
    ))


def get_common_words():
    """
    :return: list with authors as keys and number of posts as value
    """
    analytics_obj = {
        "total_Posts_bitcoin": Post.objects(Title__icontains='bitcoin').count(),
        "total_Posts_porn": Post.objects(Title__icontains='porn').count(),
        "total_Posts_gun": Post.objects(Title__icontains='gun').count(),
        "total_Posts_creditcard": Post.objects(Title__icontains='creditcard').count(),
        "total_Posts_onion": Post.objects(Title__icontains='onion').count(),
        "total_Posts_drug": Post.objects(Title__icontains='drug').count(),
        "total_Posts_hack": Post.objects(Title__icontains='hack').count(),
        "total_Posts_leak": Post.objects(Title__icontains='leak').count(),
        "total_Posts_child": Post.objects(Title__icontains='child').count(),
        "total_Posts_dark": Post.objects(Title__icontains='dark').count(),
    }
    return analytics_obj
