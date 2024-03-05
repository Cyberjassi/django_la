from rest_framework.throttling import AnonRateThrottle,UserRateThrottle

class LocalThrottling(UserRateThrottle):
    scope = 'jack'