from fastapi import FastAPI, APIRouter
from scripts.scanner import do_ping_sweep, sent_http_request

router = APIRouter()


@router.get("/scan")
def run_scan(ip: str, count: int):
    results_dct = {}
    for nhost in range(count):
        results_dct.update(do_ping_sweep(ip, nhost))
    return results_dct


@router.post("/sendhttp")
def run_send_http(target: str, method: str, header: str = None, header_value: str = None):
    hd = {header: header_value} if (header and header_value) else None
    return sent_http_request(target, method, hd)


app = FastAPI()
app.include_router(router)
