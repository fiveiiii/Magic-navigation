def router_init(app: FastAPI) -> None:
    app.include_router(
        cdn_views.router,
        prefix=configs.API_V1_STR,
        responses={404: {"description": "Not found"}},
    )
