def get_client_ip(request):
    """
    Get client ip address.
    
    Detect ip address provided by HTTP_X_REAL_IP, HTTP_X_FORWARDED_FOR and REMOTE_ADDR meta headers.
    
    :param request: django request
    :return: ip address
    """

    real_ip = request.META.get('HTTP_X_REAL_IP')
    if real_ip:
        return real_ip

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0]

    return request.META.get('REMOTE_ADDR')
