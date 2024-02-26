from typing import Union
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from .views import skill

async def http422_error_handler(
    _: Request, exc: Union[RequestValidationError, ValidationError]
) -> JSONResponse:
    print(await _.json())
    print(exc.errors())
    return JSONResponse(
        {"errors": exc.errors()}, status_code=422
    )


def create_app():
  app = FastAPI(
    title="Skill Hooks",
    version="0.0.0",
    description="Your description goes here",
  )

  # Add routes
  app.include_router(router=skill.router)
  app.add_exception_handler(ValidationError, http422_error_handler)
  app.add_exception_handler(RequestValidationError, http422_error_handler)


  return app