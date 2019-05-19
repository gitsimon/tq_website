from django.contrib.auth.models import User


def find_duplicate_users():
    """find duplicates for all users in the system"""
    duplicates = dict()
    done = set()
    for user in User.objects.all():

        if user.id not in done:
            duplicates_of_user = _find_duplicates_of(user)
            if len(duplicates_of_user) > 1:
                duplicates[duplicates_of_user[0]] = duplicates_of_user[1:]
                done.update(duplicates_of_user)
    return duplicates


# finds duplicates of the given user
def _find_duplicates_of(user):
    """
    Finds duplicates of user. Returns a list of ids including user's id, ordered by last login user joined the system.
    """
    if user.email is None or user.email == "":
        return list()

    candidates = list(User.objects.filter(email=user.email).order_by('-last_login'))
    # candidates intentionally also includes the passed user
    return list({u.id for u in candidates})