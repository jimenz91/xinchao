from django.http import HttpRequest, JsonResponse
import menu


def index(request: HttpRequest, model_name: str) -> JsonResponse:
    """
    Get all the items from a model.

    Args:
        request (HttpRequest): The request executed.
        model (Model): The model requested.

    Returns:
        JsonResponse: the list of items requested.
    """

    if request.method == 'GET':

        model = getattr(menu.models, model_name.capitalize())

        items = model.objects.all().values()

        return JsonResponse({"items": list(items)})


def item_detail(
        request: HttpRequest,
        model_name: str,
        id: int
) -> JsonResponse:
    """
    Endpoint for getting one item from a model.

    Args:
        request (HTTP Request): The request executed.

    Returns:
        JsonResponse: the item requested.
    """

    if request.method == 'GET':

        model = getattr(menu.models, model_name.capitalize())

        item = model.objects.filter(id=id).values()

        return JsonResponse({"item": list(item)})


def filtered(request: HttpRequest, model_name: str) -> JsonResponse:
    """
    A list of itmes filtered by specific fields.

    Args:
        request (HttpRequest): The request executed.
        model (Model): The model requested.

    Returns:
        JsonResponse: the list of items requested.
    """

    kws = request.GET.dict()

    model = getattr(menu.models, model_name.capitalize())

    items = model.objects.filter(**kws).values()

    return JsonResponse({"items": list(items)})
