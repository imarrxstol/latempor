def get_profile_cache_path(ads_id, path_ads):
    """Returns the cache path for a profile.

    Args:
        ads_id: The Ads ID of the profile.
        path_ads: The path to the Ads directory.

    Returns:
        The cache path for the profile.
    """

    return os.path.join(path_ads, ads_id)

