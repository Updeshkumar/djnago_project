from account.models import profileofall


def allowed_func(request):
    try:
        is_vehicle = False 
        is_driver = False
        is_labour = False
        is_sub = False
        is_user = False
        if request.user.is_authenticated:
            if not request.user.is_admin:

                obj=profileofall.objects.filter(user=request.user).first()
                if obj:
                    getprof=obj.role
                    
                    if getprof == 'heavy_vehicle':
                        is_vehicle=True
                    if getprof == 'driver':
                        is_driver=True
                    if getprof == 'subcontructor':
                        is_sub=True
                    if getprof == 'labour':
                        is_labour=True
                    if getprof == 'user':
                        is_user=True

        context={
            'is_vehicle':is_vehicle ,
            'is_driver':is_driver ,
            'is_labour':is_labour ,
            'is_sub':is_sub ,
            'is_user':is_user ,
        }
        return context
    except Exception as e:
        print("error",e)
        print("something went wrong at here in account.context_processors.py")
        return None