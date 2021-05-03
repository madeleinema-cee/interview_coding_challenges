
def validate_params_exist(request, required_params):
    passed_params = [x for x in request.args.keys()]
    return set(required_params).issubset((set(passed_params)))