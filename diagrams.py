from fastapi import APIRouter

from my_finance.models import DiagramModel
from my_finance.stock.diagram.figure import show_simple_diagram, create_and_save_to_file

diagrams_router = APIRouter(prefix="/diagrams")


@diagrams_router.get("/{ticker_id}")
def draw_a_diagram(ticker_id: str, info: str = "Close"):
    show_simple_diagram(ticker_id, info)


@diagrams_router.post("")
def create_a_diagram(model: DiagramModel):
    create_and_save_to_file(model)